"""
Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu

This code creates a text file with all artist ids,
same as /Tasks_Demos/Name_Analysis
but faster since we use the sqlite database: track_metadata.db
Of course, it takes time to create the dataset ;)

This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.

Copyright 2010, Thierry Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import datetime
import glob
import os
import sys
import sqlite3
import string
import time

try:
    import numpy as np
except ImportError:
    print('you need numpy installed to use this program')
    print('run `pip install numpy` and try again')
    sys.exit(0)




def die_with_usage():
    print("""
    HELP MENU 
    list_all_artists_from_db.py
    by T. Bertin-Mahieux (2010) Columbia University
    
    mimics the program /Tasks_Demo/NamesAnalysis/list_all_artist.py
    but assumes the sqlite db track_metadata.py is available
    i.e. it takes a few second instead of a few hours!
    
    To download track_metadata.db, see Million Song website
    to recreate it, see create_track_metadata.py

    Usage:
        python list_all_artists_from_db.py track_metadata.db output.txt
        creates a file where each line is: (one line per artist)
        artist id<SEP>artist mbid<SEP>track id<SEP>artist name
    """)
    sys.exit(0)



if __name__ == '__main__':

    # help menu
    if len(sys.argv) < 3:
        die_with_usage()

    # params
    dbfile = sys.argv[1]
    output = sys.argv[2]

    # sanity check
    if not os.path.isfile(dbfile):
        print('ERROR: can not find database:',dbfile)
        sys.exit(0)
    if os.path.exists(output):
        print('ERROR: file',output,'exists, delete or provide a new name')
        sys.exit(0)

    # start time
    t1 = time.time()

    # connect to the db
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    # get what we want
    q = 'SELECT artist_id,artist_mbid,track_id,artist_name FROM songs'
    q += ' GROUP BY artist_id  ORDER BY artist_id'
    res = c.execute(q)
    alldata = res.fetchall()
    # DEBUGGING
    q = 'SELECT DISTINCT artist_id FROM songs'
    res = c.execute(q)
    artists = res.fetchall()
    print('found',len(artists),'distinct artists')
    assert len(alldata) == len(artists), 'incoherent sizes'
    # close db connection
    c.close()
    conn.close()

    # write to file
    f = open(output,'w')
    for data in alldata:
        f.write(data[0]+'<SEP>'+data[1]+'<SEP>'+data[2]+'<SEP>')
        f.write( data[3].encode('utf-8') + '\n' )
    f.close()

    # done
    t2 = time.time()
    stimelength = str(datetime.timedelta(seconds=t2-t1))
    print('file',output,'with',len(alldata),'artists created in',stimelength)

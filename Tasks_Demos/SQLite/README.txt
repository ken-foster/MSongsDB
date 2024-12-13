/Tasks_Demos/SQLite/README.txt
   by T. Bertin-Mahieux (2010) Columbia University
      tb2332@columbia.edu

This folder contains code to create SQLite databses to help us
search through the Million Song database.
The SQLite databases can be downloaded (if not provied with the
dataset in the first place)
Look at the demo to see how to use them.

The first database should have 1M row, one per track, and contain
the metadata (artist id, album id, track id, names, ...)

The second database should have one row per artist and one column
per tag, and is binary, e.g. this artist got that term.

Code in progress, write me for question / comments / status report: 
tb2332@columbia.edu

# ken-foster edits

Steps
1. list_all_artists_from_db.py
2. list_all_tracks_from_db.py
3. create_artist_similarity_db.py
4. create_artist_terms_db.py
5. create_track_metadata_db.py

The demo files (listed below) are for people who don't know how to SQL
- demo_artist_similarity.py
- demo_artist_term.py
- demo_track_metadata.py

from datetime import date

import models
from database import engine, SessionLocal
from models import Song

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(Song).count() == 0:
    songs = [
        Song(title='Smells Like Teen Spirit', artist='Nirvana', release_date=date(1991, 9, 10)),
        Song(title='Here Comes The Sun', artist='The Beatles', release_date=date(1969, 8, 19)),
        Song(title='Karma Police', artist='Radiohead', release_date=date(1997, 8, 25)),
        Song(title='Get Lucky', artist='Daft Punk', release_date=date(2013, 4, 19)),
    ]

    for song in songs:
        db.add(song)

    db.commit()

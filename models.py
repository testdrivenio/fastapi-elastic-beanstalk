from sqlalchemy import Column, Integer, String, Date

from database import Base


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    artist = Column(String(128), nullable=False)
    release_date = Column(Date, nullable=False)

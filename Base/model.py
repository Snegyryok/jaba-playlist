from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base

playlist_tracks = Table(
    "playlist_tracks",
    Base.metadata,
    Column("track_id", ForeignKey("tracks.id"), primary_key=True),
    Column("playlist_id", ForeignKey("playlists.id"), primary_key=True),
)


class Track(Base):
    __tablename__ = "tracks"


    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(primary_key=False)
    source: Mapped[str] = mapped_column(String, nullable=False)
    link: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    added_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    playlists = relationship(
        "Playlist",
        secondary=playlist_tracks,
        back_populates="tracks")


class Playlist(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    tracks = relationship(
        "Track",
        secondary="playlist_tracks",
        back_populates="playlists",
    )


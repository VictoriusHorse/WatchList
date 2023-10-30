from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    owner_id = Column(Integer, ForeignKey("users.id"))
    movieId = Column(Integer, index=True)
    rating = Column(String(50), index=True)
    id = Column(Integer, primary_key=True, index=True)

    owner = relationship("User", back_populates="items")

class Movie(Base):
    __tablename__ = "Movies"
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    genres = Column(String(50), index=True)
    poster = Column(String(255))

class Recommend(Base):
    __tablename__ = "recommend"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    movieId = Column(Integer, index=True)
    userId = Column(Integer, index=True)


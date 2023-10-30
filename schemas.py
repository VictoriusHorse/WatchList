from pydantic import BaseModel

class ItemBase(BaseModel):
    movieId: int
    rating: float


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

class Movie(BaseModel):
    movieId: int
    title: str
    genres: str

class Poster(BaseModel):
    poster: bytes


class Recommend (BaseModel):
    id: int
    title: str
    movieId: int
    userId: int
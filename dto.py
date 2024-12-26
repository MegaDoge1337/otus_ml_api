from typing import Optional

from pydantic import BaseModel


class Features(BaseModel):
    paws_count: int
    has_fur: int
    mammal: int


class User(BaseModel):
    username: str
    email: str
    age: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

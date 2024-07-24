from pydantic import BaseModel


class Jobs(BaseModel):
    title: str
    area: str
    type: str
    company: str


class Names(BaseModel):
    first: str
    last: str


class User(BaseModel):
    status: str
    name: Names
    username: str
    password: str
    email: str
    phoneNumber: str
    job: Jobs
    uuid: str


class Users(BaseModel):
    users: list[User]

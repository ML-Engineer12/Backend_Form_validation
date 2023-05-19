from pydantic import BaseModel


class Schema(BaseModel):
    id: int
    name: str
    email: str


class InSchema(Schema):
    password: str

    class Config:
        orm_mode = True


class OutSchema(Schema):
    pass
    class Config:
        orm_mode = True

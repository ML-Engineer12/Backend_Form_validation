from sqlalchemy.orm import Session
from . import schema, model


def get_user_by_email(db:Session, email:str):
    return db.query(model.User).filter(model.User.email == email).first()

def create_user(db:Session, user:schema.InSchema):
    db_user = model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
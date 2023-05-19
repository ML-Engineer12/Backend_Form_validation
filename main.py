from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . database import engine, SessionLocal, get_db
from . import model, schema, crud

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/user", response_model=schema.OutSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: schema.InSchema, db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db , user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already in use")
    else:
        return crud.create_user(db=db, user=user)


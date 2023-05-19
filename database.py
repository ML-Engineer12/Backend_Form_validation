from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#we need to have an independent session/connection with database per request
# use the same session through all the resquest and then close it after the request is finished
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALchemy_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALchemy_DATABASE_URL, connect_args={'check_same_thread': False})

# SessionLocal is to create dependencies
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
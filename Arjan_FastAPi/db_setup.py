from sqlalchemy import create_engine, Column ,Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Database Setup
engine = create_engine("sqlite:///tools.db", connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Database Model
class Item(Base):
    __tablename__ = "Items"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False,unique=True)
    price = Column(Float,nullable=False)
    count = Column(Integer,nullable=True)
    category = Column(String,nullable=False)

Base.metadata.create_all(engine)

#Coneccion a db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql://postgres:325378@localhost:5432/basic_inventory"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush = False, bind=engine)




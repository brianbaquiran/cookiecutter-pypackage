import os
import sys
from sqlalchemy import create_engine

from .models import Base

if __name__ == '__main__':
    db_uri = os.getenv('DB_URI')
    if db_uri is None:
        print("Error: Environment variable DB_URI is not set.")
        sys.exit(1)
    engine = create_engine(db_uri, echo=True)
    Base.metadata.create_all(bind=engine)

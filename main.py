from sqlalchemy import create_engine
import config

from models.base import Base

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO)


def main():
    Base.metadata.create_all(bind=engine)
    
    
    
if __name__ == "__main__":
    main()    

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, selectinload, joinedload
import config

from typing import Iterable

from models import Base, Address, User


engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)


def create_user(session: Session, name: str, username: str) -> User:
    user = User(name=name, username=username)

    session.add(user)
    session.commit()

    return user


def create_user_with_emails(
    session: Session, name: str, username: str, emails: list
) -> User:
    addresses = [Address(email=email) for email in emails]

    user = User(name=name, username=username, addresses=addresses)

    session.add(user)
    session.commit()

    return user


def add_addresses(session: Session, user: User, *emails: str) -> None:
    user.addresses = [Address(email=email) for email in emails]
    session.commit()


def fetch_user(session: Session, name: str) -> User:
    stm = select(User).where(User.name == name)
    user: User | None = session.execute(stm).scalar_one()
    return user




def show_users(session:Session):
    stmt = select(User).options(
        selectinload(User.addresses)
    )
    
    users :Iterable[User] = session.scalars(stmt)
    
    for user in users:
        print('\n[+]',user)
        for address in user.addresses:
            print(address.email)
    ...



def show_addresses(session:Session):
    stmt = select(Address).options(
        joinedload(Address.user)
    )
    addresses: Iterable[Address]= session.scalars(stmt)
    
    for address in addresses:
        print (f"[+] {address.email}")
        print (f" + {address.user}")
        
    
    
    pass


def main():
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        # create_user(session=session, name="Bob White", username="bob")

        # create_user_with_emails(
        #     session=session,
        #     name="John Smith",
        #     username="john",
        #     emails=["john.smit@example.gov", "john@example.com"],
        # )
        # user = fetch_user(session=session, name="Bob White")
        # print("bob?", user)
        
        
        # add_addresses(session,user, "bob@example.com")
        show_addresses(session=session)


if __name__ == "__main__":
    main()

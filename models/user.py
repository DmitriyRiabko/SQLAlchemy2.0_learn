from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from address import Address
    

from base import Base



class User(Base):
    __tablename__ = 'users'
    

    id :Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    username: Mapped[str | None]
    
    addresses:Mapped[list['Address']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan')
    

    def __str__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, username={self.username!r})"

    def __repr__(self) -> str:
        return str(self)
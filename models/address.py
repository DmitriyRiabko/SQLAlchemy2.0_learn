
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import  ForeignKey


from .base import Base


if TYPE_CHECKING:
  from user import User


    
class Address(Base):
    __tablename__ = 'addresses'
    
    id :Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str]
    
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    user:Mapped['User'] = relationship(back_populates='addresses')

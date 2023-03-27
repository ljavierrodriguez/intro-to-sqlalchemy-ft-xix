from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import List, Optional, String, ForeignKey

class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = 'contacts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120), unique=True)


class PhoneNumbers(Base):
    __tablename__ = 'phone_numbers'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(String(50))
    contacts_id: Mapped[int] = mapped_column(ForeignKey('contacts.id'), nullable=False)
    contact: Mapped["Contact"] = relationship(back_populate="phone_numbers")

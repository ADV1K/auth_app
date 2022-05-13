from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    organisation_id = Column(Integer, ForeignKey("organisations.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    organisation_id = Column(Integer, ForeignKey("organisations.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class Organisation(Base):
    __tablename__ = "organisations"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

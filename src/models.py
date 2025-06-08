from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Date, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from typing import List 

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    username: Mapped[str] = mapped_column (String(10), unique=True, nullable=False)
    photo_url: Mapped[str] = mapped_column (String(), unique=True, nullable=True)
    first_name: Mapped [str] = mapped_column (String(20), nullable=False)
    las_name: Mapped [str] = mapped_column (String(20), nullable=False)
    date_of_birth: Mapped [date] = mapped_column (Date(), nullable=False)
    reels: Mapped [List["Reels"]] = relationship (back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Reels(db.Model):
    id: Mapped [int] = mapped_column (primary_key=True)
    video_url: Mapped[str] = mapped_column (String(), unique=True, nullable=False)
    created_by: Mapped[int] = mapped_column (ForeignKey("user.id"))
    date_of_creation: Mapped [date] = mapped_column (Date(), nullable=False)

post_likes = Table(
    "post_likes",
    db.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("user_id", ForeignKey("user.id")),
)

class Post (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    photo_url: Mapped[str] = mapped_column (String(), unique=True, nullable=True)
    created_by: Mapped[int] = mapped_column (ForeignKey("user.id"))
    date_of_creation: Mapped [date] = mapped_column (Date(), nullable=False)
    description: Mapped [str] = mapped_column (String(), nullable=False)
    likes= relationship("User",secondary=post_likes)

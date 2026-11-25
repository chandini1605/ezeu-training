from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from tool_library.database import Base

from datetime import datetime
from sqlalchemy import ForeignKey, DateTime

class Tool(Base):
    __tablename__ = "tools"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class Checkout(Base):
    __tablename__ = "checkouts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    tool_id: Mapped[int] = mapped_column(
        ForeignKey("tools.id"),
        nullable=False
    )

    borrower_name: Mapped[str] = mapped_column(String(100), nullable=False)

    borrowed_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    returned_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )
from datetime import datetime
from sqlalchemy.orm import Mapped
from .. import Base


class Coding(Base):
    __tablename__ = "codings"
    
    hours: Mapped[int]
    date: Mapped[datetime]
    description: Mapped[str]
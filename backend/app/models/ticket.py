from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(150))
    query = Column(Text)
    status = Column(String(50), default="Open")
    created_at = Column(DateTime, default=datetime.utcnow)
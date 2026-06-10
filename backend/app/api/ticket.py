from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate

router = APIRouter(prefix="/tickets", tags=["Tickets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_ticket(data: TicketCreate, db: Session = Depends(get_db)):
    ticket = Ticket(
        name=data.name,
        email=data.email,
        query=data.query
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return {
        "message": "Ticket created successfully",
        "ticket_id": ticket.id
    }

@router.get("/")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()
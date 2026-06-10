from pydantic import BaseModel


class TicketCreate(BaseModel):
    name: str
    email: str
    query: str
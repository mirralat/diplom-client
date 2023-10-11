import uuid

from sqlalchemy import Column, String, INT
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Node(Base):
    __tablename__ = 'nodes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ip = Column(String, nullable=False)

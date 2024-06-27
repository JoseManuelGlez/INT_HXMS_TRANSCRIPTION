import os
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from sqlalchemy import Column, String
from infrastructure.adapters.data_sources.db_config import Base, db

class TranscriptionEntity(Base):
    __tablename__ = 'transcriptions'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    title = Column(String(100), nullable=False)
    date = Column(String(100), nullable=False)
    teacher = Column(String(100), nullable=False)
    clas = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'title': self.title,
            'date': self.date,
            'teacher': self.teacher,
            'clas': self.clas,
            'description': self.description
        }

Base.metadata.create_all(bind=db.get_bind())
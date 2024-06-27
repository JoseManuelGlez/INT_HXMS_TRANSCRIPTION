import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from domain.models.transcription_model import TranscriptionModel
from domain.repositories.transcription_repository import TranscriptionRepository
from infrastructure.adapters.data_sources.entities.transcription_entity import TranscriptionEntity
from infrastructure.adapters.data_sources.db_config import db
from flask import jsonify

class TranscriptionRepositoryAdapter(TranscriptionRepository):
    def create(self, transcription: TranscriptionModel):
        new_transcription = TranscriptionEntity(title=transcription.title, date=transcription.date, teacher=transcription.teacher, clas=transcription.clas, description=transcription.description)
        db.add(new_transcription)
        db.commit()
        db.refresh(new_transcription)

        transcription_dict = {
            'title': new_transcription.title,
            'date': new_transcription.date,
            'teacher': new_transcription.teacher,
            'clas': new_transcription.clas,
            'description': new_transcription.description
        }
        return jsonify(transcription_dict), 201

    def getAll(self) -> List[TranscriptionModel]:
        transcription_entities = db.query(TranscriptionEntity).all()
        transcription_dicts = [
            {
                'title': entity.title,
                'date': entity.date,
                'teacher': entity.teacher,
                'clas': entity.clas,
                'description': entity.description
            } for entity in transcription_entities
        ]
        return jsonify(transcription_dicts), 201

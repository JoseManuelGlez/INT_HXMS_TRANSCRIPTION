import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from domain.models.transcription_model import TranscriptionModel
from domain.repositories.transcription_repository import TranscriptionRepository

class TranscriptionUseCase:
    def __init__(self, transcription_repository: TranscriptionRepository):
        self.transcription_repository = transcription_repository

    def create(self, transcription: TranscriptionModel) -> TranscriptionModel:
        return self.transcription_repository.create(transcription)

    def getAll(self) -> List[TranscriptionModel]:
        return self.transcription_repository.getAll()
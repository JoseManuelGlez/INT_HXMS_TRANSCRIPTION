import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from abc import ABC, abstractmethod
from domain.models.transcription_model import TranscriptionModel

class TranscriptionRepository(ABC):
    @abstractmethod
    def create(self, transcription: TranscriptionModel) -> TranscriptionModel:
        pass

    @abstractmethod
    def getAll(self) -> TranscriptionModel:
        pass

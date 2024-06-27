import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

sys.path.insert(0, r'C:\Users\12345\Desktop\INT_HXMS_TRANSCRIPTION')

from flask import Flask, request, jsonify
from infrastructure.adapters.transcription_repository_adapter import TranscriptionRepositoryAdapter
from domain.models.transcription_model import TranscriptionModel
from domain.uses_cases.transcription_use_case import TranscriptionUseCase
import datetime

app = Flask(__name__)

transcription_repository = TranscriptionRepositoryAdapter()
transcription_use_case = TranscriptionUseCase(transcription_repository)

class ApiRest:
    @app.route('/transcription', methods=['POST'])
    def create_transcription():
        data = request.get_json()
        transcription = TranscriptionModel(title=data['title'], teacher=data['teacher'], clas=data['class'], description=data['description'])
        return transcription_use_case.create(transcription)

    @app.route('/transcription', methods=['GET'])
    def get_all_transcriptions():
        return transcription_use_case.getAll()

def start_api():
    app.run(host='0.0.0.0', port=3001, debug=True)

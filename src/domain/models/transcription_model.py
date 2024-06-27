import datetime as datetime

class TranscriptionModel:
    def __init__(self, title, teacher, clas, description):
        self.title = title
        self.date = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        self.teacher = teacher
        self.clas = clas
        self.description = description

    def to_dict(self):
        return {
            'title': self.title,
            'date': self.date,
            'teacher': self.teacher,
            'clas': self.clas,
            'description': self.description
        }
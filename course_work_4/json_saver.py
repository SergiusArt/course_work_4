from Abstract import JobSaver
from vacantions import Vacantions
import json


class json_save(JobSaver):

    def __init__(self, name):
        self.name = name

    def _reading(self):
        try:
            with open(self.name, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except Exception(FileNotFoundError):
            data = []

        return data
    def _writing(self, data):
        with open(self.name, 'w', encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def find_vacation(self, key):
        data = self._reading()
        vacantions_list = []

        for vacantion in data:
            for item in vacantion.values():
                if any(isinstance(item, str) and key.lower() in item.lower() for keylist in key):
                    vacantions_list.append(vacantion)
                    break
        return vacantions_list

    def add_vacation(self, job):
        data = self._reading()
        data.append(job.to_dict())

        self._writing(data)

    def del_vacation(self, job):
        data = self._reading()
        vacantions_list = []

        for vacantion in data:
            if vacantion != job:
                vacantions_list.append(vacantion)

        self._writing(vacantions_list)


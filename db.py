import json
from abc import ABC, abstractmethod


class Db(ABC):
    @abstractmethod
    def get_db(self):
        pass


class JsonDb(Db):
    def __init__(self):
        self.db_path = "db.json"

    def get_db(self):
        content = open(self.db_path, encoding="utf-8").read()
        return json.loads(content)

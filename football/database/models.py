import datetime

from pydantic import BaseModel

from .settings import database


class BaseMongoModel(BaseModel):

    def __init__(self, *args, **kwargs):
        self.__collection.insert_one(kwargs)
        super().__init__(*args, **kwargs)

    @property
    def __database(self):
        return database

    @property
    def __collection(self):
        return self.__database[self.Meta.collection_name]


class League(BaseMongoModel):
    name: str

    class Meta:
        collection_name = 'league'

class Club(BaseMongoModel):
    name: str
    statistic_year: int

    class Meta:
        collection_name = 'club'


class Player(BaseMongoModel):
    first_name: str
    last_name: str
    club: Club
    position: str
    date_of_birth: datetime.date

    class Meta:
        collection_name = 'player'


class Match(BaseMongoModel):
    home_team: Club
    guest_team: Club
    home_goals: int
    guest_goals: int
    result: str
    league: League

    class Meta:
        collection_name = 'match'

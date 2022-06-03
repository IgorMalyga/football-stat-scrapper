import pymongo

CONNECTION_STRING = "mongodb://root:root@localhost"
DATABASE_NAME = "football_stats"

connection = pymongo.MongoClient(CONNECTION_STRING)
database = connection["football_stats"]

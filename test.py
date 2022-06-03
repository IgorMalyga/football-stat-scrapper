import pymongo

CONNECTION_STRING = "mongodb://root:root@localhost"

client = pymongo.MongoClient(CONNECTION_STRING)


def create_database():
    db = client["mydatabase"]
    collection = db["player"]
    collection.insert_one({'name': 'Leo'})


def show_databases():
    print(client.list_database_names())

if __name__ == '__main__':
    create_database()
    show_databases()
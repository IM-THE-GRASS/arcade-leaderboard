import reflex as rx
import pymongo
import os
import dotenv
dotenv.load_dotenv()

print(os.environ.get("mongoDB"))
dbclient = pymongo.MongoClient(os.environ.get("mongoDB"))
db= dbclient["arcade-leaderboard"]

class State(rx.State):
    def prints(to_print, thing2=None):
        print("1", to_print)
        print("2", thing2)
    
    
    def get_people():
        people = db["people"]
        result = {}
        for x in people.find():
            x.pop('_id')
            keys = list(x.keys())
            x = x[keys[0]]
            print(type(x))
            print( "x", x)
            result[keys[0]] = x
        return result
    people:dict[str, dict[str, str]] = get_people()
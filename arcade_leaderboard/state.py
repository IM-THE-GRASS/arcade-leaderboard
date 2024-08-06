import reflex as rx
import pymongo
import os
import dotenv
import requests
from bs4 import BeautifulSoup
import json
import datetime
from cryptography.fernet import Fernet

dotenv.load_dotenv()
dbclient = pymongo.MongoClient(os.environ.get("mongoDB"))
db= dbclient["arcade-leaderboard"]
people = db["people"]
class State(rx.State):
    peopledict:dict[str, dict[str, str]]
    reg_pfp:str
    reg_error:str
    reg_username:str
    reg_url:str
    register_button_disabled:bool = True
    
    
    
    
    def decrypt(to_decode:str):
        key = os.environ.get("key")
        f = Fernet(key)
        return f.decrypt(
            to_decode
        ).decode()
    def encrypt(to_encrypt:str):
        key = os.environ.get("key")
        f = Fernet(key)
        return f.encrypt(
                bytes(
                    to_encrypt,
                    "utf-8"
                )
            ).decode()
    def check_reg_valid(self):
        def decrypt(to_decode:str):
            key = os.environ.get("key")
            f = Fernet(key)
            return f.decrypt(
                to_decode
            ).decode()
        
        
        if not self.get_balance(self.strip_url(self.reg_url)):
            self.reg_error = "Your shop URL is invalid. It should be in the format https://hackclub.com/arcade/XXXXXXXXXXXXXXXXX/shop/"
            return False
        
        if self.reg_username != "":
            
            for person in people.find():
                person.pop('_id')
                person["shop_token"] = decrypt(person["shop_token"])
                person_name = person["username"]
                person_name = person_name.lower().replace(" ", "")
                regname = self.reg_username
                regname = regname.lower().replace(" ", "")
                person_url = person["shop_token"]
                regurl = self.strip_url(self.reg_url)
                if person_name == regname or regurl == person_url:
                    self.reg_error = "This user already exists!"
                    return False
            return True
        else:
            self.reg_error = "Invalid username"
            return False
    
    def register(self):
        def encrypt(to_encrypt:str):
            key = os.environ.get("key")
            f = Fernet(key)
            return f.encrypt(
                bytes(
                    to_encrypt,
                    "utf-8"
                )
            ).decode()
        username = self.reg_username
        shop_token = self.strip_url(self.reg_url)
        tickets = self.get_balance(shop_token, True)
        username = username.replace(" ", "")
        pfp = self.reg_pfp
        if self.check_reg_valid():
            people.insert_one(
                {
                    "pfp":pfp,
                    "shop_token":encrypt(shop_token),
                    "username":username,
                    "tickets": str(tickets),
                }
            )
            self.peopledict = self.get_people()
        else:
            return rx.toast("Something went wrong... Please try again!")
            
    
    def set_reg_pfp(self, new:str):
        self.reg_pfp = new
    
    def set_reg_username(self, new:str):
        self.reg_username = new
        self.register_button_disabled = not self.check_reg_valid()
    def set_reg_url(self, new:str):
        
        self.reg_url = new
        self.register_button_disabled = not self.check_reg_valid()
    
    
    
    
    def strip_url(self, input_url:str):
        input_url = input_url.replace(" ", '')
        input_url = input_url.replace("https:", '')
        input_url = input_url.replace("http:", '')
        input_url = input_url.replace("shop", '')
        input_url = input_url.replace("hackclub.com/arcade", '')
        input_url = input_url.replace("/", '')
        return input_url
    def get_balance(self, id:str, _int = False):
        try:
            response = requests.get(f"https://hackclub.com/arcade/" + id + "/shop/")
            soup = BeautifulSoup(response.text, 'html.parser')
            balance_span = soup.find('span', class_='gaegu css-3ha5y3')
            balance_text = balance_span.text
            balance_text = balance_text.replace("Your current balance is ", "")
            balance_text = balance_text.replace(" 🎟️", "")
            if not _int:
                balance_text = str(balance_text)
            else:
                balance_text = int(balance_text)
            return balance_text
        except:
            if not _int:
                
                return ""
            else:
                return 0
    
    
    
    def get_people(self = None):
        def decrypt(to_decode:str):
            key = os.environ.get("key")
            f = Fernet(key)
            return f.decrypt(
                to_decode
            ).decode()
        result = {}
        for x in people.find().sort("tickets", -1):
            x.pop('_id')
            x["shop_token"] = decrypt(x["shop_token"])
            result[x["username"]] = x
        return result
    def update_ticket_counts(self):
        def decrypt(to_decode:str):
            key = os.environ.get("key")
            f = Fernet(key)
            return f.decrypt(
                to_decode
            ).decode()
        
        for person in people.find():
            person.pop('_id')
            person["shop_token"] = decrypt(person["shop_token"])
            tickets = self.get_balance(person["shop_token"])
            print(person["username"], tickets)
            if tickets:
                
                name = person["username"]
                result = people.update_one(
                    {"username": name},
                    { "$set": { "tickets": tickets, "updated": datetime.datetime.now().strftime("%X")} },
                    upsert=True    
                )
                print(result.modified_count)
    def update_people(self):
        
        self.update_ticket_counts()
        self.peopledict = self.get_people()
        print(self.peopledict, "PEOPLEDICT")
    peopledict = get_people()
    
    
    
    top:list[int] = [1,2,3]
    top_anims:dict[int, str]={
        1 : "https://lottie.host/b3f43394-a351-4755-9c03-5c61100951e4/kHb0G7NsSI.lottie",
        2 : "https://lottie.host/16454969-d7cf-4a51-a424-15ca9ed978d8/k9z0CUDBsM.json", 
        3 : "https://lottie.host/2cbd6b2a-14a3-4a42-82e7-ceb07bf5ee59/k4lO4T6lHT.json"
    
    }
        
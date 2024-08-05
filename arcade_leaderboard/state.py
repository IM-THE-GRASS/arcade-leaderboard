import reflex as rx
import pymongo
import os
import dotenv
import requests
from bs4 import BeautifulSoup
import json
dotenv.load_dotenv()

print(os.environ.get("mongoDB"))
dbclient = pymongo.MongoClient(os.environ.get("mongoDB"))
db= dbclient["arcade-leaderboard"]

class State(rx.State):
    
    
    
    reg_password:str
    reg_username:str
    reg_url:str
    register_button_disabled:bool = False
    
    def check_reg_valid(self):
        if self.get_balance(self.strip_url(self.reg_url)) and self.reg_password != "" and self.reg_username != "":
            print("yes!")
            return True
        else:
            print("no :(")
            return False
    
    
    def set_reg_username(self, new:str):
        self.reg_username = new
        self.register_button_disabled = not self.check_reg_valid()
    def set_reg_url(self, new:str):
        
        self.reg_url = new
        self.register_button_disabled = not self.check_reg_valid()
    
    def set_reg_password(self, new:str):
        self.reg_password = new
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
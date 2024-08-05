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
people = db["people"]
class State(rx.State):
    
    
    reg_error:str
    reg_password:str
    reg_username:str
    reg_url:str
    register_button_disabled:bool = True
    
    def check_reg_valid(self):
        if not self.get_balance(self.strip_url(self.reg_url)):
            self.reg_error = "Your shop URL is invalid. It should be in the format https://hackclub.com/arcade/XXXXXXXXXXXXXXXXX/shop/"
            return False
        
        if self.reg_password != "" and self.reg_username != "":
            
            for person in people.find():
                person.pop('_id')
                keys = list(person.keys())
                person = person[keys[0]]
                person_name = person["username"]
                person_name = person_name.lower().replace(" ", "")
                regname = self.reg_username
                regname = regname.lower().replace(" ", "")
                person_url = person["shop_token"]
                regurl = self.strip_url(self.reg_url)
                print(person_url, regurl)
                if person_name == regname or regurl == person_url:
                    self.reg_error = "This user already exists!"
                    #return False
            return True
        else:
            self.reg_error = "Invalid username or password"
            return False
    
    def register(self):
        username = self.reg_username
        shop_token = self.strip_url(self.reg_url)
        tickets = self.get_balance(shop_token, True)
        
        password = self.reg_password
        if self.check_reg_valid():
            people.insert_one(
                {
                    username:{
                        "pfp":"",
                        "shop_token":shop_token,
                        "username":username,
                        "tickets": str(tickets),
                        "password": password
                    }
                }
            )
            
    
    
    
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
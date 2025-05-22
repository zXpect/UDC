from pymongo import MongoClient  
from config import Config  
import datetime  
from bson import ObjectId  
import bcrypt  
  
client = MongoClient(Config.MONGODB_URI)  
db = client.udc_netschool  
  
class Event:  
    collection = db.events  
      
    @staticmethod  
    def create(title, date, time, location, description):  
        event = {  
            'title': title,  
            'date': date,  
            'time': time,  
            'location': location,  
            'description': description,  
            'created_at': datetime.datetime.utcnow()  
        }  
        result = Event.collection.insert_one(event)  
        return result.inserted_id  
      
    @staticmethod  
    def find_all():  
        return list(Event.collection.find().sort('date', 1))  
      
    @staticmethod  
    def find_by_id(event_id):  
        try:  
            return Event.collection.find_one({'_id': ObjectId(event_id)})  
        except:  
            return None  
      
    @staticmethod  
    def update(event_id, title, date, time, location, description):  
        try:  
            result = Event.collection.update_one(  
                {'_id': ObjectId(event_id)},  
                {'$set': {  
                    'title': title,  
                    'date': date,  
                    'time': time,  
                    'location': location,  
                    'description': description,  
                    'updated_at': datetime.datetime.utcnow()  
                }}  
            )  
            return result.modified_count > 0  
        except:  
            return False  
      
    @staticmethod  
    def delete(event_id):  
        try:  
            result = Event.collection.delete_one({'_id': ObjectId(event_id)})  
            return result.deleted_count > 0  
        except:  
            return False  
  
class User:  
    collection = db.users  
      
    @staticmethod  
    def find_by_username(username):  
        return User.collection.find_one({'username': username})  
      
    @staticmethod  
    def create_user(username, password, role):  
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())  
        user = {  
            'username': username,  
            'password': hashed_password,  
            'role': role,  
            'created_at': datetime.datetime.utcnow()  
        }  
        return User.collection.insert_one(user)  
      
    @staticmethod  
    def verify_password(username, password):  
        user = User.find_by_username(username)  
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):  
            return user  
        return None
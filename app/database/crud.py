from deta import Deta
import os
from dotenv import load_dotenv
import uuid

# Load environment variables
load_dotenv()

PROJECT_KEY = os.getenv("PROJECT_KEY")

deta = Deta(PROJECT_KEY)
db = deta.Base("shops")

def get_shops():
  try:
    response = db.fetch()
    return response.items

  except Exception as e:
    print(f"An error occurred: {e}")
    return None

def get_shop(shop_id):
    try:
        # Check if shop exists in database
        if not db.fetch({"id": shop_id}).items:
            return {"error": "Shop with given ID does not exist."}
        
        response = db.fetch({"id": shop_id})
        return response.items[0] if response.items else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_shop(shop):
    shop.id = str(uuid.uuid4())
    try:
        return db.put(shop.dict())
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def update_shop(shop_id, shop):
    try:
        # Check if shop exists in database
        if not db.fetch({"id": shop_id}).items:
            return {"error": "Shop with given ID does not exist."}
        
        # Fetch shop to get key
        shop_ = db.fetch({"id": shop_id}).items[0]  
        key = shop_["key"]

        # Update only selected fields
        shop_.update(shop.dict(exclude_unset=True))

        # Update shop
        return db.put(shop_, key)
    

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    

def delete_shop(shop_id):
    try:
        # Check if shop exists in database
        if not db.fetch({"id": shop_id}).items:
            return {"error": "Shop with given ID does not exist."}
        
        # Fetch shop first to get key
        shop = db.fetch({"id": shop_id}).items[0]
        key = shop["key"]
        db.delete(key)
        return {"id": shop_id}
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
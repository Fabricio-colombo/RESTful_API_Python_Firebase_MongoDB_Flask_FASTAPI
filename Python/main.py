from pymongo import MongoClient



def connect_mongodb():
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "Books"
    COLLECTION_NAME = "Non-Fiction"

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    new_document = {
    "title": "New Book",
    "author": "John Doe",
    "year": 2022,
    "pages": 300,
    "language": "English",
    "rating": 4.5
}

    insert_result = collection.insert_one(new_document)
    print("Inserted document ID:", insert_result.inserted_id)
    
    
    
    
    









    
if __name__ == "__main__":
    connect_mongodb()    
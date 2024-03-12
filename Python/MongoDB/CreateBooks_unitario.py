# MongoDB Non-Fiction
from pymongo import MongoClient

def create_books(title, author, year, pages, language, rating):
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "Books"
    COLLECTION_NAME = "Non-Fiction"

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    new_document = {
    "title": title,
    "author": author,
    "year": year,
    "pages": pages,
    "language": language,
    "rating": rating
}
    insert_result = collection.insert_one(new_document)
    print("Inserted document ID:", insert_result.inserted_id)
    

create_books(title='hehehe',
            author='rodrigo',
            year=2000, 
            pages=44,
            language='en',
            rating=0)
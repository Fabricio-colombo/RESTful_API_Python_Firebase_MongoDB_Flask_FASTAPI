from MongoDB.connect_mongo import connect_mongodb

def main():
    collection = connect_mongodb()
    if collection:
        new_document = {"title": "New Book", "author": "John Doe", "year": 2022}
        insert_result = collection.insert_one(new_document)
        print("Inserted document ID:", insert_result.inserted_id)
    else:
        print("Erro ao conectar ao MongoDB")

if __name__ == "__main__":
    main()
    
    
    
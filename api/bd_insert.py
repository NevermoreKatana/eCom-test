from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['forms_db']
collection = db['forms']

test_templates = [
    {
        "name": "MyForm",
        "user_name": "text",
        "order_date": "date",
        "lead_email": "email"
    },
    {
        "name": "OrderForm",
        "user_name": "text",
        "order_date": "date",
        "phone_number": "phone"
    }
]

collection.insert_many(test_templates)

print("Тестовые данные успешно добавлены в базу данных.")

import dataset

db = dataset.connect('sqlite:///myDB.db')

pet_table = db["pet"]
data  = pet_table.find()
data1 = [dict(item) for item in data]
print(data1)


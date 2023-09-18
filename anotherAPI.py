import dataset

db = dataset.connect('sqlite:///myDB.db')

pet_table = db["pet"]
data  = pet_table.find()

print(data)


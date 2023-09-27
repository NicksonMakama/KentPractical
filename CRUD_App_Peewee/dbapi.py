import dataset

con = dataset.connect('sqlite:///myDb.db')

def getData(id = None):
    
    if id==None:
        getData = [dict(anItem) for anItem in con["toy"].find()]
    else:
        getData = [dict(anItem) for anItem in con["toy"].find(id=id)]

    toSend = [dict(eachData) for eachData in getData]

    return toSend

def addData(aToyName, owner):
    toyTableItem = con['toy']
    toyTableItem.insert({"toyName":aToyName, "owner":owner})
    

def updateData(id, aToyName, owner):
    toyTableItem = con['toy']
    toyTableItem.update({
        "id":id,
        "toyName":aToyName,
        "owner":owner
    },['id'])
    

def deleteItem(id):
    toyTableItem = con['toy']
    toyTableItem.delete(id=id)

def setup_database():
    
    try:
        con["toy"].drop()
    except:
        pass

    toyTableItem = con["toy"]
    for item in ['Bob','Princess', 'dog']:
        toyTableItem.insert({"toyName":item, "owner":item})

def testSetupDatabase():
    print("Testing ... setupDB")
    setup_database()
    
    itemData = [dict(anItem) for anItem in  con["toy"].find()]

    assert len(itemData) == 3
    toyNames = [item['toyName'] for item in itemData]

    for anitem in ['Bob', 'Princess','dog']:
        assert anitem in toyNames

def testgetData():
    print("testing... getdata")
    setup_database()
    itemData = getData()
    assert type(itemData) is list
    assert len(itemData) > 0
    for eachItem in itemData:
        assert type(eachItem) is dict
        assert 'id' in eachItem
        assert type(eachItem['id']) is int
        assert 'toyName' in eachItem
        assert type(eachItem['toyName']) is str
    
    id = itemData[0]['id']
    toyName = itemData[0]['toyName']

    testData = getData(id)
    assert type(testData) is list
    assert len(testData) == 1
    assert testData[0]['id'] == id
    assert testData[0]['toyName'] == toyName

def testaddData():
    print("Testing... Add data")
    setup_database()
    itemData = getData()
    original_len = len(itemData)
    addData("Unknown Toy","Nickson")
    itemData = getData()
    assert len(itemData) == original_len + 1
    toyNames = [anItemData['toyName'] for anItemData in itemData]
    assert "Unknown Toy" in toyNames
    

def testUpdateItem():
    print("Testing ... UpdateDate")
    setup_database()
    itemData = getData()
    id = itemData[2]['id']

    updateData(id,"Everything","Alll")
    itemData = getData()
    
    assert itemData[2]['toyName'] == "Everything"
    assert itemData[2]['owner'] == "Alll"


def testDeleteItem():
    print("Testing... deleteItem")
    setup_database()
    addData("Fortest","Paul")
    itemData = getData()
    for item2Delete in itemData:
        if item2Delete['toyName'] == 'Fortest':
            deleteItem(item2Delete['id'])

    itemData = getData()
    for deletedItem in itemData:
        assert deletedItem['toyName'] != 'Fortest' 

if __name__ == "__main__":
    testSetupDatabase()
    testgetData()
    testaddData()
    testUpdateItem()
    testDeleteItem()

    print('Everything... works')



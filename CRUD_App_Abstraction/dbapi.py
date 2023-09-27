import sqlite3

con = sqlite3.connect("myDb.db")

def getData(id = None):
    cursor = con.cursor()

    if id==None:
        getData = cursor.execute("select id, toyName, owner from toy")
    else:
        getData = cursor.execute(f"select id, toyName, owner from toy where id == {id}")

    theData = list(getData)

    toSend = [{'id':eachData[0], 'toyName':eachData[1], 'owner':eachData[2]} for eachData in theData]

    #iteratorList = [item[0] for item in list(getData.description)]
    #toSend = [dict(zip(iteratorList,item)) for item in theData ]

    return toSend

def addData(aToyName, owner):
    cursor = con.cursor()
    cursor.execute(f"insert into toy(toyName, owner) values('{aToyName}','{owner}')")
    con.commit()

def updateData(id, aToyName, owner):
    cursor = con.cursor()
    upDateStm = f"update toy set toyName='{aToyName}', owner = '{owner}' where id={id}"
    cursor.execute(upDateStm)
    con.commit()

def deleteItem(id):
    cursor = con.cursor()
    delStm = f"delete from toy where id={id}"
    cursor.execute(delStm)
    con.commit()

def setup_database():
    cursor = con.cursor()

    try:
        cursor.execute("drop table toy")
    except:
        pass
    
    cursor.execute("create table toy(id integer primary key, toyName text, owner text)")
    for item in ['Bob','Princess', 'dog']:
        cursor.execute(f"insert into toy(toyName, owner) values('{item}', 'No body')")

    con.commit()

def testSetupDatabase():
    print("Testing ... setupDB")
    setup_database()
    itemData = getData()

    assert len(itemData) == 3
    toyNames = [item['toyName'] for item in itemData]

    for anitem in ['Bob', 'Princess','dog']:
        assert anitem in toyNames

def testgetData():
    print("testing... getdata")
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
    print("Testing... Adddata")
    setup_database()
    itemData = getData()
    original_len = len(itemData)
    addData("Unknown Toy")
    itemData = getData()
    assert len(itemData) == original_len + 1
    toyNames = [anItemData['toyName'] for anItemData in itemData]
    assert "Unknown Toy" in toyNames

def testUpdateItem():
    print("Testing ... UpdateDate")
    setup_database()
    itemData = getData()
    id = itemData[2]['id']
    toyName = itemData[2]['toyName']
    updateData(id,"Everything")
    itemData = getData()
    assert itemData[2]['toyName'] == "Everything"

def testDeleteItem():
    print("Testing... deleteItem")
    setup_database()
    addData("Fortest")
    itemData = getData()
    for item2Delete in itemData:
        if item2Delete['toyName'] == 'Fortest':
            deleteItem(item2Delete['id'])


if __name__ == "__main__":
    testSetupDatabase()
    testgetData()
    testaddData()
    testUpdateItem()
    testDeleteItem()

    print('Everything... works')



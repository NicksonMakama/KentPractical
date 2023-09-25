import sqlite3

con = sqlite3.connect("myDB.db")

def getData(id = None):
    cursor = con.cursor()

    if id==None:
        getData = cursor.execute("select id, toyName, owner from toy")
    else:
        getData = cursor.execute(f"select id, toyName, owner from toy where id == {id}")

    theData = list(getData)

    toSend = [{'id':eachData[0], 'toyName':eachData[1]} for eachData in theData]

    #iteratorList = [item[0] for item in list(getData.description)]
    #toSend = [dict(zip(iteratorList,item)) for item in theData ]

    return toSend

def addData(aToyName):
    cursor = con.cursor()
    cursor.execute(f"insert into toy(toyName) values('{aToyName}')")
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



if __name__ == "__main__":
    testSetupDatabase()
    testgetData()
    testaddData()

    print('Everything... works')



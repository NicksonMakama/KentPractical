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

def testGetItems():
    print("testing... getItems")
    

if __name__ == "__main__":
    testSetupDatabase()
    testGetItems()



from bottle import route, run, template, post, request, redirect

import sqlite3

con = sqlite3.connect('myDB.db')

@route('/')
def index1():
    return "Hi.."



myPets = [{'id':1, 'name':"Paul", 'age':3},         
          {'id':2, 'name':"Rose", 'age':6},
          {'id':1, 'name':"Mary", 'age':33}
          ]


@route('/hello/<usernam>')
def toHello(usernam):
    
    cursor = con.cursor()
    getData = cursor.execute("select * from pet")

    theData = getData.fetchall()

    iteratorList = [item[0] for item in list(getData.description)]
    toSend = [dict(zip(iteratorList,item)) for item in theData ]

    return template("hello.tpl", usernamee = usernam, petGo=myPets, fromDatabase = toSend)

@route("/delete/<id>")
def get_delete(id):
    cursor = con.cursor()
    getDelete = cursor.execute(f"delete from pet where id == {id}")
    con.commit()
    redirect("/hello/nick")

@route("/insert")
def to_insertPage():
    return template("addPage.tpl")


@post("/addQuery")
def addData():
    theID  = request.forms.get("personID")
    theName  = request.forms.get("personName")
    theKind  = request.forms.get("personKind")
    cursor = con.cursor()
    cursor.execute(f"insert into pet(id,fname,kind) values('{theID}','{theName}','{theKind}')")

    con.commit()
    redirect("/hello/nick")

@route("/update/<id>")
def to_updatePage(id):
    cursor = con.cursor()
    getUpdate = cursor.execute(f"select id, fname, kind from pet where id = {id}")
    
    thedataList = list(getUpdate) #turn it into list, now lets check if anytin inside else redirect to home
    if len(thedataList) != 1:
        redirect("/hello/nick")
    
    fromUpdata = [{'petId': row[0], 'fname':row[1], 'kind': row[2]} for row in thedataList]

    aName = fromUpdata[0]['fname']
    aKind = fromUpdata[0]['kind']
  
    return template("updatePage.tpl", theId = id, theName = aName, theKind=aKind)

@post("/updateQuery")
def updateData():
    theId = request.forms.get("personID")
    thePerson = request.forms.get("personName")
    theKind = request.forms.get("personKind")

    cursor = con.cursor()

    cursor.execute(f"update pet set id='{theId}', fname='{thePerson}', kind='{theKind}' where id={theId}")
    con.commit()
    redirect("/hello/nick")

run(host='localhost', port=8080)
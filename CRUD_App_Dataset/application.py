from bottle import route, run, template, post, request, redirect

import dbapi

@route('/')
def index1():
    redirect('/hello/nick')

@route('/hello/<usernam>')
def toHello(usernam):
    toSend =    dbapi.getData() 
    return template("hello.tpl", fromDatabase = toSend)

@route("/delete/<id>")
def get_delete(id):
    dbapi.deleteItem(id)
    redirect("/hello/nick")

@route("/insert")
def to_insertPage():
    return template("addPage.tpl")


@post("/addQuery")
def addData():
    
    theToyName  = request.forms.get("toyName")
    theOwner  = request.forms.get("toyOwner")

    dbapi.addData(theToyName,theOwner)

    redirect("/hello/nick")

@route("/update/<id>")
def to_updatePage(id):
    toSend = dbapi.getData(id)
  
    return template("updatePage.tpl", fromDatabase = toSend[0])

@post("/updateQuery")
def updateData():
    theToyId = request.forms.get("toyId")
    theToyName = request.forms.get("toyName")
    theOwner = request.forms.get("toyOwner")

    dbapi.updateData(theToyId, theToyName, theOwner)
    redirect("/hello/nick")

run(host='localhost', port=8080)
from bottle import route, run, template

import sqlite3

@route('/')
def index1():
    return "Hi.."



myPets = [{'id':1, 'name':"Paul", 'age':3},         
          {'id':2, 'name':"Rose", 'age':6},
          {'id':1, 'name':"Mary", 'age':33}
          ]


@route('/hello/<usernam>')
def toHello(usernam):
    con = sqlite3.connect('myDB.db')
    cursor = con.cursor()
    getData = cursor.execute("select * from pet")

    theData = getData.fetchall()

    iteratorList = [item[0] for item in list(getData.description)]
    toSend = [dict(zip(iteratorList,item)) for item in theData ]

    return template("hello.tpl", usernamee = usernam, petGo=myPets, fromDatabase = toSend)

run(host='localhost', port=8080)
from bottle import route, run, template



@route('/')
def index1():
    return "Hi.."



myPets = [{'id':1, 'name':"Paul", 'age':3},         
          {'id':2, 'name':"Rose", 'age':6},
          {'id':1, 'name':"Mary", 'age':33}
          ]


@route('/hello/<usernam>')
def toHello(usernam):
    return template("hello.tpl", usernamee = usernam, petGo = myPets)



run(host='localhost', port=8080)

import simplejson
from bottle import route, view, run, template, get, post, request, static_file

global db
db={0:{'name': 'hanako',
 'nickname': 'hnk',
 'faculty': 'bunka1',
 'lang': 'chinese',
 'place_of_birth': 'tokyo',
 'highschool': 'oin',
 'station': 'nagatatyo',
 'hobby': 'shumi',
 'like': 'like',
 'club': 'club',
 'life': 'life'},
1:{'name': 'hanako',
 'nickname': 'hnk',
 'faculty': 'bunka1',
 'lang': 'chinese',
 'place_of_birth': 'tokyo',
 'highschool': 'oin',
 'station': 'nagatatyo',
 'hobby': 'shumi',
 'like': 'like',
 'club': 'club',
 'life': 'life'},
2:{'name': 'hanako',
 'nickname': 'hnk',
 'faculty': 'bunka2',
 'lang': 'chinese',
 'place_of_birth': 'tokyo',
 'highschool': 'oin',
 'station': 'nagatatyo',
 'hobby': 'shumi',
 'like': 'like',
 'club': 'club',
 'life': 'life'}}


def compare(x,y):
    pcls=1 if x["faculty"]==y["faculty"] else 0
    plng=1 if x["lang"]==y["lang"] else 0
    ppob=1 if x["place_of_birth"]==y["place_of_birth"] else 0
    phs=1 if x["highschool"]==y["highschool"] else 0
    pst=1 if x["station"]==y["station"] else 0
    return pcls+plng+ppob+phs+pst

    
@route('/recommend', method='GET')
def recommend():
   user_id = simplejson.loads(request.params['json'])['user']
   user_data = db[user_id]

   res =[]
   for i in db:
       data = db[i]
       p=compare(user_data,data)
       res.append(p)
   ids=[_id for _id in map(lambda tp:tp[0],sorted(zip(db.keys(),res),key=lambda tp:-tp[1]))
        if _id != user_id][:3]
   
   return simplejson.dumps([ db[i] for i in ids ])

if __name__ == '__main__':
   run(host='0.0.0.0', port=8888, debug=False, reloader=False)


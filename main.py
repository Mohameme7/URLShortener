import random
import sqlite3, flask
import string
#from flask_cors import CORS
from flask import request, redirect
import validators
app = flask.Flask(__name__, template_folder="templates", static_folder='static_files')
app.secret_key = "eererea"
#CORS(app)
connection = sqlite3.connect('database.db', check_same_thread=False)
c = connection.cursor()
def randomword():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6,6)))
@app.route('/create', methods = ['POST'])
def createcode():
    try:

        urlredirectedto = request.get_json()['url']
        if not urlredirectedto.startswith('https://'):
            urlredirectedto = f"https://{urlredirectedto}"

        if not bool(validators.url(urlredirectedto)):
            return "Bad Url", 400
        elif bool(validators.url(urlredirectedto)):
            code = randomword()
            c.execute('INSERT INTO urls values(?,?);', (code, urlredirectedto))
            connection.commit()
            return {"newurl" : f"http://127.0.0.1:5000/shortened?code={code}"}, 200

    except Exception:

        return "Invalid JSON"
@app.route('/shortened')
def a():

     code = request.args.to_dict().get('code')
     if code is None:
         return "Invalid Request Query", 401
     fetch = c.execute('select * from urls where Code = ?', (code,)).fetchall()
     if len(fetch) == 0:
         return "Code Does not exist.", 404

     return redirect(fetch[0][1], code= 302)

@app.route('/')
def default():
    return flask.render_template('index.html')


app.run(debug=True)
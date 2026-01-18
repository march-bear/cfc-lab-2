from flask import Flask
from redis import Redis
from waitress import serve
from werkzeug.exceptions import NotFound

import traceback


app = Flask(__name__)
db = Redis(
        host='db', 
        port=6379, db=0, 
        decode_responses=True,
        password='password1'
        )


@app.errorhandler(NotFound)
def onNotFound(e):
    return 'Go to <a href="/app">/app</a>'


@app.errorhandler(Exception)
def onException(e):
    app.logger.error(traceback.format_exc())
    return 'Something went wrong'


@app.route('/app')
def hello():
    t = db.pipeline(transaction=True)
    t.incr('counter')
    t.get('counter')
    res = t.execute()
    return f'This page was visited already {res[0]} times'


if __name__ == '__main__':
    db.set('counter', 0)
    serve(app, host='0.0.0.0', port=5000)

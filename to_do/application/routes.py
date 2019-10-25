from flask import current_app as app
from flask import render_template, jsonify

from .hello import HelloApi
from .tasks import TasksApi

#blueprint lives here because flask has been told so
app.register_blueprint(HelloApi, url_prefix='/hello')
app.register_blueprint(TasksApi, url_prefix='/tasks')  #the whole tasks API lives at url /books

# homepage - renders homepage hello.html which is saved in same project

@app.route('/')
def hello():
    return render_template('hello.html')

#app.route and render_template are both flask items

# creating a second web page
@app.route('/tasks')
def tasks_user():
    return render_template('Tasks_welcome.html')


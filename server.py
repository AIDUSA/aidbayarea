from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.admin import Admin
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin.form import rules
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

# MongoDB Config
app.config['MONGODB_DB'] = 'mydb'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

Bootstrap(app)
db = MongoEngine(app)
admin = Admin(app)

class Projects(db.Document):
    name = db.StringField(max_length=255)
    amount = db.StringField(max_length=255)
    year = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    area = db.StringField(max_length=255)
    ngo = db.StringField(max_length=255)
    image_field = db.StringField(max_length=255)

class Events(db.Document):
	name = db.StringField(max_length=255)
	year = db.StringField(max_length=255)
	description = db.StringField(max_length=300)
	area = db.StringField(max_length=255)
	date = db.StringField(max_length=300)
	event_image = db.StringField(max_length = 255)

class Home(db.Document):
	title = db.StringField(max_length=255)
	info = db.StringField(max_length=300)

class ProjectView(ModelView):
	column_filters=['name', 'year']

class EventView(ModelView):
	column_filters=['name']

@app.route('/')
def index():
	my_home = Home.objects()
	return render_template('index.html',v_home = my_home)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/donate')
def donate():
	return render_template('donate.html')

@app.route('/volunteer')
def volunteer():
	return render_template('volunteer.html')

@app.route('/events')
def events():
	my_events = Events.objects()
	return render_template('events.html', my_events=my_events)

@app.route('/projects')
def projects():
	my_projects = Projects.objects()
	return render_template('projects.html', v_projects=my_projects)

@app.route('/faq')
def faq():
	return render_template('faq.html')

@app.route('/projectdetails/<project_id>')
def projectdetails(project_id):
	current_project = Projects.objects(id=project_id)
	all_projects = Projects.objects()
	for c in current_project:
		c_project = c
	return render_template('projectdetails.html', current_project=c_project, all_projects=all_projects)

	# Need to change current_project = and the for loop

if __name__ == '__main__':
	admin.add_view(ProjectView(Projects))
	admin.add_view(EventView(Events))
	path = op.join(op.dirname(__file__), 'static/images')
	admin.add_view(FileAdmin(path, name='Images'))
	app.run(debug=True)

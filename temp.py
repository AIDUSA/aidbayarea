from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine


# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

# MongoDB Config
app.config['MONGODB_DB'] = 'mydb'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

# Create database connection object
db = MongoEngine(app)

class Project(db.Document):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()


{% set variable_foo = "foo" %}

# Create a user to test with
@app.before_first_request
def create_user():
    project=Project()
    project.email = "foobar@foo.com"
    project.save()

    my_projects = Project.objects()
    return render_template('users.html', my_projects=my_projects)

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/projects/<project_id>')
def projectdetails(project_id):
    pass

#this is what you need to do in projects to pass

# <a class="btn btn-primary" href="{{ url_for('projectdetails', project_name={{ my_project.id }}) }}">View Project <i class="fa fa-angle-right"></i></a>

if __name__ == '__main__':
    app.run(debug=True)
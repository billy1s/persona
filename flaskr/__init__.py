import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'mysecretkey'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
app_api = Api(app)

from flaskr.api.utils import checkInboundData

from flaskr.front_end.people.views import persons_blueprint
from flaskr.front_end.admin.views import admin_blueprint
from flaskr.front_end.api_view.views import api_view_blueprint


## FRONTEND
app.register_blueprint(persons_blueprint,url_prefix='/search')
app.register_blueprint(admin_blueprint,url_prefix='/admin')
app.register_blueprint(api_view_blueprint, url_prefix='/view')


from flaskr.api.persons.persona import Person_API, Person_All_API, Person_delete_API

## API points
app_api.add_resource(Person_API, "/api/search/<string:username>")
app_api.add_resource(Person_All_API, "/api/people")
app_api.add_resource(Person_delete_API, "/api/people/<string:username>")




#checkInboundData()
from flask import Blueprint,render_template,redirect,url_for

persons_blueprint = Blueprint('people',
                              __name__,
                              template_folder='templates/people')
from flaskr.api.models import Person


@persons_blueprint.route("/list")
def list():
    people = Person.query.all()
    return render_template('index.html', people = people)
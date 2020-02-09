from flask import Blueprint,render_template,redirect,url_for

from .form import searchForm
from flaskr.api.models import Person
api_view_blueprint = Blueprint('api_view',
                              __name__,
                              template_folder='templates/api_view')


@api_view_blueprint.route("/", methods=['GET', 'POST'])
def index():
    form = searchForm()
    if form.validate_on_submit():
        username = form.username.data
        person = Person.query.filter_by(username=username).first()
        if person:
            form = searchForm()
            return render_template('api_view_search.html', person=person ,form=form)
        else:
            form = searchForm()
            return render_template('api_view_no_match.html', form=form)

    return render_template('api_view_index.html', form = form)







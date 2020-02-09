from flask import Blueprint,render_template,redirect,url_for
from flaskr.api.utils import checkInboundData

admin_blueprint = Blueprint('admin',
                              __name__,
                              template_folder='templates/admin')




@admin_blueprint.route("/")
def index():
    return render_template('index.html')

@admin_blueprint.route("/ingestNewData")
def ingestNewData():

    checkInboundData()

    return render_template('ingestionStarted.html')
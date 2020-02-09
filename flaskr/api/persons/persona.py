from flaskr.api.models import Person
from flaskr import Resource, db
from flask import request


class Person_API(Resource):
    def get(self, username):
        person = Person.query.filter_by(username=username).first()
        if person:
            return person.json()
        else:
            return {'username': 'not found'}, 404

class Person_delete_API(Resource):
    def delete(self,username):
        person = Person.query.filter_by(username=username).first()

        if person:
            db.session.delete(person)
            db.session.commit()
            return {'note': 'delete successful'}
        else:
            return {'username': 'not found'}, 404

class Person_All_API(Resource):
    def get(self):
        page = request.args.get("page")
        items_per_page = request.args.get("items_per_page")

        if page == None:
            page = 1
        else:
            page = int(page)

        if items_per_page == None:
            items_per_page = 20
        else:
            items_per_page = int(items_per_page)

        personsCount = Person.query.count()
        personsPageination = Person.query.paginate(page, items_per_page)

        if personsPageination.has_next:
            next_url = f"/api/people?page={page + 1}&items_per_page={items_per_page}"
        else:
            next_url = "None"

        if personsPageination.has_prev:
            previous_url = f"/api/people?page={page - 1}&items_per_page={items_per_page}"
        else:
            previous_url = "None"

        pageinationDict = {
            "count": personsCount,
            "page": page,
            "next": next_url,
            "previous": previous_url,
            "items_per_page": items_per_page,
            "results": [person.json() for person in personsPageination.items]
        }

        if personsCount > 0:
            return pageinationDict
        else:
            return {'users': 'not found'}, 404




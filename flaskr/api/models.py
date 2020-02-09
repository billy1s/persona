from flaskr import db


class Person(db.Model):
    __tablename__ = "persons"
    job = db.Column(db.String(256))
    company = db.Column(db.String(256))
    ssn = db.Column(db.String(256))
    residence = db.Column(db.Text)
    current_location = db.Column(db.String(10))
    blood_group = db.Column(db.String(3))
    website = db.Column(db.Text)
    username = db.Column(db.String(256), primary_key=True)
    name = db.Column(db.String(256))
    sex = db.Column(db.String(1))
    address = db.Column(db.Text)
    mail = db.Column(db.String(256))
    birthdate = db.Column(db.String(10))

    def __init__(self, dictValues):
        self.job = dictValues["job"]
        self.company = dictValues["company"]
        self.ssn = dictValues["ssn"]
        self.residence = dictValues["residence"]
        self.current_location = str(dictValues["current_location"])
        self.blood_group = dictValues["blood_group"]
        self.website = str(dictValues["website"])
        self.username = dictValues["username"]
        self.name = dictValues["name"]
        self.sex = dictValues["sex"]
        self.address = dictValues["address"]
        self.mail = dictValues["mail"]
        self.birthdate = dictValues["birthdate"]

    def json(self):
        return {'job': self.job, 'company': self.company, 'ssn': self.ssn, 'residence': self.residence,
                'current_location': self.current_location, 'bloody_group': self.blood_group,
                'website': self.blood_group, 'username': self.username, 'name': self.name,
                'sex':self.sex, 'address':self.address, 'mail':self.mail, 'birthdate': self.birthdate}


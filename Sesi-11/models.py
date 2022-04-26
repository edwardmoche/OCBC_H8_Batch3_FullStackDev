from datetime import datetime
from config import db, ma

# # ini manggil db, ini returny jd python object
class Person(db.Model):
    # # ini di isi sama tabel di db
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# # nggak tau ini biar apa, tp tambahan improv dr yg ngajar
# def __str__():
#         return f'{Person.person_id} {Person.fname} {Person.lname} {Person.timestamp}'


# # ini buat baca .json dari swagger
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        # # ini ntah knapa error, bikin nggak bisa post sm put
        # sqla_session = db.session
        load_instance = True
    
        
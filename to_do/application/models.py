from . import db


class To_do(db.Model):
    """Data model for books"""

    __tablename__ = 'tasklist'
    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)
    description = db.Column(db.String(64),
                          index=False,
                         unique=True,
                         nullable=False)
    due_date = db.Column(db.DateTime, unique=False, nullable=False)


    #serialiser. These methods help
    #from dict - takes json doc, creates dict, and then you have a book object
    # acts on the current book, and returns it to user in Json
    @staticmethod
    def from_dict(dict):
        return To_do(description=dict['description'], due_date=dict['due_date'])

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           'description': self.description,
           'due_date': self.due_date
       }
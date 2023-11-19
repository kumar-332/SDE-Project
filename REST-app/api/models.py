from api import db

class Post(db.Model):
    __tablename__ = "library"
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)
    author =  db.Column(db.String)
    genre = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "book_title": self.book_title,
            "description": self.description,
            "created_at": str(self.created_at.strftime('%d-%m-%Y')),
            "author": self.author,
            "genre": self.genre
        }

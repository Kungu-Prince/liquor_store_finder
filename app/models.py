from app import db

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    opening_time = db.Column(db.Time, nullable=False)
    closing_time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f'<Store {self.name}>'

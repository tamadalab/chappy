from moji import db
from datetime import date


class MemoData(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(10))
    created_at = db.Column(db.Date, default=date.today)
    
    def id_check(self, id_check):
        return self.query.filter_by(id=id_check).first()
    
class MojiData(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(10))
    created_at = db.Column(db.Date, default=date.today)
    
    def id_check(self, id_check):
        return self.query.filter_by(id=id_check).first()
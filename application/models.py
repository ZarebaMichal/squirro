from dataclasses import dataclass

from . import db


@dataclass
class DocumentModel(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(), nullable=False)
    summary = db.Column(db.Text(), nullable=False)

    def __init__(self, body, summary):
        self.body = (body,)
        self.summary = summary

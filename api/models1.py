from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

from application import db

ma = Marshmallow()

class Changwat(db.Model):
    __tablename__ = 'CATMTable'
    CATM_UKEY = db.Column(db.Integer, primary_key=True)
    CC= db.Column(db.String(2))
    Changwat_TH= db.Column(db.String(255))
    Changwat_EN= db.Column(db.String(255))
    AA = db.Column(db.String(2))
    Ampur_TH = db.Column(db.String(255))
    Ampur_EN = db.Column(db.String(255))
    TT= db.Column(db.String(2))
    Tumbon_TH = db.Column(db.String(255))
    Tumbon_EN = db.Column(db.String(255))
    MM = db.Column(db.String(2))
    
    
 
class ChangwatSchema(ma.Schema):
    CC = fields.String()
    CATM_UKEY = fields.Integer(required=True)
    Changwat_TH = fields.String()
    Changwat_EN = fields.String()
    
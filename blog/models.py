from datetime import datetime

from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

from application import db

ma = Marshmallow()

tag_x_post = db.Table('tag_x_post',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    image = db.Column(db.String(36))
    slug = db.Column(db.String(255), unique=True) # Max for varchar indexes
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)
    gov_id = db.Column(db.Integer, db.ForeignKey('goverment.id'))
    api_url = db.Column(db.String(255), unique=True)
    api_request = db.Column(db.String(255))
    api_response = db.Column(db.String(255))

    author = db.relationship('Author',
        backref=db.backref('posts', lazy='dynamic'))

    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    tags = db.relationship('Tag', secondary=tag_x_post, lazy='subquery',
        backref=db.backref('posts', lazy='dynamic'))

    goverment = db.relationship('Goverment',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, author, title, body, category=None, image=None,
        slug=None, publish_date=None, live=True, goverment=None, 
        api_url=None, api_request=None, api_response = None ):
        self.author_id = author.id
        self.title = title
        self.body = body
        if category:
            self.category_id = category.id
        self.image = image
        self.slug = slug
        if publish_date is None:
            self.publish_date = datetime.utcnow()
        self.live = live
        if goverment:
            self.goverment_id = goverment.id
        self.api_url = api_url
        self.api_request = api_request
        self.api_response = api_response

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return  self.name
    
class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Goverment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return  self.name
    
class GovermentSchema(ma.Schema):
    id = fields.Integer()
    gov_name = fields.String(required=True)

class Parameter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type_param = db.Column(db.String(50))
    description = db.Column(db.String(500))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    post = db.relationship('Post',
        backref=db.backref('posts', lazy='dynamic'))
    
    def __init__(self,name,type_param,description,post_id):
        self.name = name
        self.type_param = type_param
        self.description = description
        self.post_id = post_id

    def __repr__(self):
        return  self.name

    
import mongoengine as me


class Player(me.Document):
    name = me.StringField(required=True)
    age = me.IntField(required=True)
    salary = me.FloatField(required=True)

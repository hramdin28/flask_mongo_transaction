import mongoengine as me


class Team(me.Document):
    name = me.StringField(required=True)
    value = me.FloatField(required=True)
    players = me.ListField(me.StringField())

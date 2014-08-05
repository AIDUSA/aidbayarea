from mongoengine import connect
from monoengine import *

connect('mydb')


class testData(Document)
{
	name = StringField(max_length=200, required=True)
	amount = DecimalField(precision=2)
	year = IntField(max_value=4)
	description = StringField(max_length=500, required=True)
	area = StringField(max_length=200, required=True)
	ngoname = StringField(max_length=200, required=True)
}
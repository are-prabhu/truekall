from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required
from wtforms import validators
from wtforms.validators import ValidationError

#class AccessForm(Form):
class ContactForm(Form):
	UserMail = TextField("EmailID", [validators.Required("Please enter MailID")])
	Name = TextField("Name", [validators.Required("Please enter Name")])
	SourceNumber = TextField("SourceNumber", [validators.Required("Please enter SourceNumber")])
	DestinationNumber = TextField("DestinationNumber", [validators.Required("Please enter DestinationNumber")])
	'''
	SquadName = TextField("Name", [validators.Required("Please enter Your Name")])
	ClusterName = TextField("SourceNumber", [validators.Required("Please enter SourceNumber which call generates")])
	IP = TextField("IP", [validators.Required("Please enter IP which required access.")])
	
	Environment = TextField("Environment", [validators.Required("Please enter Environment which required access.")])
	'''
	Gender = RadioField('', choices=[('True','I\'m Male'),('False','I\'m Female')])

  	submit = SubmitField("submit")

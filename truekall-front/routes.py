from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Mail, Message
from managers.couch_manager import CouchOperations
from managers.config_manager import CallAPIInfo
import json
import requests

app = Flask(__name__)

app.secret_key = 'development key'
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

#@app.route('/contact', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    
    else:
      payload ={}

      payload["UserMail"] = form.UserMail.data
      payload["Name"] = form.Name.data
      payload["SourceNumber"] = form.SourceNumber.data
      payload["DestinationNumber"] = form.DestinationNumber.data

      if form.Gender.data == "True":
	payload["Gender"] = "Male"
      else:
	payload["Gender"] = "Female"


      CouchOperations.couch_insert(payload)

      payload["SecretWord"] = CallAPIInfo.callapi_secretword

      url = "http://%s:%s%s" % (CallAPIInfo.callapi_host,CallAPIInfo.callapi_port,CallAPIInfo.misscall_endpoint)
      headers = {'content-type': 'application/json'}
      results = requests.post(url, data=json.dumps(payload), headers=headers)
      results = str(results.json())
      results = eval(results)
	
      if int(results.keys()[0]) == 200:
        return render_template('success.html')
      else:
        return render_template('fail.html')
  
  
  if request.method == 'GET':
    return render_template('contact.html', form=form)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80,debug=True)

from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Mail, Message
import json
import requests
import sys
sys.path.append('/root/callfront/src')
from managers.couch_manager import CouchOperations

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
      payload["Gender"] = form.Gender.data

      print payload

      url = "http://10.0.1.142:8080/"
      headers = {'content-type': 'application/json'}
      requests.post(url, data=json.dumps(payload), headers=headers)

      return render_template('contact.html', success=True)
  
  
  if request.method == 'GET':
    return render_template('contact.html', form=form)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80,debug=True)

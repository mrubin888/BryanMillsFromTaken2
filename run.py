from flask import Flask, request
import twilio.twiml
from call_utils import say_hi

app = Flask(__name__)

# This is the entry point for our app
@app.route('/', methods=['GET', 'POST'])
def run_server():
	response = twilio.twiml.Response()
	say_hi(response)
	return str(response)

if __name__ == "__main__":
	app.run(debug=True)
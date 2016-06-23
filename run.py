from flask import Flask, request
import twilio.twiml

app = Flask(__name__)

# This is the entry point for our app
@app.route('/', methods=['GET', 'POST'])
def run_server():
	response = twilio.twiml.Response()
	# response.say("Hello fellow human.")
	say_hi(response)
	return str(response)

def say_hi(response):
	response.say("Hello person.")
	return response

if __name__ == "__main__":
	app.run(debug=True)
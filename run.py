from flask import Flask, request, render_template
import twilio.twiml
from call_utils import say_hi

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice_response():
	response = twilio.twiml.Response()
	say_hi(response)
	return str(response)

# This is the entry point for our app
@app.route('/client', methods=['GET'])
def web_client():
	return render_template("call_monitor/call_monitor.html")

if __name__ == "__main__":
	app.run(debug=True)
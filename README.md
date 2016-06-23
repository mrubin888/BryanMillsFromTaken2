# BryanMillsFromTaken2
A fun exploratory twilio exercise where we're going to test its bounds.

## Objective
The intention of this project is to create a library with high level python twilio wrappers for simpler flask integration. These wrappers will be used to run complex call sequences.

Some functionalities we intend to wrap:
* Listen for a call and connect on call received
* Record a connected call and save off the audio
* Record a call between two external numbers
* Place a call and play back recorded audio on connect
* Log states and errors in a web client for debugging

## Getting Started
Please note these instructions are written for *nix systems. If you are running Windows, you should still get full compatability but some of these commands may vary slightly.

### Build and run locally
1. Clone this repo to your local machine.
  * `git clone https://github.com/mrubin888/BryanMillsFromTaken2/`
* Create a virtualenv to use for dev (if you do not have virtualenv you need to install it first)
  * `virtualenv dev_venv`
* Activate your virtualenv
  * `. dev_venv/bin/activate`
* Install project dependencies to your virtualenv
  * `pip install -r "requirements.txt"`
* Run your project locally
  * `python run.py`

To check to see that your local server is running correctly, open your browser and go to "localhost:5000". The browser should display "Hello person".

### Deploy to Heroku
1. Login to Heroku (you may need to install Heroku or create an account first). Enter your credentials when prompted.
  * `heroku login`
* Create a new Heroku project
  * `heroku create`
* Push this git project to Heroku project
  * `git push heroku master`

To check to see that your Heroku server is running correctly, open your browser and go to the url listed in the success log after the push.

### Connect to a Twilio number
1. Create an account at Twilio.com.
* From the website, either accept your free phone number or purchase one if necessary.
* Set your phone number's voice url to "\<your heroku url\>/voice".

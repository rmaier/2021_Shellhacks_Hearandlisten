''' This method starts a Flask instance and provides a small web application with a speech recognition service. 
You upload an mp3 file and get the transcript in the browser. 
'''
from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import os
from google.cloud import speech

import backend.speech2text
import backend.translate

app = Flask(__name__)

#This method will return what should be returned on the homepage

@app.route("/", methods=["GET", "POST"])
def index():
	'''This is the main method who starts the Flask and initiates the method(s).'''
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "pelagic-rig-327114-388e59ecc397.json"
	speech_client = speech.SpeechClient()
	transcript = ""
	if request.method == "POST":
		print("DEBUG : FORM DATA RECEIVED")

		#file does not exist or the file is blank
		if "file" not in request.files:
	   		return redirect(request.url)

		#if a file exists it will give me the file
		file = request.files["file"]
		if file.filename == "":
	   		return redirect(request.url)

		if file:
			# 1. Speech2Text
			
			response_standard_mp3 = backend.speech2text.speech2text(file)

			transcript = response_standard_mp3.results[0].alternatives[0].transcript
			
			## 2. Translate
			
			

	return render_template('index.html', transcript = transcript)

if __name__ == "__main__":
   app.run(debug = True, threaded=True)

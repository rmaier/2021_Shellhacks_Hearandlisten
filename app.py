from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import os
from google.cloud import speech


app = Flask(__name__)

#This method will return what should be returned on the homepage

@app.route("/", methods=["GET", "POST"])
def index():
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
			# Google Cloud -> IAM & Admin -> create service Acc --> create key
			os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'pelagic-rig-327114-388e59ecc397.json'
			speech_client = speech.SpeechClient()

			# 1. Ex 1 local media file

			byte_data_mp3 = file.read() # file is a Fask "FileStorage" object. I can read it directly. https://stackoverflow.com/questions/63306323/typeerror-expected-str-bytes-or-os-pathlike-object-not-filestorage-keeps-popp
			audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

			## 2. Configure Media files

			config_mp3 = speech.RecognitionConfig(
				sample_rate_hertz=48000,
				enable_automatic_punctuation=True,
				language_code='en-US'
			)

			# 3. Transcibing the RecognitionAudio objects
			# needed to enable Google Cloud to Speech module on website

			response_standard_mp3 = speech_client.recognize(
				config=config_mp3,
				audio=audio_mp3
			)

			transcript = response_standard_mp3.results[0].alternatives[0].transcript

	return render_template('index.html', transcript = transcript)

if __name__ == "__main__":
   app.run(debug = True, threaded=True)

# ShellHacks SpeechtoText
# pip install --upgrade google-cloud-speech
# ffmpeg -i jobs.mp3 jobs.wav

import os 
from google.cloud import speech 

# Google Cloud -> IAM & Admin -> create service Acc --> create key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'pelagic-rig-327114-388e59ecc397.json'
speech_client = speech.SpeechClient()

# 1. Ex 1 local media file

media_file_name_mp3 = 'jobs.mp3'

with open(media_file_name_mp3, 'rb') as f1: 
	byte_data_mp3 = f1.read()
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
	config = config_mp3,
	audio = audio_mp3
)

print(response_standard_mp3)

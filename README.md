# 2021 Shellhacks: *Hearandlisten*
## Shellhacks: Productivity Booster with Google Cloud. 

## Features: 
* voice recognition &rarr; speech to text
* translate to other language (text) &rarr; Cloud translation

## Steps: 
* workflow
* development

## Backend: 
* mic / audio file input
* route to API (audio)

* receive text
* route to cloud translator
* receive text and print

## Frontend: 
* recording button /file upload
* choose language (opt)
* import from other app (share to)
* show speech to text
* print translation to screen (copiable)

## Installed packages: 
```python
pip install flask
pip install google-cloud-speech
pip install google-cloud-translate
pip install google-cloud-texttospeech
pip install SpeechRecognition
```

See also the [requirements file](./requirements.txt).

# Setup of the Google Cloud Platform

https://console.cloud.google.com/ &rarr; register

## create new project

* new project &rarr; enter project name
* create credentials
  * speech2text api
  * create keys &rarr; keys &rarr; add key &rarr; JSON &rarr; download and store it secure

## add needed API's

* Cloud Speech-to-Text API ```from google.cloud import speech```
* Cloud Translation API ```from google.cloud import translate_v2 as translate```
* Cloud Text-to-Speech API ```from google.cloud import texttospeech```

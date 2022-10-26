from flask import render_template, request
from flask import Flask
import requests
import os

app = Flask(__name__)

key = os.getenv("AZURE_TRANSLATION_API_KEY")
region = 'eastus2'
endpoint = 'https://api.cognitive.microsofttranslator.com'

def detect_language(text, key, region, endpoint):
    # Use the Translator detect function
    path = '/detect'
    url = endpoint + path
    # Build the request
    params = {
        'api-version': '3.0'
    }
    headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json'
    }
    body = [{
        'text': text
    }]
    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    # Get language
    language = response[0]["language"]
    # Return the language
    return language

def translate(text, source_language, target_language, key, region, endpoint):
    # Use the Translator translate function
    url = endpoint + '/translate'
    # Build the request
    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': target_language
    }
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json'
    }
    body = [{
        'text': text
    }]
    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    # Get translation
    translation = response[0]["translations"][0]["text"]
    # Return the translation
    return translation

@app.route("/translate", methods=['POST', 'GET'])
def translateform():
    if request.method == 'POST':
        detected_language  = detect_language(request.form['source_text'], key, region, endpoint)
        translated_english = translate(request.form['source_text'], detected_language, 'en', key, region, endpoint)
        translated_spanish = translate(request.form['source_text'], detected_language, 'es', key, region, endpoint)
        translated_french = translate(request.form['source_text'], detected_language, 'fr', key, region, endpoint)
        translated_dutch = translate(request.form['source_text'], detected_language, 'nl', key, region, endpoint)
        translated_german = translate(request.form['source_text'], detected_language, 'de', key, region, endpoint)
        return render_template("translationpage.html", english_translation = translated_english, spanish_translation = translated_spanish, french_translation = translated_french, dutch_translation = translated_dutch, german_translation = translated_german)
    else:
        return render_template("translationpage.html")

#from dotenv import load_dotenv
import os
import requests

#load_dotenv()
key = os.getenv("AZURE_TRANSLATION_API_KEY")
key2 = os.getenv("AZURE_TRANSLATION_API_KEY2")

#print(key)
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

mytext = 'can you see a cat?'
detected_language  = detect_language(mytext, key, region, endpoint)

languages = ['en', 'es', 'fr', 'nl', 'de']
for target_language in languages:
    print(translate(mytext, detected_language, target_language, key, region, endpoint))
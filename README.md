# sentence_translation
Code to translate a sentence into the 5 languages that I 'daily duolingo',  connecting to an Azure API.

Takes a sentence from an html page, detects the language it was written in, sends that sentence to the API and returns the same sentence translated into the 5 languages that I am studying; spanish, french, dutch, german and scottish gaelic, displayed on the html page.

## Instructions for use:
### Quick install using pip & requirements.txt (recommended)
Create a virtual environment and type this pip command at the command line. 
```bash
pip install -r requirements.txt
```

###Challenges Overcome:
- Learning to connect to an Azure API
- Learning how to store a development key as an environmental variable so that it is not published on github.
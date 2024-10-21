# pdf2audio
PDF-to-text conversion and text-to-speech conversion using Google Cloud Services

**Generate audiobooks directly from pdf-files!**

## PDF-Extraction
The conversion from a pdf to raw text is an easy job when using PdfReader.
Substitutions will be necessary to eliminate headers and footers as well as systematic conversion errors.
It's planned to provide an external substitution table for customisation.

## Text-to-Speech Conversion
This section describes Google Cloud Services setup for text-to-speech conversion via REST API.

This video helped me make my breakthrough.: https://www.youtube.com/watch?v=GVPWz-nhJhg

### Setup
- Register/Activate Google Cloud Services (https://console.cloud.google.com/)
- Create new Project
- Select newly created Project
- Activate API: Navigation Menu->APIs & Services->Library
    - Filter for "text to speech"
    - Select Cloud Text-to-Speech API
    - Enable
- Create Service Account: Navigation Menu->APIs & Services->Credentials
    - + CREATE CREDENTIALS->Service Account
    - Enter name
    - CREATE AND CONTINUE
    - Grant this service account to project->Chose "Owner"
    - Skip 3rd Step
    - DONE
- Click on newly created Service Account
    - Click on KEYS on top
    - ADD KEY
    - Create new Key->JSON
    - CREATE
    - Store file into development folder
- Prepare Python Develpopment
    - pip install google-cloud-texttospeech
    - Code works using Secrets in vscode, set GOOGLE_APPLICATION_CREDENTIALS to path of JSON-file

### Voice Selection
https://cloud.google.com/text-to-speech/docs/voices


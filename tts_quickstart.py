import os
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS']

client = texttospeech.TextToSpeechClient()

text_block = """Ho iniziato a camminare verso quella ﬁnestra, ma sono inciampata in una scatola. Ahi, che male!
"""

synthesis_input = texttospeech.SynthesisInput(text=text_block)

voice = texttospeech.VoiceSelectionParams(
    language_code='it-IT',
    name='it-IT-Neural2-A',
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    # effects_profile_id=['small-bluetooth-speaker-class-device'],
    # speaking_rate=1,
    # pitch=1,
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config,
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

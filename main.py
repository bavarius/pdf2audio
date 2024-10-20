from tkinter import *
from tkinter import filedialog
from pypdf import PdfReader
import re
import os
from google.cloud import texttospeech

input_file = ''
output_folder = './output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def convert_text_to_speech(page_no, text):
    """The text-to-speech conversion function"""
    global input_file
    global output_folder
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code='it-IT',
        name='it-IT-Neural2-A',
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config,
    )

    tmp = os.path.basename(input_file)  # file name before removing extension
    out_file_name = os.path.splitext(tmp)[0] + f'_{page_no:03d}' + '.mp3'
    output_file = output_folder + '/' + out_file_name

    # The response's audio_content is binary.
    with open(output_file, "wb") as output:
        # Write the response to the output file.
        output.write(response.audio_content)
        print(f"Audio content written to {output_file}.")
        # TODO Write text into GUI textbox


def do_substitutions(page_no, text):
    """Substitute header/footer information or read errors"""
    new_str = ""
    if page_no > 0:
        new_str += str(page_no) + '\n'
    new_str += text.replace('7', 'tt')  # Double 't's have been read as 7.
    new_str = new_str.replace('italiano-bello.com', '')  # footer replacement
    new_str = new_str.replace('©', '')  # footer replacement
    new_str = re.sub('Italiano Bello[0-9].*',
                     '', new_str)  # footer replacement
    # TODO Read substitutions from external csv-file
    convert_text_to_speech(page_no, new_str)


def read_pdf(fname):
    """Store PDF page by page"""
    if fname != '':
        # creating a pdf reader object
        reader = PdfReader(fname)
        for no, page in enumerate(reader.pages):
            do_substitutions(no, page.extract_text())


def browse_file():
    """"Function for opening the file explorer window"""
    global input_file
    input_file = filedialog.askopenfilename(initialdir="resources",
                                            title="Select a File",
                                            filetypes=(("PDF-files",
                                                        "*.pdf"),
                                                       ("all files",
                                                        "*.*")))

    # Change label contents
    label_file_explorer.configure(text=input_file)

    read_pdf(input_file)


# Create the root window
window = Tk()

# Set window title
window.title('PDF-to-Audiobool-Converter')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="File...",
                            height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Browse for File",
                        command=browse_file)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing the widgets at respective positions in a table like structure by specifying rows and columns
label_file_explorer.grid(row=0)
button_explore.grid(row=1)
button_exit.grid(row=2, pady=20)

# Let the window wait for any events
window.mainloop()

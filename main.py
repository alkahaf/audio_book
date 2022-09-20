import pyttsx3
import PyPDF2

with open('ATOM.pdf', 'rb') as book:

    full_text = ""

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content

    audio_reader.save_to_file(full_text, "myaudiobook.mp3")
    audio_reader.runAndWait()
# book = open('ATOM.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)
# speaker = pyttsx3.init()
# for num in range(100, pages):
#     pages = pdfReader. getPage(11)
#     text = pages.extractText()
#     speaker.say(text)
#     speaker.runAndWait()

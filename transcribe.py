import os
import openpyxl
import pydub
import speech_recognition as sr
from os import path
from pydub import AudioSegment
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment



# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("recording.mp3")
sound.export("transcript.wav", format="wav")


# delete MP3 file
os.unlink('recording.mp3')


# transcribe audio file                                                         
AUDIO_FILE = "transcript.wav"


# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        text = r.recognize_google(audio)
        print("Transcription: " + text)

#write to .txt file
with open('C:\\Users\\Bathtub\\MyPyScripts\\Transcriptor\\transcription.txt', 'w') as f:
        f.write(text)
        f.close()

#write to spreadsheet
wb = load_workbook('transcription.xlsx')
ws = wb.active
ws.append([text])
wb.save('transcription.xlsx')


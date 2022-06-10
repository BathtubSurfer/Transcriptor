# Transcriptor
Used for Software Defined Radio(SDR) software and recordings they can output.


Waits for a recording.mp3 to appear in program folder. Then transcribes audio, spits out .txt of transcription, and pushes text to Excel workbook with openpyxl append()


*make a backup of recording.mp3 as it will reformat to .wav and delete original file*

Requires:
-Pydub and its dependencies, -openpyxl


to-do: word-wrap/formatting cells to bring text into better visible order

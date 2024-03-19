import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "e8d941016b3b4e8cb6b723a2e82b2dd8"

# URL of the file to transcribe
FILE_URL = "hai.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

l=transcript.export_subtitles_srt()
file1 = open('hai.srt', 'w+')
file1.write(l)
file1.close()
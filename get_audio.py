from __future__ import unicode_literals
import io, os, re, string
from os import listdir
import youtube_dl
import googleapiclient
import split_audio
from google.cloud import speech_v1p1beta1 as speech

ydl_opts = {
	'format': 'bestaudio/best',
	'outtmpl': '%(id)s.%(ext)s',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'wav',
		'preferredquality': '192',
	}],
}


def split(file_path):
	split_audio.split_audio_wav(file_path, 35000, "data/")


def get_metadata(url):
	result = []
	with youtube_dl.YoutubeDL({'format': 'bestaudio/best'}) as ydl:
		info_dict = ydl.extract_info(url, download=False)
		video_id = info_dict.get('id', None)
		video_title = info_dict.get('title', None)
	result.append(video_title)
	result.append(video_id)
	return result


def recognize_audio(file_path):
	client = speech.SpeechClient()
	speech_file = file_path
	with io.open(speech_file, 'rb') as audio_file:
		content = audio_file.read()
	audio = speech.types.RecognitionAudio(content=content)
	config = speech.types.RecognitionConfig(language_code='en-US', audio_channel_count=2, enable_automatic_punctuation=True)
	response = client.recognize(config, audio)

	for result in response.results:
		alternative = result.alternatives[0]
		return alternative.transcript


def get_audio(song_url):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info_dict = ydl.extract_info(song_url, download=True)
		video_id = info_dict.get('id', None)
	return video_id + '.wav'

def video_transcript(url):
	result = ""
	file = get_audio(url)
	split(file)
	for split_file in listdir('data/'):
		result = result + " " + recognize_audio("data/" + split_file)
		os.remove("data/" + split_file)
	os.remove(file)
	return result

# def main():
# 	# url = "https://www.youtube.com/watch?v=Y5Nu7U1ucXA"
# 	# url = "https://www.youtube.com/watch?v=C7ducZoLKgw"
# 	video_transcript("https://www.youtube.com/watch?v=Y5Nu7U1ucXA")


# if __name__ == '__main__':
# 	main()
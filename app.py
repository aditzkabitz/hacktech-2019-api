#!flask/bin/python
from flask import Flask
from flask import request, abort
from urllib.parse import unquote
import sample, get_audio

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return 'hello'

@app.route('/video_metadata', methods=['POST'])
def metadata():
	if not request.json or not 'url' in request.json:
		abort(400)
	url = url = unquote(request.json['url'])
	return tuple(get_audio.get_metadata(url))

@app.route('/video_summary', methods=['POST'])
def summary():
	if not request.json or not 'url' in request.json:
		abort(400)
	url = unquote(request.json['url'])
	result = get_audio.video_transcript(url)
	return sample.text_summary(result)

if __name__ == '__main__':
	app.debug=True
	app.run(host= '0.0.0.0', port=7000)

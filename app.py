#!flask/bin/python
from flask import Flask
from flask import request, abort
from urllib.parse import unquote
from flask import Flask
import sample, get_audio
import jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return 'hello'



@app.route('/video_summary', methods=['POST'])
def summary():
	if not request.json or not 'url' in request.json:
		abort(400)
	url = url = unquote(request.json['url'])
	result = get_audio.video_transcript(url)
	return sample.text_summary(result)

if __name__ == '__main__':
	app.run(host= '0.0.0.0', port=5000)

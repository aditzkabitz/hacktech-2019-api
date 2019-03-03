from flask import Flask
from flask_restful import Api, Resource, reqparse
import urllib
import get_audio, sample
from flask import request
from urllib.parse import unquote



app = Flask(__name__)
api = Api(app)

print("hello")

class summaries(Resource):
    def get(self, url):
        return "please post!"

    def post(self):
        args = request.args
        print(args)
        url = unquote(args['url'])
        result = get_audio.video_transcript(url)
        return jsonify({'summary': sample.text_summary(result)}), 201
      
api.add_resource(summaries, "/summaries")

app.run(debug=True)
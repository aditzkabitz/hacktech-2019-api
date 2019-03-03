from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import math
import nltk
from nltk.tokenize import sent_tokenize

def text_summary(text, summary_size=0.25):
	LANGUAGE = "english"
	result = ""
	SENTENCES_COUNT = math.floor(summary_size * len(sent_tokenize(text)))
	
	parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		result = result + " " + str(sentence)

	return result

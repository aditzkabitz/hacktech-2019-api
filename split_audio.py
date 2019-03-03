import wave
import ntpath
import math
import contextlib
from pydub import AudioSegment


def get_ms_length(file_path):
	with contextlib.closing(wave.open(file_path,'r')) as f:
	    return 1000 * (f.getnframes() / float(f.getframerate()))
	    

def split_audio_wav(old_file_path, increment_size, new_file_folder=""):
	length = get_ms_length(old_file_path)
	audio_sample = AudioSegment.from_wav(old_file_path)
	for index in range(0, math.ceil(length / increment_size) * increment_size, increment_size):
		segment = audio_sample[index:index + increment_size]
		file_name = new_file_folder + ntpath.basename(old_file_path)[:len(ntpath.basename(old_file_path)) - 4] + '_' + str(index/1000) + '.wav'
		segment.export(file_name, format="wav")


from pathlib import Path
from base64 import b64decode
class Search:

	def __init__(self, directory, word):
		self.directory = directory
		self.word = word
		self.files = []

	def get_all_files(self, directory):
		path = Path(directory)
		self.files += [file.resolve() for file in path.iterdir() if file.is_file()]
		directories = [directory for directory in path.iterdir() if directory.is_dir()]
		if directories:
			for dir in directories:
				return self.get_all_files(dir)
		return self.files

	def search(self, file):
		with open('{}'.format(file), 'r', errors='ignore') as f:
			if self.word in f.read():
				print(file)

	def start_search(self):
		for file in self.get_all_files(self.directory):
			self.search(file)

client = Search(directory="", word="")
client.start_search()

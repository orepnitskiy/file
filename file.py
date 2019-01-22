import os
import tempfile

"""
You can use that class to write data to the file, sum files and iterate within strings in the file """


class File():
	def __init__(self, filedirectory):
		self.filedirectory = filedirectory
		self.current = 0
		
		
	def __str__(self):
		return self.filedirectory
	
	
	def write(self,text):
		"""
		Function that write value to the file
		"""
		with open(self.filedirectory, 'w') as f:
			f.write(text)
	def __add__(self1,self2):
		
		
		"""
		You can use that function to get new 
		file that unite two files and create
		new file in tempdirectory
		"""
		with open(os.path.join(tempfile.gettempdir(),'new_obj.txt'), 'w') as f:
			with open(self1.filedirectory, 'r') as f2:
				with open(self2.filedirectory, 'r') as f3:
					for line in f2:
						f.write(line)
					for line in f3:
						f.write(line)
					return File(os.path.join(tempfile.gettempdir(),'new_obj.txt'))
				
				
	def _strings_count(self):
		counter = 0
		with open(self.filedirectory, 'r') as f:
			for line in f:
				counter += 1
			return counter
		
		
	def __iter__(self):
		return self
	
	
	def __next__(self):
		"""
		Iterator which you can use to iterate
		through strings of the file(built-in 
		class)
		"""
		with open(self.filedirectory, 'r') as f:
			lines = f.readlines()
			if self.current < self._strings_count():
				self.current += 1
				return lines[int(self.current)-1]
			else:
				raise StopIteration

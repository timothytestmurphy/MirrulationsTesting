import csv
import os.path


class Pathing:
	def get_test_file(self):
		my_path = os.path.abspath(os.path.dirname(__file__))
		new_path = os.path.join(my_path, "../../tests/test_files/test.csv")
		with open(new_path) as f:
			test = csv.reader(f)
			for line in test:
				for word in line:
					return(word)

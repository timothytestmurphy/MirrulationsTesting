"""This module prints a path"""
import csv
import os.path

#pylint: disable=R0903
class Pathing:
    """Example of pathing"""
    # pylint: disable=R0201
    def get_test_file(self):
        """method for showing pathing"""
        my_path = os.path.abspath(os.path.dirname(__file__))
        new_path = os.path.join(my_path, "../../tests/test_files/test.csv")
        with open(new_path) as file:
            test = csv.reader(file)
            for line in test:
                for word in line:
                    return word

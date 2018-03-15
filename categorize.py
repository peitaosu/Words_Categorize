import os, sys

class Categorizer():
    def __init__(self):
        self.data = None

    def preprocess(self):
        # TODO - add preprocess implementation here
        return self.data

    def postprocess(self):
        # TODO - add postprocess implementation here
        return self.data

    def etyma_matching(self, level=3, language="en"):
        # TODO - add etyma matching implementation here
        return self.data

    def read_data(self, input_file_path):
        with open(input_file_path, "r") as input_file:
            self.data = input_file.read()

    def save_data(self, output_file_path):
        with open(output_file_path, "w") as output_file:
            output_file.write(self.data)

if __name__ == "__main__":
    input_file_path = "in.txt"
    output_file_path = "out.txt"
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_file_path = sys.argv[2]
    categorizer = Categorizer()
    categorizer.read_data(input_file_path)
    categorizer.preprocess()
    categorizer.etyma_matching()
    categorizer.postprocess()
    categorizer.save_data(output_file_path)

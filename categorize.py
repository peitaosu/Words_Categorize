import os, sys

class Categorizer():
    def __init__(self):
        self.data = None

    def preprocess(self, func):
        # TODO - add preprocess implementation here
        self.data = func(self.data)

    def postprocess(self, func):
        # TODO - add postprocess implementation here
        self.data = func(self.data)

    def etyma_matching(self, level=3, language="en"):
        # TODO - add etyma matching implementation here
        pass

    def read_data(self, input_file_path):
        with open(input_file_path, "r") as input_file:
            self.data = input_file.read()

    def save_data(self, output_file_path):
        with open(output_file_path, "w") as output_file:
            output_file.write(self.data)

def split_words(data):
    return data.replace(';',' ').replace(',',' ').replace('\t',' ').replace('\n',' ').replace('\r',' ').split()

def join_words(word_list):
    return "\n".join(word_list)

if __name__ == "__main__":
    input_file_path = "in.txt"
    output_file_path = "out.txt"
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_file_path = sys.argv[2]
    categorizer = Categorizer()
    categorizer.read_data(input_file_path)
    categorizer.preprocess(split_words)
    categorizer.etyma_matching()
    categorizer.postprocess(join_words)
    categorizer.save_data(output_file_path)

import os, sys

class Categorizer():
    def __init__(self):
        self.data = None

    def preprocess(self, func):
        self.data = func(self.data)

    def postprocess(self, func):
        self.data = func(self.data)

    def etyma_matching(self, level=3, language="en"):
        words_sets = {}
        for word in self.data:
            ends_word = word[ 0 - level:]
            if ends_word in words_sets.keys():
                words_sets[ends_word].append(word)
            else:
                words_sets[ends_word] = [word]
        self.data = words_sets

    def read_data(self, input_file_path):
        with open(input_file_path, "r") as input_file:
            self.data = input_file.read()

    def save_data(self, output_file_path):
        with open(output_file_path, "w") as output_file:
            output_file.write(self.data)

import os, sys, json
from categorize import Categorizer

def split_words(data):
    return data.replace(';',' ').replace(',',' ').replace('\t',' ').replace('\n',' ').replace('\r',' ').split()

def join_words(word_list):
    return "\n".join(word_list)

def dict_to_string(word_dict):
    return json.dumps(word_dict)

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
    categorizer.postprocess(dict_to_string)
    categorizer.save_data(output_file_path)

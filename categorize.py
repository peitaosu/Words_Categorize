import os, sys

def preprocess(input):
    # TODO - add preprocess implementation here
    processed = input
    return processed

def postprocess(input):
    # TODO - add postprocess implementation here
    processed = input
    return processed

def etyma_matching(input, level=3, language="en"):
    # TODO - add etyma matching implementation here
    processed = input
    return processed

def read_data(input_file_path):
    with open(input_file_path, "r") as input_file:
        return input_file.read()

def save_data(out_data, output_file_path):
    with open(output_file_path, "w") as output_file:
        output_file.write(out_data)

if __name__ == "__main__":
    input_file_path = "in.txt"
    output_file_path = "out.txt"
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_file_path = sys.argv[2]
    data = read_data(input_file_path)
    data = preprocess(data)
    data = etyma_matching(data)
    data = postprocess(data)
    save_data(data, output_file_path)

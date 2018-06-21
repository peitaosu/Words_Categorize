# Words Categorize


[![GitHub license](https://img.shields.io/github/license/peitaosu/Words_Categorize.svg)](https://github.com/peitaosu/Words_Categorize/blob/master/LICENSE)


This project is implementing a light, simple and flexible words categorizer.

## Usage
```
> python run.py [in.txt] [out.txt]
```

## Define Your Process
```
def split_words():
    pass

def dict_to_string():
    pass

categorizer = Categorizer()
categorizer.read_data(input_file_path)
categorizer.preprocess(split_words)
categorizer.etyma_matching()
categorizer.postprocess(dict_to_string)
categorizer.save_data(output_file_path)
```
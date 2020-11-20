# directory-json-generator

## Description:
This module takes a directory as an input and generates a json file with the list of all files, sub folders recurisvely inside the directory.

## Output JSON Structure
"id": ""  // system id or generated by module\
"name": ""  // file/folder name \
"type": ""  // supported- ROOT, DIRECTORY, FILE\
"parent_id": "" // id of parent\
"size": ""  // size of file\
""modified_at":  // last modified date
"created_at":  // last created date

### Sample output json
{
    "id": 1970324837256664,
    "name": "Professional Vanilla.docx",
    "type": "FILE",
    "parent_id": 3096224744069512,
    "size": 5646616,
    "modified_at": 1605187475.0272171,
    "created_at": 1565164204.0
}

## Technologies included
1. Python

## RUN
usage: main.py [-h] [--output_json_path OUTPUT_JSON_PATH] input_path

Get child files and directory details in the json format as specified in Readme

positional arguments:
  input_path            Path of the input directory

optional arguments:
  -h, --help            show this help message and exit
  --output_json_path OUTPUT_JSON_PATH, -o OUTPUT_JSON_PATH
                        Output json path with file name. Default is "result.json" in current directory.

### Example:
python src/main.py "C:/Users/user1/test" -o test.json
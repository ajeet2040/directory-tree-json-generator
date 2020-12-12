# directory-json-generator

## Description:
This module takes a directory as an input and generates a json file with the list of all files, sub folders recurisvely inside the directory.

## Output JSON Structure
"id": ""  // system id - generated by OS\
"name": ""  // file/folder name \
"type": ""  // supported- ROOT, DIRECTORY, FILE\  
"parent_id": "" // id of parent\
"size": ""  // size of file - in bytes\
""modified_at":  // last modified date in timestamp seconds\
"created_at":  // last created date in timestamp seconds\
"file_path": "" // full local path of file

### Sample object from output json
  {
      "id": 1688849860573236,
      "name": "Professional Vanilla.docx",
      "type": "FILE",
      "parent_id": 3096224744126470,
      "size": 5646616,
      "modified_at": 1605187475.0272171, 
      "created_at": 1605188234.9277682,
      "file_path": "C:\\Users\\test\\Local Drive\\test1\\Others\\test2\\Professional Vanilla.docx"
  }

## Technologies used
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

ERROR with belkow directory path- To be checked later

E:\Data\E Drive\mob bckups\aj mobile\Lenevo\Removable Disk\AJ\songs\bolly\Once Upon A Time In Mumbaai (2010) ~190Kbps [www.DJMaza.Com]\Once Upon A Time In Mumbaai (2010) ~190Kbps-VBR (With Covers) [www.DJMaza.Com]
E:\\Data\\E Drive\\mob bckups\\aj mobile\\Lenevo\\Removable Disk\\AJ\\songs\\remix\\Bolly Oldies Mix Vol.3 - Various Djs (2010) [www.DJMaza.Com]\\Bolly Oldies Mix Vol.3 - Various Djs (2010) [www.DJMaza.Com]\\01 - Dil Tod Ke Na Ja (Pyaar Ke Side Effects) [www.DJMaza.Com].mp3
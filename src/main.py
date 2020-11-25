# Python script to create the directory and file structure in the JSON format

import os
import json
import platform
import argparse
import traceback
from pathlib import Path

parser = argparse.ArgumentParser(description='Get child files and directory details in the json format as specified in Readme')
parser.add_argument('input_path', help='Path of the input directory')
parser.add_argument('--output_json_path',"-o", default='result.json', help='Output json path with file name. Default is "result.json" in current directory.')

# TO DO
# 0. Add additional file data as required -- Completed
# 1. Add exception handling -- Completed
# 2. Add documentation -- Completed
# 3. Code refactoring as applicable - naming conventions, modularity etc. -- Completed
# 4. Add logs , print statments -- Completed
# 5. Add usage message and run parameters -- Completed
# 6. Update Readme as applicable -- Completed
# 7. Next Version - Do packaging

def get_file_directory_id(file_path):
    """
    Gets system id of file or directory
    @param: file_path: File or directory absolute path
    """
    return os.stat(file_path, follow_symlinks=False).st_ino

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    @param: path_to_file: absolute file path whose created date is required.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

def append_record_in_output_json(output_json, file_path, type, parent_id):
    """
    Saves the json file at the specified location.
    @param: output_json: List where oytput is stored
    @param: file_path: File or directory absolute path
    @param: type: directory or file or root
    @param: parent_id: system id of parent
    """
    record_dict = {}    # temp dict of file or directory details
    record_dict["id"] =  get_file_directory_id(file_path)
    record_dict["name"] = os.path.basename(file_path)
    record_dict["type"] = type
    record_dict["parent_id"] = parent_id
    if type == "FILE":
        record_dict["size"] = os.path.getsize(file_path)
    record_dict["modified_at"] = os.path.getmtime(file_path)
    record_dict["created_at"] = creation_date(file_path)
    # Used path to avoid file path with mix of forward and backslash - (In windows when ran with forward slash input)
    record_dict["file_path"] = str(Path(file_path))  
    # Uncomment if need other details from os.stat
    # record_dict["stats"] = os.stat(file_path)
    output_json.append(record_dict)
    return output_json

def save_json_file(output_json__path, json_data):
    """
    Saves the json file at the specified location.
    @param: output_json__path: Json file path
    @param: json_data: JSON data to be saved in file
    """
    with open(output_json__path, 'w') as f:  # writing JSON object
        json.dump(json_data, f)

def main_func(input_path, output_json_path):
    """
    Main function of processing. Uses os walks to get the directory and file details and saves it to json file.
    @param: input_path: Input directory path whose child directory and file details are required.
    @param: output_json_path: Output JSON file path with name
    """
    try:
        # Remove in case root path ends with single forward slash or 2 double slash or else handle in below finding name case
        input_path = input_path.rstrip('\\')
        input_path = input_path.rstrip('/')
        print("Processing started for input directory:", input_path, " .....")
        output_json = []    # List of file/directory structure in json format
        # Adding root directory
        output_json = append_record_in_output_json(output_json, input_path, "ROOT", None)
        # OS walk through the root directory
        for root, dirs, files in os.walk(input_path):
            # Get Parent id
            parent_id = get_file_directory_id(root)
            # Child directories
            for dir in dirs:
                dir_path = os.path.join(root,dir)
                output_json = append_record_in_output_json(output_json, dir_path, "DIRECTORY", parent_id)
            # Child files 
            for file in files:
                file_path = os.path.join(root,file)
                output_json = append_record_in_output_json(output_json, file_path, "FILE", parent_id)
        # Processing completed. Saving JSON file
        save_json_file(output_json_path, output_json)
        print("Processing is completed. Saved json file at location: ", output_json_path)
    except Exception as e:
        print("Some error occured: ", str(e))
        print(traceback.print_exc())

if __name__ == "__main__":
    args = parser.parse_args()
    input_path = args.input_path
    output_json_path = args.output_json_path
    main_func(input_path, output_json_path)
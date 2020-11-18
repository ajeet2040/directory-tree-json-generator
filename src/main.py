# Python script to create the directory and file structure in the JSON format

import os
import json
import platform

# TO DO
# 0. Add additional file data as required -- Completed
# 1. Add exception handling
# 2. Add documentation
# 3. Code refactoring as applicable - naming conventions, modularity etc.
# 4. Add logs , print statments
# 5. Add usage message
# 6. Update Readme as applicable

def get_file_folder_id(file_path):
    return os.stat(file_path, follow_symlinks=False).st_ino

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
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
    record_dict = {}
    record_dict["id"] =  get_file_folder_id(file_path)
    record_dict["name"] = os.path.basename(file_path)
    record_dict["type"] = type
    record_dict["parent_id"] = parent_id
    if type == "FILE":
        record_dict["size"] = os.path.getsize(file_path)
    record_dict["modified_at"] = os.path.getmtime(file_path)
    record_dict["created_at"] = creation_date(file_path)
    # record_dict["stats"] = os.stat(file_path)
    output_json.append(record_dict)
    return output_json

def save_json_file(dest_file_path, json_data):
    with open(dest_file_path, 'w') as f:  # writing JSON object
        json.dump(json_data, f)

def main_func(root_path):
    print("Hey bro", root_path)
    output_json = []    # List of file/directory structure in json format
    # Remove in case root path ends with single forward slash or 2 double slash or else handle in below finding name case
    # Adding root folder
    output_json = append_record_in_output_json(output_json, root_path, "ROOT", None)
    # OS walk through the root directory
    for root, dirs, files in os.walk(root_path):
        # Get Parent id
        parent_id = get_file_folder_id(root)
        # Child directories
        for dir in dirs:
            print(dir)
            dir_path = os.path.join(root,dir)
            output_json = append_record_in_output_json(output_json, dir_path, "DIRECTORY", parent_id)
        # Child files 
        for file in files:
            print(file)
            file_path = os.path.join(root,file)
            output_json = append_record_in_output_json(output_json, file_path, "FILE", parent_id)
    # Processing completed
    print("Processing is completed. Saving Json file")
    save_json_file("result.json", output_json)
   
if __name__ == "__main__":
    root_path = "C:/Users/ajeet/Local Drive/"
    main_func(root_path)
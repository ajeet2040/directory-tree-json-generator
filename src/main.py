# Python script to create the directory and file structure in the JSON format

import os
import json

# TO DO
# 0. Add additional file data as required
# 1. Add exception handling
# 2. Add documentation
# 3. Code refactoring - naming conventions, modularity etc.
# 4. Add logs , print statments 

def get_file_folder_id(file_path):
    return os.stat(file_path, follow_symlinks=False).st_ino

def append_record_in_dir_json(output_dir_json, file_path, type, parent_id):
    record_dict = {}
    record_dict["id"] =  get_file_folder_id(file_path)
    record_dict["name"] = os.path.basename(file_path)
    record_dict["type"] = type
    record_dict["parent_id"] = parent_id
    output_dir_json.append(record_dict)
    return output_dir_json

def save_json_file(dest_file_path, json_data):
    with open(dest_file_path, 'w') as f:  # writing JSON object
        json.dump(json_data, f)

def main_func(root_path):
    print("Hey bro", root_path)
    output_dir_json = []
    # Remove in case root path ends with single forward slash or 2 double slash or else handle in below finding name case
    # Adding root folder
    output_dir_json = append_record_in_dir_json(output_dir_json, root_path, "ROOT", None)
    # OS walk through the root directory
    for root, dirs, files in os.walk(root_path):
        # Get Parent id
        parent_id = get_file_folder_id(root)
        # directories
        for dir in dirs:
            print(dir)
            dir_path = os.path.join(root,dir)
            output_dir_json = append_record_in_dir_json(output_dir_json, dir_path, "DIRECTORY", parent_id)
        # files 
        for file in files:
            print(file)
            file_path = os.path.join(root,file)
            output_dir_json = append_record_in_dir_json(output_dir_json, file_path, "FILE", parent_id)
    # Processing completed
    print("Processing is completed. Saving Json file")
    save_json_file("result.json", output_dir_json)
   
if __name__ == "__main__":
    root_path = "C:/Users/ajeet/Local Drive/Softwares"
    main_func(root_path)
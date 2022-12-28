import shutil
import glob
import os
import sys

input_mode = input("what is mode?: ")
if input_mode == "create":
    directory_path = input("directory path to ./path/path2/~~/ ")
    os.makedirs(directory_path)
    sys.exit("success!")

elif input_mode == "copy":
    input_path = input("input file name ")
    output_path = input("output path new file name ")
    shutil.copyfile(input_path, output_path)
    sys.exit("success!")

elif input_mode == "duplication":
    input_path = input("input path to ./directory path/? ")
    output_path = input("output path to ./directory path/? ")
    shutil.copytree(input_path, output_path)
    sys.exit("success!")

elif input_mode == "delete":
    input_path = input("input path to ./directory path/ or /file name/? ")
    yes_or_no = input("i can do delete now. yes or no? ")
    if yes_or_no == "yes":
        shutil.rmtree(input_path)
    sys.exit("success!")

elif input_mode == "move":
    input_path = input("input ./directory path/? ")
    output_path = input("output ./directory path/? ")

    move_file_list = glob.glob(input_path + "*")
    print(move_file_list)

    for item in move_file_list:
        shutil.move(item, output_path)
        print("success!")

else:
    sys.exit("good bye!")
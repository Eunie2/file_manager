import shutil
import glob

input_path = input("input? ")
output_path = input("output? ")

move_file_list = glob.glob(input_path + "*")
print(move_file_list)

for item in move_file_list:
    shutil.move(item, output_path)
    print("success")
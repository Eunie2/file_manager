import shutil
import glob
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument()
# print("Input and Output folder name?")
# input_path, output_path = input().split()

# help("Input : ./input_folder/", "Output: ./output_folder/")

input_path = input("input? ")
output_path = input("output? ")

print("input is a .. "+input_path)
print("output is a .. "+output_path)
# input_path = "./input/"
# output_path = "./output/"

move_file_list = glob.glob(input_path + "*")
print(move_file_list)

for item in move_file_list:
    shutil.move(item, output_path)
    print("success")
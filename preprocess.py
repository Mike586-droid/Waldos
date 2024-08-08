from customLib import *


# main function
def main(input_folder, dest_path):
    generate_windows(input_folder=input_folder, dest_path=dest_path)


source_path = "./labelled_data/"
dest_path = "./datasets/train/"
# generate windows:
main(input_folder=source_path, dest_path=dest_path)  # , test_file_name="14_1696"
#  * setting a test_file_name to a file name will not train and it will test that file name

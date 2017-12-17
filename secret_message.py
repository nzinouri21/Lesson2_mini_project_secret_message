import os

def rename_files():
    #step1: get file names from a folder
    file_list = os.listdir(r"C:\Users\nazanin\Desktop\HHIV\Intro to Programming Nanodegree\4-Create a Movie Website\Lesson2_mini_project_secret_message\alphabet2")
    print file_list
    saved_path = os.getcwd()
    print saved_path
    os.chdir(r"C:\Users\nazanin\Desktop\HHIV\Intro to Programming Nanodegree\4-Create a Movie Website\Lesson2_mini_project_secret_message\alphabet2")

    #step2: for each file, rename files
    for file_name in file_list:
        print "Old name " + file_name
        os.rename(file_name,file_name.translate(None, "0123456789"))
        print "New name " + file_name.translate(None, "0123456789")


rename_files()

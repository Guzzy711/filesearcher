import os
import os.path
curr_dir = os.getcwd() #get the current working directory
list_dir = os.listdir('.') #get a 'list' of files and dir's within the current directory
file_extensions = ['.doc','.pdf','docx','.dot','.dotm','.xls','.xlsx','.ppt','.pptx','.gif','.exe','.png','.psd','.txt','.html']
list_files = []
list_folders = []
def search_file():
    try:
        for file in list_dir: #loop through the files in the list
            for i in range(len(file_extensions)): #get the index
                if file.endswith(file_extensions[i]): #if that file ends with one of the extensions 
                    working_dir = os.path.abspath(os.getcwd())
                    list_files.append(working_dir + '/' + file) #append to list of files
            if os.path.isdir(file):
                    list_folders.append(file)
        print("Files containing stored extension: " + str(list_files))
        print("Folders: " + str(list_folders))
    except IOError:
        print("There was an error with " + SystemError)
search_file()

#make search into a function
    # Add parameter to specify which folder to search
#add function to go into folders
# change folder with os.chdir(path)



import os
import os.path
search_path = input("Enter a path to search (leave empty to search current): ")
file_extensions = ['.doc','.pdf','docx','.dot','.dotm','.xls','.xlsx','.ppt','.pptx','.gif','.exe','.png','.psd','.txt','.html']
list_files = []
list_folders = []
searched_folders = []
path = os.path.expanduser("~/Desktop")
def search_file():
    try:
        working_dir = os.path.abspath(os.getcwd())
        searched_folders.append(working_dir)
        list_dir = os.listdir('.') #get a 'list' of files and dir's within the current directory
        for file in list_dir: #loop through the files in the list
            for i in range(len(file_extensions)): #get the index
                if file.endswith(file_extensions[i]): #if that file ends with one of the extensions 
                    list_files.append(working_dir + '/' + file) #append to list of files
            if os.path.isdir(file):
                    list_folders.append(working_dir + '/' + file) #append found folders to a list
    except IOError:
        print("There was an error with " + SystemError)

def change_dir():
    try:
        for folder in list_folders:
            if folder in searched_folders: #if the folder has already been searched 
                break
            else:
                for i in range(len(list_folders)):
                    os.chdir(list_folders[i]) #change current working directory
                    search_file()
    except:
        print("There was an error with " + SystemError)
def check_search_path():
    if search_path and os.path.isdir(search_path):
        os.chdir(search_path)
    print("Searching: " + os.getcwd())
    search_file()    
check_search_path()
change_dir()
print("Files found: ")
print(*list_files,sep='\n')
save = input("Do you want to store these results in file? (Y/n): ")
print(path)
if save == "Y" or save == "y" or save == "yes":
    os.chdir(path)
    print("Results saved in: " + path + "/results.txt")
    with open('results.txt','w') as filehandle:
        for item in list_files:
            filehandle.write('%s\n' % item)
# Save all stores files in log file if the user wants to


import os
import os.path
curr_dir = os.getcwd() #get the current working directory
list_dir = os.listdir('.') #get a 'list' of files and dir's within the current directory
file_extensions = ['.doc','.pdf','docx','.dot','.dotm','.xls','.xlsx','.ppt','.pptx','.gif','.exe','.png','.psd','.txt','.html']
list_files = []
print(list_dir)
print(file_extensions)
try:
    for file in list_dir: #loop through the files in the list
        for i in range(len(file_extensions)): #get the index
            if file.endswith(file_extensions[i]): #if that file ends with one of the extensions
                print(file + ' ends with' + file_extensions[i]) 
                list_files.append(file) #append to list of files
            else:
                print(file + ' does not end with ' + file_extensions[i])
    print(list_files)
except IOError:
    print("There was an error with " + SystemError)

#add function to go into folders



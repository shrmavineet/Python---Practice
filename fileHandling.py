"""
- File Handling means Creating, Updating, Reading, Deleting (CURD) that we perform in a files.
- We have to use open() function to open a file in python.
- Now there are multiple modes to open the file.
:- 'r' --> Read(default) - file must exist.
:- 'w' --> Write - creates file or overwrites.
:- 'a' --> Append - adds to end of the file.
;- 'x' --> Creates a new file, fails if it exits
"""


##########################################################################################

# open("superman.txt")  #default 'r'
# open("superman.txt",'r')


##################################################

# r = open("fileCreateByHandeler.txt",'w')

# r.write("Hello this vineet and I am writing inside fileHandling file ")

# r.close()


###############################################################
r = open("fileCreateByHandeler.txt",'a')

r.write("Added some more extra line  by append method")

r.close()
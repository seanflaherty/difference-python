import sys
import os
import hashlib

if len(sys.argv) < 3:
    print ("You need to specify 2 directories")
    print (sys.argv[0]), "<directory 1> <directory 2>"
    sys.exit

# directory1 = sys.argv[1]
# directory2 = sys.argv[2]

# for directory in [directory1, directory2]:
#     if not os.access(directory, os.F_OK):
#         print (directory, "isn't a valid directory!")
#         sys.exit
#     print ("Directory", directory)
#     for item in os.walk(directory):
#         print (item)
#         print()

read_file = open(os.path.join("c:\\Users\\seanF\\development\\hello-python\\test", "test-file-1.txt"))
file_contents = list(read_file.readlines())
print ("Read in", len(file_contents), "lines from test.txt")
print ("First line reads:", file_contents[0])

write_file = open("c:\\Users\\seanF\\development\\hello-python\\test\\test-file-1.txt", "w")
write_file.write("This is the first line of the file\n")
write_file.writelines(
["and the second\n",
"and the third!\n"])
write_file.close()

#hashlib
# file_name = sys.argv[1]
# read_file = open(file_name)
# the_hash = hashlib.md5()
# for line in read_file.readlines():
#     the_hash.update(line)
# print (the_hash.hexdigest())

#dictionary
test_dictionary = {}
test_dictionary = {'one' : 1, 'two' : 2}
test_dictionary = {
    'list' :  [1,2,3],
    'dict' : {'one' : 1, 'two' : 2},
}
print (test_dictionary['list'])
del test_dictionary['list']
print(test_dictionary.keys())
print(test_dictionary.values())
print(test_dictionary.items())

# print ("Comparing:")
# print (directory1)
# print (directory2)
# print ()
#c:\Users\seanF\development\hello-python\test
#c:\Users\seanF\development\hello-python\hunt-wumpus
#python difference.py "c:\Users\seanF\development\hello-python\test" 
#python difference.py "c:\Users\seanF\development\hello-python\test" "c:\Users\seanF\development\hello-python\hunt-wumpus"
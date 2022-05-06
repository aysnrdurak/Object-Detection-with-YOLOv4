#you can use it for preparing test and train txt  files

import os

with open("output.txt", "w") as a:
    for path, subdirs, files in os.walk(r'/home/aysenur/Desktop/data'):
       for filename in files:
         f = os.path.join(path, filename)
         a.write(str(f) + os.linesep)

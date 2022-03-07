import time
import os
start_time = time.time()
# Old Extention
OldEX = ".mmm"
# New Extention
NewEX = ".jgw"
# dir or ls of files to be converted ex. dir *.mmm > folder.txt
# then edit txt file and remove .mmm on all lines
Filelist = "Test.txt"

files = []
with open(Filelist, encoding = 'utf8') as t:
    files = t.readlines()
t.close()
count = 0

for fileconvert in files:
    fil = files[count]
    fil = fil.strip("\n")
    filename = fil + OldEX
    FAST1 = "0.1"
    FAST2 = "0"
    FAST4 = "-0.1"

    lines = []
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()
    f.close()

    DataY = lines[2]
    splitting = DataY.split(' ')
    DataY = splitting[0]

    DataX = lines[3]
    splitting = DataX.split(' ')
    DataX = splitting[1]
    filename1 = fil + NewEX
    x = open(filename1, "w")
    x.writelines([FAST1, "\n", FAST2, "\n", FAST2, "\n", FAST4, "\n", DataY, "\n", DataX])
    x.close()
    count = (count + 1)


Ent_time = (time.time() - start_time)
print(Ent_time)

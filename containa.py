file1 = open("myfile.txt")
file2 = open("myfilenew.txt","w")
for line in file1:
    if 'a' in line:
        line = line.replace('a','')
    else:
        file2.write(line)
    file1.close()
    file2.close()
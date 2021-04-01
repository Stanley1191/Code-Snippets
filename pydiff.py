with open('file1.txt', 'r') as file1:
    with open('file2.txt', 'r') as file2:
        s_file1 = set(file1)
        s_file2 = set(file2)
        print("Total Items in file 1: " + str(len(s_file1)))
        print("Total Items in file 2: " + str(len(s_file2)))
        print("Output file should contain items: " + str(len(s_file1) -len(s_file2)))
        differences = s_file1.difference(s_file2)

differences.discard('\n')
count=0
with open('file_output.txt', 'w') as file_out:
    for line in differences:
        count+=1
        file_out.write(line)
        print(line, end="")

print("Total Items: " + str(count))
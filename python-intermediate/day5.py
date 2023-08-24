try:
    file = open("test.txt", "r")
except Exception as error:
    print(error)

count = 0

for i in file:
    if i:
        count += 1

file.close()
print(f"file contains {count} lines")


# alternate approach
# try:
#     with open("test.txt", "r") as file2:
#         lines = len(file2.readlines())
#         print(f"file contains {lines} lines")
# except Exception as err:
#     print(err)

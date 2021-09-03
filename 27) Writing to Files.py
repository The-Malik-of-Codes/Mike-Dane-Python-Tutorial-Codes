test_file = open("test.txt", "r")

print(test_file.read())
test_file.close()

test_file = open("test.txt", "a")

test_file.write("\nLina - Sudan")

test_file.close()

test_file = open("test.txt", "w")

test_file.write("\nLina - Sudan")

test_file.close()

test_file = open("test1.txt", "w")

test_file.write("\nLina - Sudan")

test_file.close()
test_file = open("test.txt", "r")

print(test_file.readable())
test_file.close()

test_file = open("test.txt", "r")

print(test_file.read())
test_file.close()

test_file = open("test.txt", "r")

print(test_file.readline())
test_file.close()

test_file = open("test.txt", "r")

print(test_file.readlines())
test_file.close()

test_file = open("test.txt", "r")

print(test_file.readlines()[1])
test_file.close()

test_file = open("test.txt", "r")
for test in test_file.readlines():
    print(test )
test_file.close()
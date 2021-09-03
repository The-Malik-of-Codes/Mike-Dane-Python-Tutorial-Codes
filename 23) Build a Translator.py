def translate(pharse):
    translation = ""
    for letter in pharse:
        if letter in "AEIOUaeiou":
            translation = translation + "s"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a pharse")))


def translate(pharse):
    translation = ""
    for letter in pharse:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "s"
            else:
                translation = translation + "s"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a pharse")))

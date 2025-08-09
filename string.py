class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def find_string_length(self):
        return len(self.text)

name = StringManipulator("Binay Raut")

char = name.find_character("R")
length = name.find_string_length()

print(f"The total characters are: {char}")
print(f"The length is: {length}")

class wordsCounter:
    def __init__(self, text):
        self.text = text

    def splitText(self):
        splitedWords = self.text.split()
        return splitedWords

    def countWords(self, splitedWords):
        totalWords = len(splitedWords)
        return totalWords


def main():
    fileData = open("F:\Week1\pythonProject\demo.txt", "r", encoding="UTF-8")
    read_file = fileData.read()
    print(read_file)
    fileData.close()
    countWords = read_file.split()
    totalWords = len(countWords)
    print(totalWords)
    fileData.close()

    readFile = wordsCounter(read_file)
    count_readFile = readFile.countWords(readFile.splitText())


if __name__ == "__main__":
    main()
class Sentence:
    def __init__(self):
        self.sentence = ""
        self.word_count = 0

    def user_sentence(self):
        self.sentence = input("Enter a sentence: ")

    def count_words(self):
        if not self.sentence.strip():
            self.word_count = 0
            return

        words = self.sentence.split()
        self.word_count = len(words)

    def display_word_count(self):
        """Displays the calculated word count."""
        print(f"The number of words in the sentence is: {self.word_count}")

if __name__ == "__main__":
    analyzer = Sentence()
    analyzer.user_sentence()
    analyzer.count_words()
    analyzer.display_word_count()
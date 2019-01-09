class Sentence:
    def __init__(self, text):
        self.sentence_text = text
        self.index = 0
        self.word_list = self.sentence_text.split()
        self.end = len(self.word_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.word_list):
            raise StopIteration
        else:
            word = self.word_list[self.index]
            self.index +=1
            return word

def my_sentence(text):
    for word in text.split():
        yield word

print("[+] Class Based Iterator")
sent1 = Sentence("Hello the grass is green")
for word in sent1:
    print(word)

print("[+] Function Based Generator")
sent2 = my_sentence("Good Morning Charlie Brown")

for word in sent2:
    print(word)



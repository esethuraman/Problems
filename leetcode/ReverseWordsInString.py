class ReverseWords:
    def reverse_words(self, s):
        return " ".join(s.strip().split()[::-1])
        # return (s[::-1])


obj = ReverseWords()
print(obj.reverse_words("  ela is a computer science engineer"))
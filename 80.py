#hg
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
n=input()
print(reverse_string_words(n))

def break_words(stuff):
    """This function will break up words for us."""
    return stuff.split(" ")

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    w = words.pop(0)
    print w

def print_last_word(words):
    w = words.pop(-1)
    print w

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = "The quick brown fox jumps over..."

print break_words(sentence)
print sort_sentence(sentence)

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)

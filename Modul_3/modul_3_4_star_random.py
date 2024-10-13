def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        word_lower = word.lower()
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)
    return same_words


# TEST
test1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
test2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# RESULT
print(test1)
print(test2)

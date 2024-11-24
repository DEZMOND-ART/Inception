class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            # Открытие файла для чтения
            file = open(file_name, 'r', encoding='utf-8')
            content = file.read().lower()
            for _ in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                content = content.replace(_, ' ')
            word = content.split()
            all_words[file_name] = word
            file.close()
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                result[name] = position
            else:
                result[name] = None
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


text = """
O Captain! My Captain!

O Captain! my Captain! our fearful trip is done,
The ship has weather’d every rack, the prize we sought is won,
The port is near, the bells I hear, the people all exulting,
While follow eyes the steady keel, the vessel grim and daring;
But O heart! heart! heart!
O the bleeding drops of red,
Where on the deck my Captain lies,
Fallen cold and dead.

O Captain! my Captain! rise up and hear the bells;
Rise up — for you the flag is flung — for you the bugle trills,
For you bouquets and ribbon’d wreaths — for you the shores a - crowding,
For you they call, the swaying mass, their eager faces turning;
Here Captain! dear father!
This arm beneath your head!
It is some dream that on the deck,
You’ve fallen cold and dead.

My Captain does not answer, his lips are pale and still,
My father does not feel my arm, he has no pulse nor will,
The ship is anchor’d safe and sound, its voyage closed and done,
From fearful trip the victor ship comes in with object won;
Exult O shores, and ring O bells!
But I with mournful tread,
Walk the deck my Captain lies,
Fallen cold and dead.

Walt Whitman
"""

with open(f'Walt Whitman - O Captain! My Captain!.txt', 'w', encoding='utf-8') as file:
    file.write(text)
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

dictionary = {'i': 'i', 'ɪ': '1', 'e': 'e', 'ɛ': '3', 'æ': '5', 'ʌ': '6', 'ə': '2',
              'ɚ': '', 'u': 'u', 'ʊ': 'o', 'o': '7', 'ɔ': '4', 'ɑ': 'a',
              'p': '-', 'b': 'b', 'd': 'd', 't': 't', 'k': 'k', 'g': 'g', 'f': 'f', 'v': 'v',
              'θ': '\'', 'ð': ';', 's': 's', 'z': 'z', 'ʃ': 'p', 'ʒ': 'q', 'h': 'h', 'ʧ': 'y',
              'ʤ': 'x', 'm': 'm', 'n': 'n', 'ŋ': 'c', 'l': 'l', 'r': 'r', 'w': 'w', 'j': 'j',
              '0': '9', '1': '[', '2': '8', '3': '\\', '4': ']', '5': '0', '6': '/', '7': '=',
              'ˈ': '$', 'ˌ': '$'}


def changeDiph(text):
    diphthongList = ['eɪ', 'oʊ', 'ɪə', 'ʊə', 'əʊ', 'ɑɪ', 'ɑʊ', 'ɔɪ']
    for i in range(8):
        text = text.replace(diphthongList[i], str(i))
    return text


def addSpace(text):
    text = " ".join(text)
    text = text + " "
    return text


def transLetter(letter, dic):
    if letter in dic:
        return dic[letter]
    else:
        return letter


def translate(text):
    text = addSpace(text)  # add space for dictionary to recognize
    translation = ''
    word = ''
    for c in text:
        if c != ' ':
            word = word + c
        else:
            translation = translation + ' ' + transLetter(word, dictionary)
            word = ''

    removeList = ['$ ', ' $', '  ', ' ', '**', '*']
    repList = ['', '', '*', '', ',', ',']
    for i in range(6):
        translation = translation.replace(removeList[i], repList[i])

    return translation  # remove extra space


def get(text):
    translation = translate(text)
    return translation


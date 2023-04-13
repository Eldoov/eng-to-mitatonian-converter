import eng_to_ipa as ipa
from PIL import Image, ImageFont, ImageDraw
import translator


def outputPic(text, fontSize=30):
    font = ImageFont.truetype("Mitatonian-Regular", fontSize, encoding='utf-8')
    img = Image.new("RGB", (1000, 50), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (0, 0, 0), font=font)
    img.show()


def translate(text):
    text = ipa.convert(text)
    print(text)
    new_text = translator.get(text)
    return new_text


def transFile(filePath):
    final_line = ''
    for line in open(filePath):
        new_line = translate(line)
        final_line = final_line + new_line 
    outputPic(final_line, 30)


def Start():
    while True:
        choice = None
        while choice is None:
            try:
                print("Welcome to English-to-Mitatonian converter.")
                print("Do you want to:")
                print("1. Translate a sentence. | 2. Translate a file. | 0. Quit.")
                choice = int(input())
            except ValueError:
                print("Invalid input!")
                continue
            if choice < 0 or choice > 2:
                print("Invalid input.")
                choice = None
                continue

        if choice == 1:
            print('Enter your sentence:')
            text = input()
            res = translate(text)
            outputPic(res)
            continue
        elif choice == 2:
            transFile('text.txt')
            continue
        elif choice == 0:
            quit()


#print(translate('hello world'))
Start()

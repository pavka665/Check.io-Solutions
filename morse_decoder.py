MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    words = code.split('   ')
    message = []
    for word in words:
        word_eng = ''
        for letter in word.split(' '):
            word_eng += MORSE[letter]
        message.append(word_eng)
    return ' '.join(message).capitalize()


print("Example:")
morse_decoder("... --- -- .   - . -..- -")
# print(morse_decoder("... --- -- .   - . -..- -"))

# assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
# assert (
#     morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
#     == "I was born in 1990"
# )
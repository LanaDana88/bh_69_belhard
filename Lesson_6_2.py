c
def func_code_morze(text):
    code_morze = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..',
        'E': '..', 'F': '..-.',
        'G': '--.', 'H': '....',
        'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-',
        'U': '..-', 'V': '...-',
        'W': '.--.', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
    }
    code_text = ''
    for letter in text:
        if letter.upper in code_morze:
            text += code_morze[letter.upper()] + ''
        else: code_text += ' '
    return code_text
print(func_code_morze('hello'))
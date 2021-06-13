from string import ascii_lowercase
import sys
import random

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y', 'aa', 'ae', 'ai', 'au', 'ay', 'ea', 'ee', 'ei', 'eu', 'ey', 'iu', 'oa', 'oe', 'oi', 'oo', 'ou', 'oy', 'ue']
SOUNDS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
FLOWS = ['', 'l', 'r', 'w']
HARD = ['ch', 'cj', 'ck', 'cz', 'fh', 'gh', 'gn' 'hm', 'hn', 'ks', 'kz', 'lh', 'ls', 'ph', 'pj', 'pk', 'pt'] + \
    ['sb', 'sc', 'sd', 'sf', 'sg', 'sh', 'sj', 'sk', 'sm', 'sn', 'sp', 'sq', 'st', 'sz', 'th', 'tch', 'tj', 'ts', 'vh', 'wh', 'wr', 'zh']
ENDS = ['', 'ng', 's']
NUMBERS = range(10)

# Repeatedly generate and write passwords to out_file
def write_passwords() -> None:
    out_file = './typable-passwords.txt'
    iterations = int(sys.argv[1])
    count = 0
    generator = pw_gen()
    with open(out_file, 'w') as file:
        while count < iterations:
            pw = next(generator, None)
            if (pw == None): break
            file.write(pw + '\n')

            # Increment pw count
            count += 1

# Generator for extra syllables
# Separated to reset pointers for duplicate sounds
def syllable_gen() -> str:
    # Password format - korean alpha sounds
    # Pref + Vowel + End?
    # Word = Pref || Pref? + Vowel + End? + (Pref + Vowel + End?)*
    # Hardcoded bc lazy
    for s in SOUNDS:
        for f in FLOWS:
            for v in VOWELS:
                for e in ENDS:
                    sound = s + f + v + e
                    yield sound 
    for h in HARD:
        for f in FLOWS:
            for v in VOWELS:
                for e in ENDS:
                    sound = h + f + v + e
                    yield sound

# Generate passwords of increasing length
def pw_gen() -> str:
    syllables = 1
    sound_gen = syllable_gen()
    while True:
        word = ''
        for _ in range(syllables):
            sound = next(sound_gen)
            if sound == None:
                break
            word += sound
        if sound == None:
            sound_gen = syllable_gen()
            syllables += 1
            continue
        yield word
    

if __name__ == '__main__':
    write_passwords()
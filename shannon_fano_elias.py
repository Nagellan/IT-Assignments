from huffman_coding import huffman_coding
from math import log2, ceil


def compute_cdf(dict):
    cdf = {}
    prev_val = 0

    for letter, value in dict.items():
        cdf[letter] = value + prev_val
        prev_val = cdf[letter]

    return cdf


def code(mids, probs):
    codes = {}

    for letter, value in mids.items():
        length = ceil(log2(1/probs[letter])) + 1
        fraction = int(str(value).split('.')[1])
        code = ''
        for _ in range(length):
            fraction = float('0.' + str(fraction))*2
            whole, fract = str(fraction).split('.')
            code += whole
            fraction = int(fract)
        codes[letter] = code

    return codes


def shannon_fano_elias_code(dict):
    cdf = compute_cdf(dict)
    midpoints = {letter: round(f - dict[letter]/2, 7) for letter, f in cdf.items()}
    codes = code(midpoints, dict)
    return codes


def shannon_fano_elias_decode(number, probs):
    bottom, top = 0, 1
    cdf = compute_cdf(probs)
    for c in str(number):
        diff = (top - bottom)/2
        if int(c) == 1:
            bottom += diff
        elif int(c) == 0:
            top -= diff

    result = ''
    for letter, f in cdf.items():
        if top <= f:
            result = letter
            break

    return result


dict1 = {'a': 0.01, 'b': 0.24, 'c': 0.05, 'd': 0.20, 'e': 0.47, 'f': 0.01, 'g': 0.02}
dict2 = {'a': 0.2, 'b': 0.15, 'c': 0.25, 'd': 0.05, 'e': 0.3, 'z': 0.05}
num_to_decode = '111110'

print("\nProbabilities: ", dict2)
print("Huffman code: ", huffman_coding(dict2))
print("Shannon-Fano-Elias code: ", shannon_fano_elias_code(dict2))
print("Shannon-Fano-Elias decode: ", num_to_decode, ' > ', shannon_fano_elias_decode(num_to_decode, dict2), end="\n\n")

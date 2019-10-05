from huffman_coding import huffman_coding
from shannon_fano_elias import compute_cdf


def arithmetic_coding(string, dict):
    bottom, top = 0, 1
    areas = {}
    props = compute_cdf(dict)
    for c in string:
        for letter, val in props.items():
            areas[letter] = (top - bottom)*val + bottom
        bottom, top = areas[c] - (top - bottom)*dict[c], areas[c]

    code = ''
    diff = 0
    frac_bot, frac_top = str(bottom).split('.')[1], str(top).split('.')[1]
    while diff == 0:
        frac_bot = float('0.' + str(frac_bot))*2
        frac_top = float('0.' + str(frac_top))*2
        bit_bot, frac_bot = str(frac_bot).split('.')
        bit_top, frac_top = str(frac_top).split('.')
        diff = int(bit_top) - int(bit_bot)
        code += bit_top

    return code


def bin_frac_to_dec(num):
    result = 0.0
    for i in range(0, len(num)):
        result += int(num[i])*(2**(-(i + 1)))
    return result


def arithmetic_decoding(number, length, dict):
    dec_num = bin_frac_to_dec(number)
    bottom, top = 0, 1
    msg = ''
    areas = {}
    props = compute_cdf(dict)
    for _ in range(length):
        for letter, val in props.items():
            areas[letter] = (top - bottom)*val + bottom
        c = ''
        for letter, val in areas.items():
            if dec_num < val:
                c = letter
                break
        msg += c
        bottom, top = areas[c] - (top - bottom)*dict[c], areas[c]
    return msg



dict2 = {'a': 0.2, 'b': 0.15, 'c': 0.25, 'd': 0.05, 'e': 0.3, 'z': 0.05}
string_to_code = "aabcdzzdbdaa"
num_to_decode = '00000010110101011100111001110100010111'

print("\nProbabilities: ", dict2)
print("Huffman code: ", huffman_coding(dict2))
print("Arithmetic coding: ", string_to_code, " > ", arithmetic_coding(string_to_code, dict2))
print("Arithmetic decoding: ", num_to_decode, ' > ', arithmetic_decoding(num_to_decode, len(string_to_code), dict2), end="\n\n")
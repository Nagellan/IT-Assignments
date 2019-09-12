def huffman_coding(dict):
    alpha = transformIntoPairs(dict)

    while len(alpha) > 1:
        alpha = sorted(alpha, key=lambda x: x[1], reverse=True)
        pair1 = alpha.pop()
        pair2 = alpha.pop()
        alpha.append(([pair2[0], pair1[0]], pair1[1] + pair2[1]))

    return decodeAlpha(alpha[0][0])


def decodeAlpha(alpha):
    result = {}
    def decodeAlphaRec(arr, num):
        if (type(arr[0]) is str):
            result[arr[0]] = num + '0'
        else:
            decodeAlphaRec(arr[0], num + '0')
        
        if (type(arr[1]) is str):
            result[arr[1]] = num + '1'
        else:
            decodeAlphaRec(arr[1], num + '1')
        
    decodeAlphaRec(alpha, '')

    return result

def transformIntoPairs(dict):
    result = []
    for letter, value in dict.items():
        result.append((letter, value))

    return result

dict = {'a': 0.01, 'b': 0.24, 'c': 0.05, 'd': 0.20, 'e': 0.47, 'f': 0.01, 'g': 0.02}
print(huffman_coding(dict))
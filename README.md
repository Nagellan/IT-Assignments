# Prefix-Code-Construction
Assignment for Information Theory subject at Innopolis University, 5th semester

## Shannon-Fano coding

### Task
Create a code tree according to Shannon and Fano, calculate total lengths.
Write a program which will create a Shannon-Fano code and will calculate total lengths for different set of symbols with different frequencies.

|     Symbol    | A  | B  | C  | D | E |
|---------------|----|----|----|---|---|
| **Frequency** | 24 | 12 | 10 | 8 | 8 |

### Solution
Python program ``shannon_fano.py`` constructing a prefix code based on a set of symbols and their frequencies in the text. It is suboptimal in the sense that it does not achieve the lowest possible expected code word length like Huffman coding.

### Input/Output
Dictinary containing symbol and its frequency in the key-value pairs.

**Example:** ``{'B': 12, 'D': 8, 'A': 24, 'C': 10, 'E': 8}``

## Huffman coding

### Task
Consider the following probability distribution:

|      Symbol     |   a  |   b  |   c  |   d  |   e  |   f  |   g  |
|-----------------|------|------|------|------|------|------|------|
| **Probability** | 0.01 | 0.24 | 0.05 | 0.20 | 0.47 | 0.01 | 0.02 |

* Create a code using Huffman algorithm;
* Find Expected Length for a Code;
* Implement Huffman Coding for different set of symbols with different probabilities.

### Solution
Python program ``huffman_coding.py`` constructing a type of optimal prefix code that is commonly used for lossless data compression. It achieves the lowest possible expected code word length.

### Input/Output
Dictinary containing symbol and its probability in the key-value pairs.

**Example:** ``{'a': 0.01, 'b': 0.24, 'c': 0.05, 'd': 0.20, 'e': 0.47, 'f': 0.01, 'g': 0.02}``

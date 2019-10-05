# IT-Assignments
Assignments for Information Theory subject at Innopolis University, 5th semester

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

## Shannon-Fano-Elias coding/decoding

### Task
Consider a source that generates letters with the probabilities as given in the table below:

|      Symbol     |   a  |   b  |   c  |   d  |   e  |
|-----------------|------|------|------|------|------|
| **Probability** | 0.25 | 0.25 | 0.20 | 0.15 | 0.15 |

* Use Shannon-Fano-Elias Coding to generate the code for any sequence;
* Write a code for encoding and decoding. Compare the codelength with the code generated from Huffman coding.

### Solution
Python program ``shannon_fano_elias.py`` which provides encoding and decoding functionalities for set of symbols, given their probabilities. One of the main features of Shannon-Fano-Elias coding is that, unlike Shannon-Fano coding, the probabilities of the source symbols do not have to be ordered non-increasingly. During the encoding operation it is impossible to predict how many symbols are left and what their probabilities are.

### Input/Output
* Dictinary containing symbol and its probability in the key-value pairs;
* Binary number to decode from.

**Example:** ``{'a': 0.25, 'b': 0.25, 'c': 0.20, 'd': 0.15, 'e': 0.15}, 11010``

## Arithmetic coding/decoding

### Task
Consider the following symbol with probability distributions as shown in the table below: 

|      Symbol     |   a  |   b  |   c  |   d  |   e  |   z  |
|-----------------|------|------|------|------|------|------|
| **Probability** | 0.20 | 0.15 | 0.25 | 0.05 | 0.30 | 0.05 |

* Find the Arithmetic code for the sequence of any given characters;
* Write a code for encoding and decoding;
* Compare the result with the Huffman code for the same sequence.

### Solution
Python program ``arithmetic_coding.py`` which provides encoding and decoding functionalities for string of characters, given their probabilities. String is represented using a fixed number of bits per character, as in the ASCII code. When a string is converted to arithmetic encoding, frequently used characters will be stored with fewer bits and not-so-frequently occurring characters will be stored with more bits, resulting in fewer bits used in total.

### Input/Output
* Dictinary containing symbol and its probability in the key-value pairs;
* String to encode;
* Binary number to decode from.

**Example:** ``{'a': 0.2, 'b': 0.15, 'c': 0.25, 'd': 0.05, 'e': 0.3, 'z': 0.05}, "aabcdzzdbdaa", 11010``

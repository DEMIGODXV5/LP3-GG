"""
Huffman Encoding is a lossless data compression algorithm.

It assigns variable-length binary codes to characters based on their frequencies.
- Frequently occurring characters receive shorter codes.
- Less frequently occurring characters receive longer codes.
The objective is to reduce the total number of bits required to represent a strin


"""

"""
heapq is a Python library used to implement a priority queue (Min Heap).
A Min Heap always gives us the element with the smallest priority first.
In Huffman Encoding, priority is based on character frequency.
"""
import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other): #This compares two nodes based on their frequencies.It tells Python's heap which node has a smaller frequency.
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code, huffman_codes):

    if root is None: #Check if node is empty .If there is no node, stop recursion.
        return

    # Leaf node .If code is not empty, use it.Otherwise, assign "0".
    if root.char is not None:
        huffman_codes[root.char] = code if code else "0"
        return

    generate_codes(root.left, code + "0", huffman_codes) #Whenever we move to the left child, append 0 to the code.
    generate_codes(root.right, code + "1", huffman_codes) #Whenever we move to the right child, append 1 to the code.


# Huffman Encoding
def huffman_encoding(text):

    if not text:
        print("Input text cannot be empty.")
        return

    # Calculate character frequencies
    frequency = {}

    for char in text: #This counts how many times each character appears.
        frequency[char] = frequency.get(char, 0) + 1  

    # Create priority queue
    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Build Huffman Tree
    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # Generate Huffman Codes
    root = heapq.heappop(heap)
    huffman_codes = {}

    generate_codes(root, "", huffman_codes)

    # Display results
    print("\nCharacter Frequencies and Huffman Codes:")

    for char, freq in frequency.items():
        display_char = "Space" if char == " " else char
        print(f"{display_char} : Frequency = {freq}, Code = {huffman_codes[char]}")

    # Encode input text
    encoded_text = ""

    for char in text:
        encoded_text += huffman_codes[char]

    print("\nOriginal Text:", text)
    print("Encoded Text:", encoded_text)


# Main Program
print("===== Huffman Encoding =====")

text = input("Enter a string: ")

huffman_encoding(text)
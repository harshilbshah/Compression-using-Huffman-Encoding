from huffman import HuffmanCoding
import sys
import os

path = "sample.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)

b = os.path.getsize('C:/Users/omtha/Downloads/Final Submission/Text File/sample.bin')
print("Compressed File Size: (in KB)", int(b/1000))

a = os.path.getsize('C:/Users/omtha/Downloads/Final Submission/Text File/sample_decompressed.txt')
print("Decompressed File Size: (in KB)", int(a/1000))

print("Compression Ratio :", (b/a)*100)

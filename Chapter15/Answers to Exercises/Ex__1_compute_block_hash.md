__Modern Computer Architecture and Organization Second Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 15, Exercise 1

Visit the blockchain explorer at https://bitaps.com and locate the list of last blocks on that page. Click on a block number and you will be presented with a display containing the hexadecimal listing of the block header along with its SHA-256 hash. Copy both items and write a program to determine if the hash provided is the correct hash of the header. Remember to perform SHA-256 twice to compute the header hash.

# Answer
See the python file [Ex__1_compute_block_hash.py](src/Ex__1_compute_block_hash.py) for the block header hashing code.

To execute the program, assuming **python** is installed and is in your path, execute the command **python Ex__1_compute_block_hash.py**

This is the output of a test run:
```
C:\>python Ex__1_compute_block_hash.py
Hashes match!
```
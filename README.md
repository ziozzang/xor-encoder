# xor-encoder
simple binary XOR encoder - to encryption/bypass tools

- this tool just encrypt/decrypt/scramble/unscramble with xor calculation.
- just simple. only to bypass or store security tools.

# How to use
- two version's results are just same. and binary level compatilbe each others.

## Python version
```
python encoder.py [input_file_name] [output_file_name] [keynumber(0~255):optional]
```

- slow. works with any python2/3

## C/C++ version

```
gcc -o encoder encoder.c -static
encoder [input_file_name] [output_file_name] [keynumber(0~255):optional]
```
- fast, but need compile.

# License

- MIT.
  - use at your own risk.
  - no guarantee.

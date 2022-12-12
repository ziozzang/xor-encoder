#!/usr/bin/python
# Compatible python 2/3 (any version)
# Code by Jioh L. Jung
import sys
import struct
buffer_size = 1024

def encoder(in_file, out_file, keys=0xA8):
   fi = open(in_file, 'rb', buffering=buffer_size)
   fo = open(out_file, 'wb', buffering=buffer_size)
   for i in bytearray(fi.read()):
       fo.write(struct.pack("B", i ^ keys))
   fi.close()
   fo.close()

if __name__ =="__main__":
  enc_key = 0xA8
  if len(sys.argv) >= 4:
    enc_key = int(sys.argv[3]) % 256
  if len(sys.argv) >= 3:
    encoder(sys.argv[1], sys.argv[2], enc_key)
  else:
    print('Simple Binary XOR encrypter/decrypter')
    print('> usage: %s [in_file] [out_file] [key_value: 0~255/optional]' % sys.argv[0])

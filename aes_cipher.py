import base64
from Crypto import Random
from Crypto.Cipher import AES
import string, random
import argparse
import sys
import getpass
import my_aes
class AESCipher(object):
    def __init__(self, key, block_size=32):
        self.bs = block_size
        if len(key) >= len(str(block_size)):
            self.key = key[:block_size]
        else:
            self.key = self._pad(key)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pss')
    parser.add_argument('--type', '-t', type=int, default=0)
    parser.add_argument('--length', '-l', type=int, default=16)
    args = parser.parse_args()

    if args.type == 0:
        print(''.join([random.choice(string.ascii_letters + string.digits) for i in range(args.length)]))
    elif args.type == 1:
        password = getpass.getpass('password> ')
        password2 = getpass.getpass('confirm> ')
        if password != password2:
            print('Passwords do not match.')
            sys.exit(0)
        enc = my_aes.encrypt(sys.stdin.buffer.read(), password)
        sys.stdout.buffer.write(enc)
    elif args.type == 2 :
        password = getpass.getpass('password> ')
        dec = my_aes.decrypt(sys.stdin.buffer.read(), password)
        sys.stdout.buffer.write(dec)

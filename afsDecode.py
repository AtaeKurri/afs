"""
Use this bit of program to decode *.afs files
Can be used from the terminal using : afsDecode.py the_file.afs
"""

import os, shutil, argparse
from cryptography.fernet import Fernet
key = Fernet(f"{open("key.txt", "r").read()}") # Replace the f_string to use your own fernet token

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
name = args.file
split = os.path.splitext(name)[0]

with open(name, 'rb') as enfile:
    enf = enfile.read()

defile = key.decrypt(enf)

with open(f"{split}.zip", 'wb') as decrypted_file:
    decrypted_file.write(defile)

shutil.unpack_archive(f'{split}.zip', format="zip")
os.remove(f"{split}.zip")

"""
Use this bit of program to encode *.afs files
Can be used from the terminal using : afsEncode.py the_file.afs
"""

import os, shutil, argparse
from cryptography.fernet import Fernet
key = Fernet(f"{open("key.txt", "r").read()}") # Replace the f_string to use your own fernet token

parser = argparse.ArgumentParser()
parser.add_argument("directory")
args = parser.parse_args()
name = args.directory
 
shutil.make_archive(name, "zip", base_dir=name)
with open(f"{name}.zip", 'rb') as f:
    value = f.read()

enfile = key.encrypt(value)

with open (f'{name}.afs', 'wb') as encrypted_file:
    encrypted_file.write(enfile)

os.remove(f'{name}.zip')
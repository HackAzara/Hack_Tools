# Encryptor Script

## Overview

Encryptor Script is a tool for encrypting and decrypting files using a password. It uses the Fernet symmetric key encryption algorithm to ensure the security of your sensitive data.

## Features

- **File Encryption:** Securely encrypt your files with a password.
- **File Decryption:** Decrypt previously encrypted files.

## Usage

### Requirements

- Python 3.x
- Required Python packages: `cryptography`, `termcolor`, `pyfiglet`

Install the required packages:

pip install cryptography termcolor pyfiglet

## How to Run

python3 your_script_name.py [file] [-s SALT_SIZE] [-e | -d]
[file]: Path to the file you want to encrypt or decrypt.
[-s SALT_SIZE]: Optional. Set the size of the salt for key derivation.
[-e]: Encrypt the file.
[-d]: Decrypt the file.

## Examples
## Encrypt a file:
python3 your_script_name.py your_file.txt -e

## Decrypt a file:
python3 your_script_name.py your_file.txt -d


Author
H4ckAzara

Email
h4ckazara@gmail.com

GitHub
https://github.com/HackAzara

Telegram
t.me/hackAzara

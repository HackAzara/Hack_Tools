import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64
import getpass
import os
from termcolor import colored
from pyfiglet import Figlet

def generate_salt(size=16):
    """Generate the salt used for key derivation, 
    `size` is the length of the salt to generate"""
    return secrets.token_bytes(size)

def derive_key(salt, password):
    """Derive the key from the `password` using the passed `salt`"""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def load_salt(file_path=None):
    # load salt from salt.salt file
    if file_path:
        salt_filename = os.path.join(os.path.dirname(file_path), "salt.salt")
    else:
        salt_filename = "salt.salt"
    return open(salt_filename, "rb").read()

def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True, file_path=None):
    """
    Generates a key from a `password` and the salt.
    If `load_existing_salt` is True, it'll load the salt from a file
    in the current directory called "salt.salt".
    If `save_salt` is True, then it will generate a new salt
    and save it to "salt.salt"
    """
    if load_existing_salt:
        # load existing salt
        salt = load_salt(file_path)
    elif save_salt:
        # generate new salt and save it
        salt = generate_salt(salt_size)
        salt_filename = os.path.join(os.path.dirname(file_path), "salt.salt")
        with open(salt_filename, "wb") as salt_file:
            salt_file.write(salt)
    # generate the key from the salt and the password
    derived_key = derive_key(salt, password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derived_key)

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully")

def main():
    big_figlet = Figlet(width=80, justify='center')
    big_text = big_figlet.renderText("Encryptor Script")
    print(colored(big_text, 'blue'))
    print(colored("                                            Information : ", 'red'))
    print(colored("                                            ToolName: Encryptor Script", 'red'))
    print(colored("                                            Author: H4ckAzara", 'red'))
    print(colored("                                            Copyright: H4ckAzara (2023)", 'red'))
    print(colored("                                            Email: h4ckazara@gmail.com", 'red'))
    print(colored("                                            Github : https://github.com/HackAzara", 'red'))
    print(colored("                                            Telegram : t.me/hackAzara", 'red'))
    print(colored("                                            Description: A tool for encrypting and decrypting files\n", 'red'))

    import argparse
    parser = argparse.ArgumentParser(description="File Encryptor Script with a Password")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated",
                        type=int)
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()
    file = args.file

    if args.encrypt:
        password = getpass.getpass("Enter the password for encryption: ")
    elif args.decrypt:
        password = getpass.getpass("Enter the password you used for encryption: ")

    if args.salt_size:
        key = generate_key(password, salt_size=args.salt_size, save_salt=True, file_path=file)
    else:
        key = generate_key(password, load_existing_salt=True, file_path=file)

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt(file, key)
    elif decrypt_:
        decrypt(file, key)
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")

if __name__ == "__main__":
    main()
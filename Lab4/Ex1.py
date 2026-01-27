from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encode_text = cipher_suite.encrypt(b"This is a really secret message")
print(f"Encoded text: {encode_text}")

# use the cryptography library to encode and ecode a message
decoded_text = cipher_suite.decrypt(encode_text)
print(f"Decoded text: {decoded_text.decode('utf-8')}")
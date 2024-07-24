from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization
import base64


def generate_wireguard_keypair():
    private_key = x25519.X25519PrivateKey.generate()
    public_key = private_key.public_key()
    private_key_base64 = base64.b64encode(private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )).decode('utf-8')
    public_key_base64 = base64.b64encode(public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )).decode('utf-8')
    return private_key_base64, public_key_base64


def write_keys_to_files(private_key, public_key, key_file):
    with open(key_file, 'w') as file:
        file.write(f"pri-key:\"{private_key}\"\npub-key:\"{public_key}\"")

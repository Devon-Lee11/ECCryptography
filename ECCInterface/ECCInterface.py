from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes


def generate_keys():
    private_key = ec.generate_private_key(ec.SECP384R1())
    public_key = private_key.public_key()
    return private_key, public_key


def sign(document, private_key):
    if not isinstance(document, str):
        return None
    document = bytes(document, 'utf-8')
    signature = private_key.sign(
        document,
        ec.ECDSA(hashes.SHA256())
    )
    return signature


def verify_data(document, signature, public_key):
    try:
        if not isinstance(document, str):
            return False
        document = bytes(document, 'utf-8')
        public_key.verify(
            signature,
            document,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False


from ECCInterface import generate_keys, sign, verify_data
from tests import test_sign_with_array_data, test_verify_data_with_array_data


def main():
    private_key, public_key = generate_keys()
    print(private_key, public_key)
    signed_document = sign('data.txt', private_key)
    print(signed_document)
    verified_data = verify_data('data.txt', signed_document, public_key)
    print(verified_data)
    test_sign_with_array_data()
    test_verify_data_with_array_data()


if __name__ == "__main__":
    main()

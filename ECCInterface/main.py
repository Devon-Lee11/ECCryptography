from ECCInterface import generate_keys
from tests import test_sign_with_array_data, test_verify_data_with_array_data, \
    test_verify_data_with_file, test_sign_with_file


def main():
    private_key, public_key = generate_keys()
    print(private_key, public_key)
    test_verify_data_with_file()
    test_sign_with_file()
    test_sign_with_array_data()
    test_verify_data_with_array_data()


if __name__ == "__main__":
    main()

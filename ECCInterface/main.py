from tests import test_sign_with_array_data, test_verify_data_with_array_data, \
    test_verify_data_with_file, test_sign_with_file, test_keys_were_generated, \
    test_sign_with_string


def main():
    test_keys_were_generated()
    test_verify_data_with_file()
    test_sign_with_file()
    test_sign_with_array_data()
    test_verify_data_with_array_data()
    test_sign_with_string()


if __name__ == "__main__":
    main()

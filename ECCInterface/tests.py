from ECCInterface import generate_keys, sign, verify_data
private_key, public_key = generate_keys()
test_array = [1, 2, 3]
signed_document = sign('data.txt', private_key)


def test_sign_with_array_data():
    print('expected None')
    print(sign(test_array, private_key))


def test_verify_data_with_array_data():
    print('expected false')
    print(sign(test_array, public_key))


def test_sign_with_file():
    print(signed_document)


def test_verify_data_with_file():
    print(verify_data('data.txt', signed_document, public_key))


def test_keys_were_generated():
    print(public_key, private_key)

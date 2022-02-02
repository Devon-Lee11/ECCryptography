from RsaInterface import generate_keys, sign, verify_data
private_key, public_key = generate_keys()
test_array = [1, 2, 3]


def test_sign_with_array_data():
    print('expected false')
    print(sign(test_array, private_key))


def test_verify_data_with_array_data():
    print('expected false')
    print(sign(test_array, public_key))

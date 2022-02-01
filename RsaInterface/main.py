from RsaInterface import generate_keys, sign, verify_data


def main():
    private_key, public_key = generate_keys()
    print(private_key, public_key)
    signed_document = sign('data.txt', private_key)
    print(signed_document)
    verified_data = verify_data('data.txt', signed_document, public_key)
    print(verified_data)


if __name__ == "__main__":
    main()

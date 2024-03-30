from cryptography.fernet import Fernet


def main() -> None:
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())


if __name__ == "__main__":
    main()

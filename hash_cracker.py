import hashlib

def crack_hash(target_hash, hash_type, wordlist_path):

    print(f"\nAttempting to crack: {target_hash}")

    try:

        with open(
            wordlist_path,
            'r',
            encoding='utf-8',
            errors='ignore'
        ) as f:

            for count, line in enumerate(f,1):

                word = line.strip()

                if hash_type == 'md5':

                    attempt = hashlib.md5(
                        word.encode()
                    ).hexdigest()

                elif hash_type == 'sha1':

                    attempt = hashlib.sha1(
                        word.encode()
                    ).hexdigest()

                elif hash_type == 'sha256':

                    attempt = hashlib.sha256(
                        word.encode()
                    ).hexdigest()

                else:

                    print(
                        "Unsupported hash type"
                    )
                    return

                if attempt == target_hash:

                    print(
                        f"Password found: {word}"
                    )

                    print(
                        f"Found after {count} attempts"
                    )

                    return word

        print("Password not found.")

    except FileNotFoundError:

        print(
            f"Wordlist not found: {wordlist_path}"
        )
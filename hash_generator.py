import hashlib

def generate_hash(text):
    print(f"\n Hashes for: '{text}'")
    print(f" MD5    :{hashlib.md5(text.encode()).hexdigest()}")
    print(f" SHA-1  :{hashlib.sha1(text.encode()).hexdigest()}")
    print(f" SHA-256:{hashlib.sha256(text.encode()).hexdigest()}")
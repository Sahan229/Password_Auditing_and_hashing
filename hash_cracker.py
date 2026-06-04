import hashlib

def crack_hash(target_hash, hash_type, wordlist_path):
    print(f"\n Attemting to crack: {target_hash}")
    print(f"  hash type : {hash_type.upper()}")
    print(f"  wordlist  : {wordlist_path}")
    print(f"  searching...\n")
    try:
	with open(wordlist_path, 'r',encoding='utf-8',errors='ignore') as f:
	    for count, line in enumerate(f,1):
	        word = line.strip()
	        if hash_type =='md5':
	            attempt = hashlib.md5(word.encode()).hexdigest()

		elif hash_type == 'sha256':
	            attempt = hashlib.sha256(word.encode()).hexdigest()
             
                elif hash_type == 'sha1'
                    attempt = hashlib.sha1(word.encode).hexdigest()

	        else:
                    print("Unsupproted hash type. use: md5, sha1, sha256")
                return None

	        if attempt == target_hash:
	                print(f"Cracked password is the: {word}")
                    print(f"Found after {count} attempts")
                    return word
         
     print("Password not found in wordlist.")
 except FileNotFoundError:
     print("wordlist file not found: {wordlist_path}")
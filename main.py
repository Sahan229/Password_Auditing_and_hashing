from password_strength import check_password_strength
from hash_generator import generate_hash
from hash_cracker import crack_hash

def show_menu():
    print("\n" + "="*45)
    print("  PASSWORD AUDITING & HASH CRACK TOOL")
    print("="*45)
    print("  [1] Check Password Strength")
    print("  [2] Generate Hash of a Password")
    print("  [3] Crack a Hash (Wordlist Attack)")
    print("  [4] Exit")
    print("="*45)
 
def main():
    while True:
        show_menu()
        choice = input(" Enter your choice (1-4): ").strip()
 
        if choice == '1':
            pw = input("\n Enter password to check: ")
            check_password_strength(pw)
 
        elif choice == '2':
            text = input("\n Enter text to hash: ")
            generate_hash(text)
 
        elif choice == '3':
            target = input("\n Enter the hash to crack: ").strip()
            htype  = input("   Hash type (md5 / sha1 / sha256): ").strip().lower()
            wlist  = input("   Wordlist path (e.g. /usr/share/wordlists/rockyou.txt): ").strip()
            crack_hash(target, htype, wlist)
 
        elif choice == '4':
            print("\n Goodbye! Keep learning cybersecurity!\n")
            break
 
        else:
            print("  Invalid choice. Please enter 1, 2, 3 or 4.")
 
if __name__ == "__main__":
    main()
 
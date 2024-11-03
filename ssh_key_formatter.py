def format_key(raw_key, key_type):
    # Determine header and footer based on key type
    if key_type == "OpenSSH":
        header = "-----BEGIN OPENSSH PRIVATE KEY-----"
        footer = "-----END OPENSSH PRIVATE KEY-----"
    elif key_type == "RSA":
        header = "-----BEGIN RSA PRIVATE KEY-----"
        footer = "-----END RSA PRIVATE KEY-----"
    else:
        raise ValueError("Invalid key type provided.")

    # Define unwanted symbols to be removed from the raw key
    unwanted_symbols = [
        "\"", "'", ",", ";", ":", "|", "\\", "!", "@", "#", "$", "%", "^", 
        "&", "*", "(", ")", "[", "]", "{", "}", "<", ">", "?",
    ]

    # Remove unwanted symbols from the raw key
    for symbol in unwanted_symbols:
        raw_key = raw_key.replace(symbol, "")
    
    # Clean the key content by removing headers, footers, and whitespace
    key_content = raw_key.replace(header, "").replace(footer, "").replace("\n", "").replace(" ", "").strip()
    
    # Format key content into lines of 64 characters
    formatted_key_content = "\n".join([key_content[i:i+64] for i in range(0, len(key_content), 64)])
    
    # Return the complete formatted key with header and footer
    return f"{header}\n{formatted_key_content}\n{footer}\n"


def read_key_from_file(filename):
    # Attempt to read the key from a specified file
    try:
        with open(filename, 'r') as key_file:
            return key_file.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def main():
    # Prompt user for key type
    print("Which type of key would you like to format?")
    print("1. OpenSSH Private Key")
    print("2. RSA Private Key")
    choice = input("Enter your choice (1 or 2): ").strip()

    # Set key type based on user choice
    if choice == "1":
        key_type = "OpenSSH"
    elif choice == "2":
        key_type = "RSA"
    else:
        print("Invalid choice. Exiting.")
        return

    # Ask if the user wants to read the raw key from a file
    if input("Do you want to read the raw key from a file? (y/n): ").lower() == 'y':
        filename = input("Enter the filename (e.g., key.txt): ")
        raw_key = read_key_from_file(filename)
        if raw_key is None:
            return
    else:
        raw_key = input(f"Enter your raw {key_type} key (whatever it looks like): ")
    
    # Format the raw key and handle potential errors
    try:
        formatted_key = format_key(raw_key, key_type)
    except ValueError as e:
        print(e)
        return

    # Output the formatted key
    print(f"\nFormatted {key_type} Key:\n")
    print(formatted_key)

    # Ask if the user wants to save the formatted key to a file
    if input("Do you want to save the formatted key to a file? (y/n): ").lower() == 'y':
        filename = input("Enter the filename (e.g., id_rsa): ")
        try:
            with open(filename, 'w') as key_file:
                key_file.write(formatted_key)
            print(f"\nKey saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()

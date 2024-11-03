def format_key(raw_key, key_type):
    """Format the given raw key based on the specified key type."""
    # Determine the header and footer based on key type
    if key_type == "OpenSSH":
        header = "-----BEGIN OPENSSH PRIVATE KEY-----"
        footer = "-----END OPENSSH PRIVATE KEY-----"
    elif key_type == "RSA":
        header = "-----BEGIN RSA PRIVATE KEY-----"
        footer = "-----END RSA PRIVATE KEY-----"
    else:
        raise ValueError("Invalid key type provided.")

    # Clean input: Remove unwanted symbols, newlines, spaces, and headers/footers
    unwanted_symbols = [
        "\"", "'", ",", ";", ":", "|", "\\", "/", "!", "@", "#", "$", "%", "^", 
        "&", "*", "(", ")", "[", "]", "{", "}", "<", ">", "?", "="
    ]
    
    for symbol in unwanted_symbols:
        raw_key = raw_key.replace(symbol, "")
    
    # Remove headers and footers, and trim the key content
    key_content = raw_key.replace(header, "").replace(footer, "").replace("\n", "").replace(" ", "").strip()
    
    # Format the key content into 64-character lines
    formatted_key_content = "\n".join([key_content[i:i+64] for i in range(0, len(key_content), 64)])
    
    # Assemble the formatted key with the header and footer
    return f"{header}\n{formatted_key_content}\n{footer}\n"


def read_key_from_file(filename):
    """Read the raw key from a specified file."""
    try:
        with open(filename, 'r') as key_file:
            return key_file.read()  # Return the content of the file
    except FileNotFoundError:
        print(f"File {filename} not found.")  # Inform the user if the file is not found
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")  # Handle other potential errors
        return None


def main():
    """Main function to execute the key formatting process."""
    print("Which type of key would you like to format?")
    print("1. OpenSSH Private Key")
    print("2. RSA Private Key")
    choice = input("Enter your choice (1 or 2): ").strip()

    # Determine the type of key based on user choice
    if choice == "1":
        key_type = "OpenSSH"
    elif choice == "2":
        key_type = "RSA"
    else:
        print("Invalid choice. Exiting.")
        return

    # Read raw key from file or user input
    if input("Do you want to read the raw key from a file? (y/n): ").lower() == 'y':
        filename = input("Enter the filename (e.g., key.txt): ")
        raw_key = read_key_from_file(filename)  # Read key from the specified file
        if raw_key is None:
            return  # Exit if there was an error reading the file
    else:
        raw_key = input(f"Enter your raw {key_type} key (whatever it looks like): ")
    
    # Format the key using the specified function
    try:
        formatted_key = format_key(raw_key, key_type)
    except ValueError as e:
        print(e)  # Print error message if invalid key type
        return

    # Output the formatted key
    print(f"\nFormatted {key_type} Key:\n")
    print(formatted_key)

    # Optionally save the formatted key to a file
    if input("Do you want to save the formatted key to a file? (y/n): ").lower() == 'y':
        filename = input("Enter the filename (e.g., id_rsa): ")
        try:
            with open(filename, 'w') as key_file:
                key_file.write(formatted_key)  # Write the formatted key to the specified file
            print(f"\nKey saved to {filename}")  # Confirm that the key has been saved
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")  # Handle errors during saving

if __name__ == "__main__":
    main()  # Run the main function

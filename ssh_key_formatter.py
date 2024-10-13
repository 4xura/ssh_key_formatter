def format_openssh_key(raw_key):
    # Define the header and footer for the OpenSSH key format
    header = "-----BEGIN OPENSSH PRIVATE KEY-----"
    footer = "-----END OPENSSH PRIVATE KEY-----"
    
    # Clean input: Remove unwanted symbols, newlines, spaces, and header/footer
    unwanted_symbols = ["\"", "\'", ",", ";", ":", "|", "\\", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "<", ">", "?", "="]
    for symbol in unwanted_symbols:
        raw_key = raw_key.replace(symbol, "")
    
    # Further clean to remove newlines, spaces, and headers/footers
    key_content = raw_key.replace(header, "").replace(footer, "").replace("\n", "").replace(" ", "").strip()
    
    # Split into 64-character lines
    formatted_key_content = "\n".join([key_content[i:i+64] for i in range(0, len(key_content), 64)])
    
    # Reassemble the key with the header and footer, and add necessary line breaks
    formatted_key = f"{header}\n{formatted_key_content}\n{footer}\n"
    
    return formatted_key

def format_rsa_key(raw_key):
    # Define the header and footer for the RSA key format
    header = "-----BEGIN RSA PRIVATE KEY-----"
    footer = "-----END RSA PRIVATE KEY-----"
    
    # Clean input: Remove unwanted symbols, newlines, spaces, and header/footer
    unwanted_symbols = ["\"", "\'", ",", ";", ":", "|", "\\", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "<", ">", "?", "="]
    for symbol in unwanted_symbols:
        raw_key = raw_key.replace(symbol, "")
    
    # Further clean to remove newlines, spaces, and headers/footers
    key_content = raw_key.replace(header, "").replace(footer, "").replace("\n", "").replace(" ", "").strip()
    
    # Split into 64-character lines
    formatted_key_content = "\n".join([key_content[i:i+64] for i in range(0, len(key_content), 64)])
    
    # Reassemble the key with the header and footer, and add necessary line breaks
    formatted_key = f"{header}\n{formatted_key_content}\n{footer}\n"
    
    return formatted_key

def main():
    # Ask the user which type of key they want to format
    print("Which type of key would you like to format?")
    print("1. OpenSSH Private Key")
    print("2. RSA Private Key")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        key_type = "OpenSSH"
        format_function = format_openssh_key
    elif choice == "2":
        key_type = "RSA"
        format_function = format_rsa_key
    else:
        print("Invalid choice. Exiting.")
        return

    # Input raw key
    raw_key = input(f"Enter your raw {key_type} key (whatever it looks like): ")
    
    # Format the key using the selected function
    formatted_key = format_function(raw_key)
    
    # Output the formatted key
    print(f"\nFormatted {key_type} Key:\n")
    print(formatted_key)
    
    # Optionally save the key to a file
    save_to_file = input("Do you want to save the formatted key to a file? (y/n): ").lower()
    if save_to_file == 'y':
        filename = input("Enter the filename (e.g., id_rsa): ")
        with open(filename, 'w') as key_file:
            key_file.write(formatted_key)
        print(f"\nKey saved to {filename}")

if __name__ == "__main__":
    main()

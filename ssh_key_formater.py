def format_openssh_key(raw_key):
    # Define the header and footer for the OpenSSH key format
    header = "-----BEGIN OPENSSH PRIVATE KEY-----"
    footer = "-----END OPENSSH PRIVATE KEY-----"
    
    # Remove raw header and footer if they exist
    key_content = raw_key.replace(header, "").replace(footer, "").strip()
    
    # Split the key content into 64-character lines
    formatted_key_content = "\n".join([key_content[i:i+64] for i in range(0, len(key_content), 64)])
    
    # Reassemble the key with the header and footer
    formatted_key = f"{header}\n{formatted_key_content}\n{footer}"
    
    return formatted_key

def main():
    # Input raw key
    raw_key = input("Enter your one-line OpenSSH key: ")
    
    # Format the key
    formatted_key = format_openssh_key(raw_key)
    
    # Output the formatted key
    print("\nFormatted OpenSSH Key:\n")
    print(formatted_key)
    
    # Optionally save the key to a file for future use
    save_to_file = input("Do you want to save the formatted key to a file? (y/n): ").lower()
    if save_to_file == 'y':
        filename = input("Enter the filename (e.g., id_rsa): ")
        with open(filename, 'w') as key_file:
            key_file.write(formatted_key)
        print(f"\nKey saved to {filename}")

if __name__ == "__main__":
    main()

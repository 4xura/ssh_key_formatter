def format_openssh_key(raw_key):
    # Define the header and footer for the OpenSSH key format
    header = "-----BEGIN OPENSSH PRIVATE KEY-----"
    footer = "-----END OPENSSH PRIVATE KEY-----"
    
    # Clean input: Remove any newlines, spaces, and header/footer
    key_content = raw_key.replace(header, "").replace(footer, "").replace("\n", "").replace(" ", "").strip()
    
    # Split into 64-character lines
    formatted_key_content = "\n".join([key_content[i:i+64] for i in range(0, len(key_content), 64)])
    
    # Reassemble the key with the header and footer, and add necessary line breaks
    formatted_key = f"{header}\n{formatted_key_content}\n{footer}\n"
    
    return formatted_key

def main():
    # Input raw key
    raw_key = input("Enter your raw OpenSSH key (one-line or improperly formatted): ")
    
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

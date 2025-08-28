def file_read_write():
    try:
        # Ask user for input filename
        input_filename = input("Enter the name of the file to read: ").strip()
        
        # Try opening and reading the file
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = "modified_" + input_filename
        
        # Write modified content into new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"✅ File processed successfully! Modified content saved as {output_filename}")
    
    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write this file.")
    
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
file_read_write()

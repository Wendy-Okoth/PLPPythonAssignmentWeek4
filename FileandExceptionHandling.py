# File Handling and Exception Handling Assignment
# Author: Your Name
# Date: YYYY-MM-DD

def file_read_write():
    try:
        # Ask the user for the filename to read
        input_file = input("Enter the filename to read: ")

        # Open the file for reading
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the file content (example: make all text uppercase)
        modified_content = content.upper()

        # Ask for the output file name
        output_file = input("Enter the new filename to write modified content: ")

        # Write modified content to the new file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ File has been successfully read from '{input_file}' and written to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read or write this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    file_read_write()

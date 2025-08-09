# 📂 File Handling and Exception Handling Assignment

## 📌 Overview
This project demonstrates **file handling** and **exception handling** in Python.  
It reads a file provided by the user, modifies its content, and writes the result to a new file.  
The program also includes **error handling** to manage common file-related issues gracefully.

---

## 🛠 Features
- Reads the content of a file
- Converts the content to **uppercase**
- Writes the modified content to a **new file**
- Handles:
  - Missing files (`FileNotFoundError`)
  - Permission issues (`PermissionError`)
  - Unexpected errors

---

## 💻 How It Works
1. The user is prompted to enter:
   - The **input filename** (to read from)
   - The **output filename** (to write to)
2. The program reads the input file and modifies its content.
3. The modified content is written to the output file.
4. If errors occur (e.g., file not found), the program prints an appropriate error message.

---

## 📜 Code
```python
def read_and_modify_file(input_filename, output_filename):
    """
    Reads the content of a file, modifies it, and writes it to a new file.
    The modification here is converting text to uppercase.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ File '{input_filename}' successfully read and modified into '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read '{input_filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Main program
if __name__ == "__main__":
    input_file = input("Enter the name of the file to read: ")
    output_file = input("Enter the name of the new file to write: ")
    read_and_modify_file(input_file, output_file)
▶️ How to Run
Save the Python file as file_handler.py.

Place it in the same directory as your input file.

Open your terminal or command prompt.

Run:
python file_handler.py
Enter the input filename and output filename when prompted.


Example
Input file (sample.txt):
Hello World
Python is fun!

Output file (output.txt):
HELLO WORLD
PYTHON IS FUN!


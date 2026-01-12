try:
    filename = input("Enter the filename to read: ")

    # Try to open and read file
    with open(filename, "r") as file:
        content = file.read()

    # Modify content
    modified_content = content.upper()

    # Write to new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as file:
        file.write(modified_content)

    print("🎉 Success!")
    print(f"New file created: {new_filename}")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")

except PermissionError:
    print("❌ Error: You don't have permission to read this file.")

except Exception as e:
    print("❌ Unexpected error:", e)

#Read files
#Write new files
# Modify content
# Handle exceptions
#Build robust Python programs

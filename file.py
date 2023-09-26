source_file_path = 'source.txt'
destination_file_path = 'destination.txt'

try:
  
    with open(source_file_path, 'r') as source_file:
        
        file_contents = source_file.read()

    
    with open(destination_file_path, 'w') as destination_file:
        # Write the contents to the destination file
        destination_file.write(file_contents)

    print(f"Contents copied from '{source_file_path}' to '{destination_file_path}' successfully.")
except FileNotFoundError:
    print(f"Error: The source file '{source_file_path}' does not exist.")
except IOError:
    print(f"Error: Unable to write to the destination file '{destination_file_path}'.")

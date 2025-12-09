import os

def list_directory_contents(directory_path):
    try:
        # Retrieve the list of entries in the specified directory
        entries = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '/path/to/your/directory'
list_directory_contents(directory_path)

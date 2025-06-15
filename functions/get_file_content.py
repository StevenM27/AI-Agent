import os

def get_file_content(working_directory, file_path):
    try:
        combined_dir = os.path.abspath(os.path.join(working_directory, file_path))

        # Check to see if the file provided is in the working directory.
        # Also checks to see that the file_path var is a file.
        if not combined_dir.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(combined_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'


        MAX_CHARS = 10000
        with open(combined_dir, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS]
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return file_content_string
    except Exception as err:
        return f"Error: {err}"

import os

def write_file(working_directory, file_path, content):
    try:
        combined_dir = os.path.abspath(os.path.join(working_directory, file_path))

        split_dir = combined_dir.split("/")
        new_combined_dir = "/".join(split_dir[:-1])
        
        # Check to see if the file_path provided is in the working directory.
        # Also checks to see that the file_path var is a file. If not, a new file by
        # that name gets created.
        if not combined_dir.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif not os.path.exists(new_combined_dir):
            os.makedirs(new_combined_dir)
        
        with open(combined_dir, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as err:
        return f"Error: {err}"
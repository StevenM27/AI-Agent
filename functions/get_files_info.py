import os

def get_files_info(working_directory, directory=None):

    try:
        combined_dir = os.path.abspath(os.path.join(working_directory, directory))

        # Check to see if the directory provided is in the working directory.
        # Also checks to see that the directory var is a directory
        if not combined_dir.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(combined_dir):
            return f'Error: "{directory}" is not a directory'

        dir_list = os.listdir(combined_dir)
        dir_list_string = []
        for item in dir_list:
            path = os.path.join(combined_dir, item)
            result = f"- {item}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}"
            dir_list_string.append(result)

        return "\n".join(dir_list_string)
    except Exception as err:
        return f"Error: {err}"
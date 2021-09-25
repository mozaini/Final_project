import os

def new_folder(folder_name):
    """
    this funcation creates a new directory in the currnet running directory when it's called
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
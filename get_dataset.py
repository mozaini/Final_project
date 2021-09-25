import requests as re
import os
def get_dataset(url, file_name):
    """
        The following function will download the dataset from the internet using requests library and
        save it in the 'dataset' directory inside the current running direcroty.

        The function will take url and the file name including its format `csv` for example

        """

    response = re.get(url)
    with open(os.path.join('dataset', file_name), mode='wb') as file:
        file.write(response.content)
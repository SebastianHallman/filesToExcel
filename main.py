import os
from datetime import datetime
import pandas as pd

files = os.listdir('files')
file_dictionary = {}
file_dictionary['File name'] = []
file_dictionary['Creation date'] = []

for file in files:
    creation_date = datetime.fromtimestamp(os.path.getctime('files/' + file))
    file_name = file.split('.')[0]
    file_dictionary['File name'].append(file_name)
    file_dictionary['Creation date'].append(creation_date)

data = pd.DataFrame(file_dictionary)
data.to_csv('list_of_files.csv')

    
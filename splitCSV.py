''' Function: main is a method that splits the xlxs file to multiple CSVs based on provided row size.
    Variables: 
    1. <filename> - filepath/name of a Excel file. Eg: '~/Desktop/test.xlsx' 
        Or if file is in same path as this script simply 'test.xlsx'
    2. <rowsize> - size of a row you want to split the Excel file to create multiple CSVs.  
    3. <output_file_prefix> - output file prefix. Eg. If you provide 'result' then file name will be result_1.csv, 
        result_2.csv ... 
    
    Steps:
    1. Load Excel file and create a dataframe using python library pandas
    2. Split the dataframe to list/array of dataframes based on the row size you provided
    3. Loop through the list to create multiple CSVs. 
    
    All the CSVs are saved inside Output folder.
'''

import sys
import os  
import time

try:
    import pandas as pd   # importing pandas module 
except ImportError:
    print ('Trying to Install required module: Pandas\n')
    os.system('python -m pip install pandas')

try:
    import progressbar  # importing pandas module 
except ImportError:
    print ('Trying to Install required module: import progressbar\n')
    os.system('python -m pip install import progressbar2')

def main(filename, rowsize, output_file_prefix):
    # Output directory name
    output_dir = 'Output'

    # Loading the Excel file as a dataframe
    print('Reading {}..'.format(filename))
    df = pd.read_excel(filename, sheet_name=None)
    df = df['data']
    
    # Splitting the dataframe in to list of dataframes based on provided row size
    list_of_dfs = [df.loc[i:i+int(rowsize)-1,:] for i in range(0, len(df),int(rowsize))]
    
    # Create an output folder if doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    bar = progressbar.ProgressBar(max_value=len(list_of_dfs))
    print('Creating CSVs...')
    # Loop through list of dataframes and output each CSVs
    for index, df in enumerate(list_of_dfs):
        df.to_csv("{}/{}_{}.csv".format(output_dir, output_file_prefix, index))
        time.sleep(0.1)
        bar.update(index+1)
    print(' Check Output directory for CSV files.')    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

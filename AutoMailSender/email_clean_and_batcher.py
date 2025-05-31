# 1. email_clean_and_batcher.py
import subprocess
import sys
import warnings
import pandas as pd

# Ignore warnings from openpyxl
warnings.simplefilter('ignore', UserWarning)

print('Data cleaner started! About to look for duplicate email address...')
df = pd.read_excel('skolenhetsadresser_20250413_030018.xlsx', sheet_name='Gymnasieskola')
print(f'Number of rows: {df.shape[0]}, number of columns: {df.shape[1]}')
# Count unique email address
unique_email_count = df['EPOST'].nunique()
print(f'Number of unique email-addresser: {unique_email_count}')
if unique_email_count == df.shape[0]:
    print('All address are unique, no cleaning required')
    sys.exit(0)

# Use unique emails only
df_unique = df.drop_duplicates(subset='EPOST', keep='first')

# Show new data frame
print(f'Creating new data frame by dropping duplicates. New size: {df_unique.shape}')

# Sort the dataframe by email address in ascending order
df_unique = df_unique.sort_values(by='EPOST', ascending=True)

# Export unique mail address
print('Exporting new data to gymnasieskolor_unika_email.xlsx...')
df_unique.to_excel('gymnasieskolor_unika_email.xlsx', index=False)

print('Done!✅')


# Check if 'batches' directory exists, then run batchify.py

subprocess.run(['python', 'batchify.py'], check=True)

sys.exit(0)


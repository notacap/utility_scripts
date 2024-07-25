import pandas as pd
import os

# File paths
input_dir = r'C:\Users\PC\Desktop\code\data_files'
output_dir = os.path.join(input_dir, 'combined')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to process each file set
def process_file_set(file_info, output_name):
    combined_df = pd.DataFrame()
    for file_name, pos, exclude_last_columns in file_info:
        file_path = os.path.join(input_dir, file_name)
        df = pd.read_csv(file_path)

        # Remove the 'Rank' column
        df = df.iloc[:, 1:]
        
        # Exclude the last columns if needed
        if exclude_last_columns:
            df = df.iloc[:, :-3]
        
        # Add the 'POS' column
        df['POS'] = pos
        
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    output_path = os.path.join(output_dir, output_name + '.csv')
    combined_df.to_csv(output_path, index=False)

# File set 1
file_set_1 = [
    ('fantasypros_redzoneWR.csv', 'WR', True),
    ('fantasypros_redzoneTE.csv', 'TE', True)
]
process_file_set(file_set_1, 'fp_redzone')

# File set 2
file_set_2 = [
    ('fantasypros_tenzoneWR.csv', 'WR', True),
    ('fantasypros_tenzoneTE.csv', 'TE', True)
]
process_file_set(file_set_2, 'fp_tenzone')

# File set 3
file_set_3 = [
    ('fantasypros_advancedWR.csv', 'WR', False),
    ('fantasypros_advancedTE.csv', 'TE', False)
]
process_file_set(file_set_3, 'fp_advancedreceiving')

# File set 4
file_set_4 = [
    ('fantasypros_seasonWR.csv', 'WR', True),
    ('fantasypros_seasonTE.csv', 'TE', True)
]
process_file_set(file_set_4, 'fp_receiving')

print("Files processed and combined successfully.")

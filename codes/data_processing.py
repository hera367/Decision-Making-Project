import csv
import pandas as pd

# Load the CSV file into a pandas DataFrame
# from google.colab import files
# uploaded = files.upload()

 df = pd.read_csv('D20.csv')

# Define the columns to filter
key_resp_cols = [col for col in df.columns if 'key_resp' in col]
rt_cols = [col for col in df.columns if 'rt' in col]
participant_col = 'participant'
slider_col = 'slider_1.response'

# Filter the DataFrame to get the relevant columns
filtered_df = df[['thisRow.t', 'instructions.started', 'instructions.stopped', 'text.started', 'text.stopped', 'catch1.started', 'catch1.stopped', 'c1.started', 'c1.stopped', 'slider_1.started', 'slider_1.stopped', 'slider_1.rt', participant_col, slider_col] + key_resp_cols + rt_cols]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_data.csv', index=False)
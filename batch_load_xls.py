# This script open data in data/external/sdc_data_ann_9216 folder and save to feather format.
import os
import pandas as pd

path_to_file = input("Add relative path to xlsx data folder: ")
file_names = os.listdir(path_to_file)
file_names.sort()
print(f"file to load {file_names}")


def batch_load_xlsx():
    sdc_df = pd.DataFrame()
    for file_name in file_names:
        file_path = os.path.join(path_to_file, file_name)
        ann_df = pd.read_excel(
            file_path,
            header=1,
        )
        ann_df.columns = (
            ann_df.columns.str.replace("\n", "_").str.replace(" ", "").str.lower()
        )
        sdc_df = pd.concat([sdc_df, ann_df])
        print(f"{file_name} concatenated")

    return sdc_df


if __name__ == "__main__":
    sdc_df = batch_load_xlsx()
    sdc_df.reset_index(drop=True).to_csv(input("Add relative path to csv file: "))

# file_path = os.path.join(path_to_file, file_names[-1])
# ann_df = pd.read_excel(file_path, header=1)
# ann_df.columns = ann_df.columns.str.replace("\n", "_").str.replace(" ", "").str.lower()

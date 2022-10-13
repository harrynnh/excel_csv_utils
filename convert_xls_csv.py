import openpyxl, csv, os
import pandas as pd


def xlsx_csv_converter():
    path_to_xls = input("Add relative path to xlsx data folder: ")
    xls_names = os.listdir(path_to_xls)
    xls_names.sort()
    path_to_csv = input("Add relative path to csv output folder: ")
    print(f"file to convert {xls_names}")
    for xls_name in xls_names:
        wb = openpyxl.load_workbook(os.path.join(path_to_xls, xls_name), data_only=True)
        sheet_name = wb.active
        file_path = os.path.join(path_to_csv, xls_name.replace("xlsx", "csv"))
        with open(file_path, "w", newline="") as f:
            csv_writer = csv.writer(f)
            for row in sheet_name.iter_rows():
                csv_writer.writerow([cell.value for cell in row])
                print(f"converted to {file_path}")
    return


if __name__ == "__main__":
    xlsx_csv_converter()

import pandas as pd
import numpy as np
import os

def compare_excel_files(file1, file2, output_txt):
    # Read files
    df1 = pd.read_excel(file1, engine='openpyxl')
    df2 = pd.read_excel(file2, engine='openpyxl')

    # Determine the maximum number of rows
    max_rows = max(len(df1), len(df2))

    # List to store differences
    differences = []

    # Display progress in English
    for i in range(max_rows):
        # Calculate progress percentage
        progress = (i + 1) / max_rows * 100
        print(f"\rProgress: {progress:.2f}%", end="", flush=True)

        if i >= len(df1):
            differences.append(f"Row {i+1}: Missing in file a.xlsx, present in file b.xlsx: {df2.iloc[i].tolist()}")
        elif i >= len(df2):
            differences.append(f"Row {i+1}: Missing in file b.xlsx, present in file a.xlsx: {df1.iloc[i].tolist()}")
        else:
            row1 = df1.iloc[i]
            row2 = df2.iloc[i]
            for col in df1.columns:
                val1 = row1[col]
                val2 = row2[col]
                # Check if both are NaN/NaT
                if pd.isna(val1) and pd.isna(val2):
                    continue
                elif pd.isna(val1) or pd.isna(val2):
                    differences.append(
                        f"Row {i+1}, Column '{col}': "
                        f"a.xlsx = {val1}, b.xlsx = {val2}"
                    )
                elif val1 != val2:
                    differences.append(
                        f"Row {i+1}, Column '{col}': "
                        f"a.xlsx = {val1}, b.xlsx = {val2}"
                    )

    # End of line after completion
    print("\n")

    # Save differences to text file
    with open(output_txt, 'w', encoding='utf-8') as f:
        if differences:
            f.write("Differences found:\n")
            for diff in differences:
                f.write(f"{diff}\n")
        else:
            f.write("No differences found.\n")

    print(f"Comparison completed. Result saved in {output_txt}")

# File paths
current_dir = os.getcwd()
file1 = os.path.join(current_dir, "a.xlsx")
file2 = os.path.join(current_dir, "b.xlsx")
output_txt = os.path.join(current_dir, "c.txt")

# Execute
compare_excel_files(file1, file2, output_txt)

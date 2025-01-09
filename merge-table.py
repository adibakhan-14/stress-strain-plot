input_file = r"C:\Users\akhan62\Desktop\NiTi\ten-y-till-fails\cyclic-nb-6.txt"  # Path to your input file
output_file = r"C:\Users\akhan62\Desktop\NiTi\ten-y-till-fails\merge-table.txt"  # Path to save the extracted table

# Define the table start identifier
table_start_indicator = "Step"  # Identify the start of the table
columns_detected = False  # Flag to ensure we only write the header once
merged_tables = []  # List to store extracted table lines
unique_lines = set()  # Set to track unique lines

with open(input_file, "r") as infile:
    for line in infile:
        # Skip lines starting with "Loop time"
        if line.strip().startswith("Loop time"):
            continue
        # Check for the start of the table
        if table_start_indicator in line:  # Start of the table
            columns_detected = True
            if not merged_tables:  # Add header only once
                merged_tables.append(line)
                unique_lines.add(line.strip())  # Add to the set
        elif columns_detected:  # Inside the table
            if line.strip() and line.strip() not in unique_lines:  # Ignore duplicates and empty lines
                merged_tables.append(line)
                unique_lines.add(line.strip())
            elif not line.strip():  # Empty line signals the end of a table
                columns_detected = False

# Save the merged tables to a new file
with open(output_file, "w") as outfile:
    outfile.writelines(merged_tables)

print(f"Merged tables have been saved to {output_file}")

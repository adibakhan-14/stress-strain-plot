import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter

# Define the file paths and corresponding custom labels
file_info = [

   
    #    ('comp-y-400K.csv', 'Compression along the Y axis at 400K'),
    #    ('comp-from-relax.csv', 'Compression along the Y axis at 325K'),
    #    ('comp-y-NiTi.csv', 'Compression along the Y axis at NiTi'),
    #    ('comp-z-NiTi.csv', 'Compression along the Z axis at NiTi'),
    #    ('comp-y-semi.csv', 'Compression along the y axis at Semicoherent NiTiNb'),
    #    ('comp-z-semi.csv', 'Compression along the Z axis at Semicoherent NiTiNb'),
    #    ('comp-y-coher.csv', 'Compression along the Y axis at Coherent NiTiNb'),
    #    ('comp-z-coher.csv', 'Compression along the Z axis at Coherent NiTiNb'),
        #  ('ten-z-coher.csv', 'Tensile loading along the Z axis at Coherent NiTiNb'),
        #  ('ten-y-coher.csv', 'Tensile loading along the Y axis at Coherent NiTiNb'),
        #  ('ten-z-semi.csv', 'Tensile loading along the Z axis at Semicoherent NiTiNb'),
        #  ('ten-y-semi.csv', 'Tensile loading along the Y axis at Semicoherent NiTiNb'),
        #  ('ten-z-NiTi.csv', 'Tensile along the Z axis at NiTi'),
        #  ('ten-y-NiTi.csv', 'Compression along the Y axis at NiTi'),
         ('niti-nb-6-tensile-y.csv', 'Tensile loading along the Y axis at 400K'),
         ('Nb-6-tensile-y.csv', 'Tensile loading along the Y axis at 400K'),


    #    ('comp-y-semi.csv', 'Compression along the Y axis at 400K in semicoherent'),
    #    ('comp-y-coherent.csv', 'Compression along the Y axis at 400K in Coherent'),
    #    ('unload-from-relax.csv', 'Unload along the Y axis at at 325K'),
    #    ('unload-y-400K.csv', 'Unload along the Y axis at at 400K'),
    #    ('NiTi-old-meam-unload.csv', 'Unload using NbNiTi potential file along the Y axis at at 400K'),
        #  ('comp-y-coherent.csv', 'Compression along the Y axis at 400K in Coherent')
        #  ('unload-y-semi.csv', 'Unload along the Y axis at 400K in Semicoherent')
    
    
    

]

# Define the columns to plot
x_column = 'strain'
y_column = 'Pyy'

# Function to load and clean data
def load_data(file_path):
    data = pd.read_csv(file_path)
    # Strip any leading/trailing spaces from column names
    data.columns = data.columns.str.strip()
    return data

# Plotting the data
plt.figure(figsize=(10, 6))

for file_path, label in file_info:
    data = load_data(file_path)
    print(f"Columns in {file_path}: {data.columns}")  # Print columns for debugging
    if x_column not in data.columns or y_column not in data.columns:
        print(f"Error: Columns '{x_column}' or '{y_column}' not found in {file_path}")
        continue
    x = data[x_column]
    y = data[y_column]
    plt.plot(x, y, label=label, linestyle='-', linewidth=2 )

plt.xlabel('Strain')  # Add unit for the x-axis
plt.ylabel('Stress (GPa)')  # Add unit for the y-axis

# Use FuncFormatter to add '1e6 Pa' to y-axis labels and ScalarFormatter to avoid scientific notation
formatter = FuncFormatter(lambda x, _: f'{(x*10)/(1000000)}')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Stress-Strain Curves')
plt.legend()  # Display the customized legend
# plt.grid(True)
plt.show()

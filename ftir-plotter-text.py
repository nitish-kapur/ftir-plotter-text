"""
FTIR Plotter
Copyright (C) 2026 Nitish Kapur
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)
Licensed under GNU GPLv3
"""
"""
    1. Plots and opens FTIR graph between transmission and wavenumber from .txt file.
    2. Lets the user choose the .txt file using a dialog box that opens in the current directory, i.e., where the script is stored.
    3. The script expects the data in the following format: 
            ##TITLE=No Description
            ##DATA TYPE=INFRARED SPECTRUM
            ##XUNITS=1/CM
            ##YUNITS=%T
            400.296851  	88.715012
            401.731607  	90.091356
            403.166362  	89.741948
            404.601118  	89.374511 
    4. Make necessary modifications to the "read_ftir_data()" if the meta-data in the .txt file is in some other form.
"""

import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import os  # Import os module for current working directory

# Function to read the FTIR data from the file
def read_ftir_data(file_path):
    wavenumbers = []
    transmissions = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

        # Skip metadata lines until data starts (usually after the '##YUNITS=%T' line)
        data_started = False
        for line in lines:
            if data_started:
                try:
                    # Split the line into wavenumber and transmission
                    parts = line.split()
                    if len(parts) >= 2:  # Ensure the line contains at least two values
                        wavenumber, transmission = map(float, parts[:2])
                        wavenumbers.append(wavenumber)
                        transmissions.append(transmission)
                except ValueError:
                    print(f"Skipping line due to ValueError: {line}")  # Debugging line
                    continue
            elif 'YUNITS=%T' in line:
                data_started = True  # Start reading the data after this line

    # Convert lists to numpy arrays
    return np.array(wavenumbers), np.array(transmissions)

# Function to open file dialog and read the data
def open_and_plot_data():
    # Ask the user to select a text file
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Set the default folder to the current working directory
    current_directory = os.getcwd()

    # Open the file dialog with the initial directory set to current working directory
    file_path = filedialog.askopenfilename(title="Select FTIR Data File", filetypes=[("Text Files", "*.txt")], initialdir=current_directory)

    if file_path:
        try:
            # Read the data from the selected file
            wavenumbers, transmissions = read_ftir_data(file_path)

            # Check if data was read correctly
            if len(wavenumbers) == 0 or len(transmissions) == 0:
                print("No data found in the file or data format is incorrect.")
                return

            # Get the filename without the extension
            file_name = os.path.splitext(os.path.basename(file_path))[0]

            # Plot the data
            plt.figure(figsize=(24, 10))
            plt.plot(wavenumbers, transmissions, label=file_name, color='b', linewidth=2.5)
            plt.xlabel(r'Wavenumber (cm$^{-1}$)', fontsize=20)
            plt.ylabel("Transmission (%) (a.u.)", fontsize=20)
            plt.title(f"FTIR Spectrum - {file_name}", fontsize=20)  # Include the file name in the title
            plt.gca().invert_xaxis()  # Invert the x-axis as is common for FTIR spectra
            # plt.grid(True, linewidth=1.5)

            # Increase the font size of the ticks
            plt.xticks(fontsize=16)  # Increase x-axis tick font size
            plt.yticks(fontsize=16)  # Increase y-axis tick font size

            # plt.legend(fontsize=20, frameon=False,loc='upper right')

            # Increase frame line width (spines)
            # ax = plt.gca()  # Get the current axes
            # ax.spines['top'].set_linewidth(2)
            # ax.spines['right'].set_linewidth(2)
            # ax.spines['bottom'].set_linewidth(2)
            # ax.spines['left'].set_linewidth(2)


            save_path = os.path.splitext(file_path)[
                            0].lower() # + "_saved_plot.png"  # Save with the same base name but with "_saved_plot" suffix
            # plt.savefig(save_path, bbox_inches='tight', pad_inches=0.2)  # Remove padding and save tightly cropped plot

            plt.show()

        except Exception as e:
            print(f"An error occurred while processing the file: {e}")
    else:
        print("No file selected.")

# Run the function to open file dialog and plot
open_and_plot_data()

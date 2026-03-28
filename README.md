# FTIR Plotter

A Python script that reads FTIR spectroscopy data from `.txt` files and plots transmission (%) against wavenumber (cm⁻¹).

---

## Expected Input Format

The script expects `.txt` files with JCAMP-DX-style metadata followed by two-column data:
```
##TITLE=No Description
##DATA TYPE=INFRARED SPECTRUM
##XUNITS=1/CM
##YUNITS=%T
400.296851      88.715012
401.731607      90.091356
403.166362      89.741948
404.601118      89.374511
```

> Data parsing begins after the `##YUNITS=%T` line. If your metadata header differs, modify the `read_ftir_data()` function accordingly.

---

## Requirements

Install dependencies with:
```bash
pip install numpy matplotlib
```

> `tkinter` is included with most standard Python installations. On some Linux systems you may need to install it separately (e.g. `sudo apt install python3-tk`).

---

## Usage

Run the script directly:
```bash
python ftir_plotter.py
```

A file dialog will open in the script's current directory. Select your `.txt` FTIR data file and the plot will be generated and displayed.

---

## Output

- An interactive matplotlib window displaying the FTIR spectrum
- X-axis: Wavenumber (cm⁻¹), **inverted** as per FTIR convention
- Y-axis: Transmission (%) 
- Plot title and legend label are set automatically from the filename

---

## Notes

- The script currently displays the plot interactively. To also save it as an image, uncomment the `plt.savefig(...)` line in `open_and_plot_data()`.
- To re-enable the plot grid or frame spine styling, uncomment the relevant lines in the plotting section.

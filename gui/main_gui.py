import sys
import os
import re
from tkinter import *
from tkinter import ttk, filedialog, messagebox

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import run_pipeline

def main():
    root = Tk(className="Data Cleaner")
    root.minsize(250, 300)
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    # initiate variables
    file_path = StringVar(value="No file selected")
    out_dir = StringVar(value="No output dir selected")
    fill_strat = StringVar(value="N/A")

    # title label
    ttk.Label(frame, text="Data Cleaner").grid(row=0, column=2)
    ttk.Separator(frame, orient="horizontal").grid(row=1, column=0, columnspan=4, sticky="ew", pady=10)

    def get_file_path():
        filepath = filedialog.askopenfilename(
            initialdir=os.path.join(os.getcwd(), "data"),
            title="Select file",
            filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")]
        )
        if filepath:
            file_path.set(filepath)

    def get_output_dir():
        dirpath = filedialog.askdirectory(
            initialdir=os.path.join(os.getcwd(), "outputs"),
            title="Select output directory"
        )
        if dirpath:
            out_dir.set(dirpath)

    def clean_data():
        input_file = file_path.get()
        output_dir = out_dir.get()
        fill_strategy = fill_strat.get()
        if not os.path.exists(input_file):
            messagebox.showerror("Error", "Please select a valid input file")
            return
        if not os.path.exists(output_dir):
            messagebox.showerror("Error", "Please select a valid output directory")
            return

        # run the pipeline (you may need to adjust run_pipeline signature)
        clean_df, report = run_pipeline(input_file, output_dir, fill_strategy)
        
        root.destroy()
        result_window(report)

    # input
    Button(frame, text="Select input file", command=get_file_path).grid(row=2, column=1)
    Label(frame, textvariable=file_path).grid(row=2, column=2)

    # output
    Button(frame, text="Select output dir", command=get_output_dir).grid(row=3, column=1)
    Label(frame, textvariable=out_dir).grid(row=3, column=2)

    # fill strategy
    Label(frame, text="Fill empty values").grid(row=4, column=1)
    Entry(frame, textvariable=fill_strat).grid(row=4, column=2)

    # cleaning
    Button(frame, text="Clean", command=clean_data).grid(row=5, column=2)

    ttk.Button(frame, text="Quit", command=root.destroy).grid(row=6, column=3)
    root.mainloop()

def result_window(report):
    root = Tk(className="Results")
    root.minsize(250, 200)
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    ttk.Label(frame, text="Data Cleaned!").grid(row=0, column=2)
    ttk.Separator(frame, orient="horizontal").grid(row=1, column=0, columnspan=4, sticky="ew", pady=10)

    roww=2
    for key, val in report.items():
        ttk.Label(frame, text=re.split(r"_", key)).grid(row=roww, column=1)
        ttk.Label(frame, text=val).grid(row=roww, column=2)
        roww+=1

    ttk.Button(frame, text="Quit", command=root.destroy).grid(row=5, column=3)
    root.mainloop()

if __name__ == "__main__":
    main()

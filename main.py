import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from GUI.solarSystemGui import SolarSystemGUI
dir_path = os.path.dirname(os.path.realpath(__file__))


def main():
    """execute to run the application"""
    root = tk.Tk()
    app = SolarSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
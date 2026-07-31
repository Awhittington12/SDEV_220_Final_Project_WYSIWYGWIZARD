import tkinter as tk
from gui import ExpenseTrackerGUI


def main():
    root = tk.Tk()
    ExpenseTrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
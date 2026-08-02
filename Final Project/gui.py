"""
gui.py

Contains the graphical user interface.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from expense_manager import ExpenseManager


class ExpenseTrackerGUI:

    def __init__(self, root):

        self.manager = ExpenseManager()

        self.root = root
        self.root.title("Weekly Expense Tracker")
        self.root.geometry("700x550")

        ####################################
        # Expense Name
        ####################################

        tk.Label(root, text="Expense").grid(row=0, column=0, padx=10, pady=5)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        ####################################
        # Amount
        ####################################

        tk.Label(root, text="Amount").grid(row=1, column=0)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)

        ####################################
        # Category
        ####################################

        tk.Label(root, text="Category").grid(row=2, column=0)

        self.category = ttk.Combobox(
            root,
            values=[
                "Food",
                "Transportation",
                "Entertainment",
                "Bills",
                "Shopping",
                "Other"
            ]
        )

        self.category.grid(row=2, column=1)
        self.category.current(0)

        ####################################
        # Buttons
        ####################################

        tk.Button(
            root,
            text="Add Expense",
            command=self.add_expense
        ).grid(row=3, column=0, pady=10)

        tk.Button(
            root,
            text="Edit Selected",
            command=self.edit_expense
        ).grid(row=3, column=1)

        tk.Button(
            root,
            text="Delete Selected",
            command=self.delete_expense
        ).grid(row=3, column=2)

        ####################################
        # Listbox
        ####################################

        self.listbox = tk.Listbox(root, width=70, height=15)
        self.listbox.grid(row=4, column=0, columnspan=3, padx=10)

        ####################################
        # Totals
        ####################################

        self.total_label = tk.Label(root, text="Total: $0.00")
        self.total_label.grid(row=5, column=0, pady=10)

        tk.Button(
            root,
            text="Category Totals",
            command=self.show_categories
        ).grid(row=5, column=1)

    ##################################################

    def refresh(self):

        self.listbox.delete(0, tk.END)

        for expense in self.manager.expenses:
            self.listbox.insert(tk.END, str(expense))

        self.total_label.config(
            text=f"Total: ${self.manager.total_spent():.2f}"
        )

    ##################################################

    def add_expense(self):

        try:

            self.manager.add_expense(
                self.name_entry.get(),
                float(self.amount_entry.get()),
                self.category.get()
            )

            self.refresh()

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid amount."
            )

    ##################################################

    def delete_expense(self):

        selection = self.listbox.curselection()

        if selection:

            self.manager.delete_expense(selection[0])
            self.refresh()

    ##################################################

    def edit_expense(self):

        selection = self.listbox.curselection()

        if selection:

            try:

                self.manager.edit_expense(

                    selection[0],

                    self.name_entry.get(),

                    float(self.amount_entry.get()),

                    self.category.get()
                )

                self.refresh()

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Enter a valid amount."
                )

    ##################################################

    def show_categories(self):

        totals = self.manager.category_totals()

        text = ""

        for category, total in totals.items():

            text += f"{category}: ${total:.2f}\n"

        if text == "":
            text = "No expenses recorded."

        messagebox.showinfo(
            "Category Totals",
            text
        )
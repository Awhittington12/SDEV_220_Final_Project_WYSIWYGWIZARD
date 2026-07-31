

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from expense_manager import ExpenseManager


class ExpenseTrackerGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Weekly Expense Tracker")
        self.root.geometry("700x500")

        # Create an ExpenseManager object
        self.manager = ExpenseManager()

        # Build the interface
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_listbox()
        self.create_total_label()

    #################################################

    def create_labels(self):

        tk.Label(self.root, text="Expense").grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        tk.Label(self.root, text="Amount").grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        tk.Label(self.root, text="Category").grid(
            row=2,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

    #################################################

    def create_entries(self):

        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.grid(row=0, column=1)

        self.amount_entry = tk.Entry(self.root, width=30)
        self.amount_entry.grid(row=1, column=1)

        self.category = ttk.Combobox(
            self.root,
            values=[
                "Food",
                "Transportation",
                "Entertainment",
                "Bills",
                "Shopping",
                "Other"
            ],
            state="readonly",
            width=27
        )

        self.category.grid(row=2, column=1)
        self.category.current(0)

    #################################################

    def create_buttons(self):

        tk.Button(
            self.root,
            text="Add Expense",
            command=self.add_expense
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

    #################################################

    def create_listbox(self):

        self.listbox = tk.Listbox(
            self.root,
            width=60,
            height=15
        )

        self.listbox.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

    #################################################

    def create_total_label(self):

        self.total_label = tk.Label(
            self.root,
            text="Total: $0.00",
            font=("Arial", 12, "bold")
        )

        self.total_label.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=10
        )

    #################################################

    def add_expense(self):

        try:
            name = self.name_entry.get()
            amount = float(self.amount_entry.get())
            category = self.category.get()

            self.manager.add_expense(name, amount, category)

            self.refresh()

            # Clear the input fields
            self.name_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.category.current(0)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number for the amount."
            )

    #################################################

    def refresh(self):

        self.listbox.delete(0, tk.END)

        for expense in self.manager.get_expenses():
            self.listbox.insert(tk.END, str(expense))

        total = self.manager.total_spent()

        self.total_label.config(
            text=f"Total: ${total:.2f}"
        )
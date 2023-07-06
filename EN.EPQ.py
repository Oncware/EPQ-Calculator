import tkinter as tk
from tkinter import ttk, messagebox
import math

def calculate():
    try:
        demand = int(entry_demand.get())
        production_rate = int(entry_production_rate.get())
        unit_production_cost = float(entry_unit_production_cost.get())
        setup_cost = float(entry_setup_cost.get())
        holding_percentage = float(entry_holding_percentage.get())
        
        setup_cost = setup_cost
        EOQ = math.sqrt((2 * demand * setup_cost) / ((holding_percentage * unit_production_cost) * (1 - (demand / production_rate))))
        optimal_production_time = EOQ / production_rate * 365
        optimal_inventory_cycle_time = (EOQ / demand) * 365
        total_cost = (demand * unit_production_cost) + (setup_cost * (demand / EOQ)) + ((EOQ * holding_percentage * unit_production_cost) / 2)
        
        result_window = tk.Toplevel(root)
        result_window.title("Results")
        ttk.Label(result_window, text="a. Economic Production Quantity (EPQ):").grid(row=0, column=0, sticky="w")
        ttk.Label(result_window, text=f"{EOQ:.2f}").grid(row=0, column=1, sticky="w")
        ttk.Label(result_window, text="b. Optimal Production Time:").grid(row=1, column=0, sticky="w")
        ttk.Label(result_window, text=f"{optimal_production_time:.2f}").grid(row=1, column=1, sticky="w")
        ttk.Label(result_window, text="c. Optimal Inventory Cycle Time:").grid(row=2, column=0, sticky="w")
        ttk.Label(result_window, text=f"{optimal_inventory_cycle_time:.2f}").grid(row=2, column=1, sticky="w")
        ttk.Label(result_window, text="d. Total Cost:").grid(row=3, column=0, sticky="w")
        ttk.Label(result_window, text=f"{total_cost:.2f}").grid(row=3, column=1, sticky="w")
        
    except ValueError as e:
        messagebox.showerror("Error", "Please enter valid values.")

root = tk.Tk()
root.title("Inventory Planning Calculator")

# Input fields
ttk.Label(root, text="Demand:").grid(row=0, column=0, sticky="e")
entry_demand = ttk.Entry(root)
entry_demand.grid(row=0, column=1)

ttk.Label(root, text="Production Rate:").grid(row=1, column=0, sticky="e")
entry_production_rate = ttk.Entry(root)
entry_production_rate.grid(row=1, column=1)

ttk.Label(root, text="Unit Production Cost:").grid(row=2, column=0, sticky="e")
entry_unit_production_cost = ttk.Entry(root)
entry_unit_production_cost.grid(row=2, column=1)

ttk.Label(root, text="Setup Cost:").grid(row=3, column=0, sticky="e")
entry_setup_cost = ttk.Entry(root)
entry_setup_cost.grid(row=3, column=1)

ttk.Label(root, text="Holding Percentage:").grid(row=4, column=0, sticky="e")
entry_holding_percentage = ttk.Entry(root)
entry_holding_percentage.grid(row=4, column=1)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2)

root.mainloop()

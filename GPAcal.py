
import tkinter as tk

def calculate_gpa(grades, credit_hours):
    grade_points = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'F': 0.0
    }

    total_credit_hours = sum(credit_hours)
    weighted_grade_points = sum(grade_points[grade] * credit for grade, credit in zip(grades, credit_hours))

    gpa = weighted_grade_points / total_credit_hours
    return gpa

def calculate_button_click():
    grades = [entry_vars[grade].get().upper() for grade in grade_labels]
    credit_hours = [float(credits[i]) for i in range(len(grade_labels))]
    final_gpa = calculate_gpa(grades, credit_hours)
    result_label.config(text=f"Your GPA is: {final_gpa:.4f}")

# Create the main window
root = tk.Tk()
root.title("GPA Calculator")

# Create and place labels and entry fields
grade_labels = ["Mathematics", "DSA", "CODD", "Electrical", "English", "P C"]
entry_vars = {}
credits = [3, 3, 3, 3, 2, 3]  # Specify credits for each course

for i, label_text in enumerate(grade_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5)
    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_vars[label_text] = entry_var

# Create and place calculate button
calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_button_click)
calculate_button.grid(row=len(grade_labels), columnspan=2, padx=10, pady=10)

# Create and place result label
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.grid(row=len(grade_labels) + 1, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()

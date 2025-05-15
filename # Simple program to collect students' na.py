import tkinter as tk
from tkinter import Canvas
import random

def get_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

students = []
percentages = []
colors = []
totals = []
max_totals = []

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    try:
        num_subjects = int(input(f"How many subjects for {name}?: "))
    except ValueError:
        print("Please enter a valid number for subjects.")
        continue
    subject_totals = []
    subject_marks = []
    for i in range(num_subjects):
        try:
            max_mark = float(input(f"Enter total marks for subject {i+1}: "))
            mark = float(input(f"Enter marks obtained for subject {i+1}: "))
        except ValueError:
            print("Please enter valid numbers for marks.")
            break
        subject_totals.append(max_mark)
        subject_marks.append(mark)
    else:
        total = sum(subject_marks)
        max_total = sum(subject_totals)
        percentage = (total / max_total) * 100 if max_total > 0 else 0
        students.append(name)
        percentages.append(percentage)
        colors.append(get_color())
        totals.append(total)
        max_totals.append(max_total)
        continue
    print(f"Skipping {name} due to invalid input.")

if students:
    root = tk.Tk()
    root.title("Students' Percentages")
    width = 80 * len(students) + 100
    height = 400
    canvas = Canvas(root, width=width, height=height, bg='white', highlightthickness=0)
    canvas.pack()

    max_percent = 100
    bar_width = 40
    gap = 40
    pastel_colors = ['#A3CEF1', '#FFB5A7', '#B5EAD7', '#FFDAC1', '#C7CEEA', '#E2F0CB', '#B5D0E6', '#F3B0C3', '#F6DFEB', '#F9F9C5']
    for i, (name, percent, total, max_total) in enumerate(zip(students, percentages, totals, max_totals)):
        color = pastel_colors[i % len(pastel_colors)]
        x0 = 50 + i * (bar_width + gap)
        y0 = height - 50
        x1 = x0 + bar_width
        y1 = y0 - (percent / max_percent) * 300
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='')
        canvas.create_text((x0 + x1) / 2, y0 + 15, text=name, anchor='n', angle=45, fill='#222', font=('Arial', 10, 'bold'))
        canvas.create_text((x0 + x1) / 2, y1 - 10, text=f"{percent:.2f}%", anchor='s', fill='#222', font=('Arial', 10, 'bold'))
        def smart_fmt(val):
            return f"{val:.2f}" if not val.is_integer() else f"{int(val)}"
        canvas.create_text((x0 + x1) / 2, y0 + 35, text=f"{smart_fmt(total)}/{smart_fmt(max_total)}", anchor='n', font=('Arial', 9), fill='#555')
    root.mainloop()
else:
    print("No data to display.")
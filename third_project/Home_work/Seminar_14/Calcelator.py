from tkinter import Tk, Button, Entry, Label


def on_click(button_text):
    current_text = entry.get()
    new_text = current_text + button_text
    entry.delete(0, "end")
    entry.insert(0, new_text)


def clear_entry():
    entry.delete(0, "end")


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, "end")
        entry.insert(0, "Error")


# Создание окна
root = Tk()
root.title("Простой калькулятор")

# Создание виджета для ввода текста
entry = Entry(root, width=16, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

# Создание кнопок
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(root, text=button, padx=20, pady=20, font=("Arial", 12),
           command=lambda b=button: on_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Кнопка для очистки ввода
Button(root, text="C", padx=20, pady=20, font=("Arial", 12), command=clear_entry).grid(row=row_val, column=col_val)

# Запуск цикла событий
root.mainloop()

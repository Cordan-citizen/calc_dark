from tkinter import *
from decimal import *

# Tk() - базовый класс любого Tkinter-приложения 
root = Tk()
# Задаётся название (title)
root.title('Calculator')

# Список кнопок
buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = ''
stack = []
# Тёмная тема - выключена по умолчанию
dark_theme = False

# Функция, реализующая тёмную тему
def d_theme():
    global dark_theme
    global button
    global button1
    global label
    global root
    global buttons
    global stack
    global activeStr
    
    dark_theme == True
    root["bg"] = "gray22"
    label = Label(root, text='0', bg='gray22', fg='Cyan', width=35)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")
    
    button = Button(root, overrelief=SUNKEN, text='CE', fg="Cyan", bg="gray22", command=lambda text='CE': click(text))
    button.grid(row=1, column=3, sticky="nsew")

    button1 = Button(root, overrelief=SUNKEN, text='White', fg="Cyan", bg="gray22", command=w_theme)
    button1.grid(row=1, column=2, sticky="nsew")
    
    for row in range(4):
        for col in range(4):
            button = Button(root, overrelief=SUNKEN, text=buttons[row][col],fg="Cyan",bg="gray22",
                    command=lambda row=row, col=col: click(buttons[row][col]))
            button.grid(row=row + 2, column=col, sticky="nsew")
            
# Функция, реализующая светлую тему
def w_theme():
    global dark_theme
    global button
    global button1
    global label
    global root
    global buttons
    global stack
    global activeStr
    
    dark_theme == False
    root["bg"] = "#f2f0f2"
    label = Label(root, text='0', width=35)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    button = Button(root, overrelief=SUNKEN, text='CE', command=lambda text='CE': click(text))
    button.grid(row=1, column=3, sticky="nsew")

    button1 = Button(root, overrelief=SUNKEN, text='Dark', command=d_theme)
    button1.grid(row=1, column=2, sticky="nsew")

    for row in range(4):
        for col in range(4):
            button = Button(root, overrelief=SUNKEN, text=buttons[row][col],
                    command=lambda row=row, col=col: click(buttons[row][col]))
            button.grid(row=row + 2, column=col, sticky="nsew")

    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(4, weight=1)

# Функция с перациями калькулятора
def calculate():
    global stack
    global label
    
    result = 0
    # Метод pop возвращает удалённый объект из списка
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        if operand2 == '0':
            result = 'Error'
        elif operand2 != 0:    
            result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2

    # Метод configure конфигурирует объект после создания
    label.configure(text=str(result))

# Функция click выполняет обработку нажатой клавиши
def click(text):
    global activeStr
    global stack

    if text == 'CE':
        # Метод clear очищает список stack(табло калькулятора)
        stack.clear()
        activeStr = ''
        label.configure(text='0')

    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)

    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')
    
if dark_theme == False:
    
    label = Label(root, text='0', width=35)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    button = Button(root, text='CE', overrelief=SUNKEN, command=lambda text='CE': click(text))
    button.grid(row=1, column=3, sticky="nsew")

    button1 = Button(root, text='Dark', padx='5',overrelief=SUNKEN, command=d_theme)
    button1.grid(row=1, column=2, sticky="nsew")

    for row in range(4):
        for col in range(4):
            button = Button(root, overrelief=SUNKEN, text=buttons[row][col],
                    command=lambda row=row, col=col: click(buttons[row][col]))
            button.grid(row=row + 2, column=col, sticky="nsew")

    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(4, weight=1)
    

root.mainloop()

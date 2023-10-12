import tkinter as tk


class CalculatorApp:

  def __init__(self, root):
    self.root = root
    root.title("Calculator")
    self.result_var = tk.StringVar()
    self.result_var.set("0")
    self.current_input = ""

    # Entry for displaying the result
    entry = tk.Entry(root,
                     textvariable=self.result_var,
                     font=("Arial", 20),
                     justify="right",
                     bd=10)
    entry.grid(row=0, column=0, columnspan=4)

    # Buttons
    button_texts = [
        '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', 'C',
        '=', '+'
    ]

    row, col = 1, 0
    for text in button_texts:
      tk.Button(root,
                text=text,
                font=("Arial", 20),
                height=2,
                width=5,
                command=lambda t=text: self.on_button_click(t)).grid(
                    row=row, column=col)
      col += 1
      if col > 3:
        col = 0
        row += 1

  def on_button_click(self, button_text):
    if button_text == '=':
      try:
        result = str(eval(self.current_input))
      except:
        result = "Error"
      self.current_input = result
    elif button_text == 'C':
      self.current_input = ""
      result = "0"
    else:
      self.current_input += button_text
      result = self.current_input

    self.result_var.set(result)


if __name__ == '__main__':
  root = tk.Tk()
  app = CalculatorApp(root)
  root.mainloop()

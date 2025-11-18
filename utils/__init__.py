import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.destroy())
root.configure(bg="#222")

canvas = tk.Canvas(root, bg="#222", highlightthickness=0)
canvas.pack(fill="both", expand=True)

buttons = []

def create_button(x1, y1, x2, y2, text, command):
    rect = canvas.create_rectangle(x1, y1, x2, y2, fill="#3F8CFF", outline="#3F8CFF", width=0)
    label = canvas.create_text((x1+x2)//2, (y1+y2)//2, text=text, fill="white", font=("맑은 고딕", 20, "bold"))
    
    def on_click(event):
        command()
    def on_enter(event):
        canvas.itemconfig(rect, fill="#1E5FFF")
        canvas.scale(rect, (x1+x2)//2, (y1+y2)//2, 1.05, 1.05)
        canvas.scale(label, (x1+x2)//2, (y1+y2)//2, 1.05, 1.05)
    def on_leave(event):
        canvas.itemconfig(rect, fill="#3F8CFF")
        canvas.scale(rect, (x1+x2)//2, (y1+y2)//2, 0.95238, 0.95238)
        canvas.scale(label, (x1+x2)//2, (y1+y2)//2, 0.95238, 0.95238)

    canvas.tag_bind(rect, "<Button-1>", on_click)
    canvas.tag_bind(label, "<Button-1>", on_click)
    canvas.tag_bind(rect, "<Enter>", on_enter)
    canvas.tag_bind(label, "<Enter>", on_enter)
    canvas.tag_bind(rect, "<Leave>", on_leave)
    canvas.tag_bind(label, "<Leave>", on_leave)

    buttons.append((rect, label))
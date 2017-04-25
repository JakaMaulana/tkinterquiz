
#!/usr/bin/env python3

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox
import json

class VerticalScrolledFrame:
    def __init__(self, master, **kwargs):
        self.outer = tk.Frame(master)

        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        self.canvas = tk.Canvas(self.outer, highlightthickness=0, **kwargs)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas['yscrollcommand'] = self.vsb.set
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview

        self.inner = tk.Frame(self.canvas)
        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            return getattr(self.outer, item)
        else:
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units" )
        elif event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units" )

root=tk.Tk()
root.geometry('700x700+400+400')
root.title('Rishabh Arts Admin Panel')
img_label = tk.Label(root)
img_label.img = tk.PhotoImage(file='Logo.png')

img_label.config(image=img_label.img)
img_label.pack()

welcom=tk.Label(root,text="Quiz Database").pack()

score = 0

def mquit():
    mexit=messagebox.askyesno(title="Quit",message="Quit Updating Test ?")
    if mexit > 0:
        root.destroy()
        return

def finished():
    mexit=messagebox.askyesno(title="Finish",message="Are You Sure ?")
    if mexit > 0:
        score = 0
        for i in user_answers:
            if user_answers[i].get() == database[i]['answer']:
                score = score + 1

        lc.config(text="you got {} questions out of {} correct!".format(score, len(user_answers)))

with open('database.json') as f:
    database = json.load(f)


question_frame = VerticalScrolledFrame(root, height=500)
question_frame.pack(fill=tk.X)
user_data = [] # put the user data into a list, just like the database. This will be just like the database, except filled with StringVars and Intvars

def add_question(question, options, answer):
    one_q_frame = tk.Frame(question_frame) # since we need to layout the radio buttons side by side with a Entry, it would be easier to use the grid manager. So lets make a new frame for every question that we can lay out.
    one_q_frame.columnconfigure(1, weight=1) # make the 2nd column expand
    one_q_frame.pack(expand=True, fill=tk.X)

    # make the question dictionary for variables with 3 componants
    q_vars = {
        'question': tk.StringVar(value=question),
        'options': [], # we'll fill this in in the loop
        'answer': tk.IntVar(value=answer)
        }
    user_data.append(q_vars)

    ent = tk.Entry(one_q_frame, width=50, textvariable=q_vars['question']) # set the width of the frame here
    ent.grid(row=0, column=0, columnspan=2, sticky='ew')

    for j in range(4):
        btn = tk.Radiobutton(one_q_frame,
            value=j,
            variable=q_vars['answer'])
        btn.grid(row=1+j, column=0)
        q_vars['options'].append(tk.StringVar(value=options[j])) # make the option stringvar
        ent = tk.Entry(one_q_frame, textvariable=q_vars['options'][j])
        ent.grid(row=1+j, column=1, sticky='ew')


    mbutton=tk.Button(one_q_frame,
        text='Del Question',
        command=del_question,
        fg='red',bg='blue')
    mbutton.grid(row=2+j, column=1)

def del_question():
    add_question('', ['','','',''], -1)



for i in range(50):
    add_question(database[i]['question'], database[i]['options'], database[i]['answer'])

def new_question():
    add_question('', ['','','',''], -1) # add a new question with blank question, 4 blank answers, and -1 as the correct answer
    root.after(10, lambda: question_frame.canvas.yview('moveto', 1)) # scroll to bottom

def finished():
    new_list = []
    for i in range(len(user_data)):
        new_list.append({}) # add a empty dictionary to the new list
        new_list[i]['answer'] = user_data[i]['answer'].get()
        # add question data and options data the same way

    #save the new data
    with open('db.json', 'w') as f:
        json.dump(new_list, f, indent=2)


mbutton=tk.Button(root,text='Quit',command=mquit,fg='red',bg='blue')
mbutton.pack()

mbutton=tk.Button(root,text='Add Question',command=new_question,fg='red',bg='blue')
mbutton.pack()

mbutton=tk.Button(root,text='Del Question',command=del_question,fg='red',bg='blue')
mbutton.pack()

lc = tk.Label(root) # the score will be displayed here.
lc.pack()

fbutton=tk.Button(root,text='Finish',command=finished,fg='red',bg='blue')
fbutton.pack()



root.mainloop()

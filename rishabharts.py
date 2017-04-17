#! usr/bin/python3
#(this part i have added because i am trying to make it click and execute on my ubuntu )
 
 
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox
 
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
root.title('Quiz Program')
img_label = tk.Label(root)
img_label.img = tk.PhotoImage(file='Logo.png')
'''logo seems to be big what size should i prefer coz its messed up
the frame i guess'''
img_label.config(image=img_label.img)
img_label.pack()
 
welcom=tk.Label(root,text="Welcome To Quiz")
welcom.pack()
 
score = 0
 
def mquit():
    mexit=messagebox.askyesno(title="Quit",message="Quit The Test ?")
    if mexit > 0:
        root.destroy()
        return
 
def finished():
    mexit=messagebox.askyesno(title="Finish",message="Are You Sure ?")
    if mexit > 0:
        score = 0
        for i in user_answers:
            if user_answers[i].get() == correct_answers[i]:
                score = score + 1
 
        lc.config(text="you got {} questions out of {} correct!".format(score, len(user_answers)))
 
answers = {1: ['a.Western India Insurance', 'b.LIC', 'c.Oriental Life Insurance Company', 'd.Bombay Mutal Insurance'],
           2: ['a.Fiancial Risk', 'b.Non-Financial Risk', 'c.Both A And B', 'd.None Of Them'],
           3: ['a.The Risk', 'b.The Peril', 'c.Neither Peril Nor Risk', 'd.Both'],
           4: ['a.Smoking', 'b.A Family History Of High Blood Pressure', 'c.Both', 'd.None Of Them'],
           5: ['a.Policyholder', 'b.Agent', 'c.I.R.D.A', 'd.Insurance Company'],
           6: ['a.Agent', 'b.Policyholder', 'c.Insurance Company', 'd.I.R.D.A'],
           7: ['a.One Phase', 'b.Four Phase', 'c.Two Phase', 'd.Three Phase'],
           8: ['a.Dividend', 'b.Sum Assured', 'c.Premium', 'd.Interest'],
           9: ['a.Indian Runner Duck Association', 'b.Iskandar Regional Development Authority ', 'c.Insurance Regulatory Development Authority', 'd.Infra Red Data Association'],
           10: ['a.Risk Cover', 'b.Investment Option', 'c.Combination Of Both', 'd.None Of Both'],
           11: ['a.Giving Guarantee To Policies By Bank', 'b.To Undergo Prescribed Training', 'c.Selling Insurance Policies Through Banks', 'd.None Of Them'],
           12: ['a.ULIP', 'b.Endowment', 'c.Pension Policy', 'd.Term Assuurance'],
           13: ['a.Net Premium', 'b.Loading Premium ', 'c.Gross Premium', 'd.Risk Premium'],
           14: ['a.High Returns', 'b.Low Returns', 'c.No Returns', 'd.Good Returns'],
           15: ['a.Parents', 'b.Husband', 'c.Insurance Company', 'd.Child'],
           16: ['a.Family', 'b.Employees', 'c.Acc TO Height', 'd.Same Age'],
           17: ['a.Term Insurance Plan', 'b.Money Back', 'c.Pension Plan', 'd.ULIP Plan'],
           18: ['a.Single Premium Policies', 'b.Money Back Policies', 'c.Annuity Plans', 'd.Endowment Plans'],
           19: ['a.Agent', 'b.To Achieve The Ultimate Goal', 'c.IRDA', 'd.Insurance Company'],
           20: ['a.2000', 'b.2004', 'c.2002', 'd.2017'],
           21: ['a.SB,Maturity And Death', 'b.None Of Them', 'c.Loan,Premium,Pension', 'd.Surrender Values'],
           22: ['a.Dec 2018', 'b.May 2005', 'c.Dec 1999', 'd.Aug 1985'],
           23: ['a.Highly Qualified Customer', 'b.True Identity Of The Customer', 'c.Rural Customer', 'd.Innocent Customer'],
           24: ['a.2002', 'b.1995', 'c.2012', 'd.1999'],
           25: ['a.SEBI', 'b.IRDA', 'c.Constitution', 'd.RBI'],
           26: ['a.IRDA', 'b.De-Tarrification', 'c.Tarrif Advisory Committee', 'd.Foreign Exchange'],
           27: ['a.2 month', 'b.1 Month', 'c.1 Year', 'd.5 Years'],
           28: ['a.Agents', 'b.Bank Manager', 'c.Lose Assessors', 'd.Surveyors'],
           29: ['a.Conduct Inspection At Stock Exchange', 'b.Conduct Enquiry of Insurance Company', 'c.Conduct Audit Of Insurance Company', 'd.Conduct Inspection Of Insurance Company'],
           30: ['a.15th Aug 1940', 'b.1st Jan 1947', 'c.1st Apr 1935', 'd.5th May 2012'],
           31: ['a.Clients Need', 'b.Insurance Decision', 'c.Market Situation', 'd.Agents Choice'],
           32: ['a.In Mail', 'b.Orally In Meeting', 'c.By Order', 'd.In Writing'],
           33: ['a.Quarterly', 'b.Yearly', 'c.Monthly', 'd.Once In 6 Months'],
           34: ['a.Dying Early And Living Too Long', 'b.Sum Assured And Bonus', 'c.Death Cover And Maturity', 'd.Accident Risk Cover And Death Cover'],
           35: ['a.Major Possible Loan', 'b.Minimum Possible Loan', 'c.Minor Possible Loan', 'd.Maximum Possible Loan'],
           36: ['a.Sec 42 Of Insurance Act 1938', 'b.Contract Act 1872', 'c.Insurance Act 1972', 'd.None Of Above'],
           37: ['a.Chances To Up Selling', 'b.All The Above', 'c.Word Of Mouth Publicity For Agent', 'd.More Reference Generation'],
           38: ['a.Maturity Payment', 'b.Claim Settlement Ratio', 'c.Revival', 'd.Foreclosure'],
           39: ['a.1st Aug 1890', 'b.1st Sept 1956', 'c.1st Dec 1956', 'd.4th July 1956'],
           40: ['a.1st July 2005', 'b.1st Mar 2005', 'c.4th Dec 2005', 'd.1st Jan 2005'],
           41: ['a.1945', 'b.1986', 'c.2011', 'd.2003'],
           42: ['a.LIC Only', 'b.All Financial Institutions', 'c.Govt Co. Only', 'd.Banks Only'],
           43: ['a.Trustee', 'b.Beneficiary', 'c.Trustor', 'd.Life Assured'],
           44: ['a.Address Proof', 'b.ID Proof', 'c.None', 'd.Both A and B'],
           45: ['a.SEBI', 'b.RBI', 'c.IRDA', 'd.TRAI'],
           46: ['a.Hedge', 'b.IRDA', 'c.Life Insurance Council', 'd.SEBI'],
           47: ['a.₹10', 'b.₹50', 'c.₹100', 'd.₹20'],
           48: ['a.3 Year', 'b.5 Year', 'c.1 Year', 'd.2 Year'],
           49: ['a.1st July 1939', 'b.1st Mar 2009', 'c.2nd June 1999', 'd.5th Sept 2008'],
           50: ['a.Minimize Paper Work', 'b.Earn More', 'c.None Of Them', 'd.Avoid Customer Complaint']
           }
 
questions = {1: 'First Insurance Company In India ?',
             2: 'Which Of The Following Risks Are Insurable ?',
             3: 'The Amount Of Insurance Depends On ?',
             4:'Moral Hazard Is ?',
             5:'Insured Means ?',
             6:'Insurer Means ?',
             7:'History Of Insurance Can Be Divided Into ?',
             8:'The Insured Has To Pay Consideration To Insure Is Called ?',
             9:'I.R.D.A Stands For ?',
             10:'Insurance Product Is ?',
             11:'What Is Bancassurance ?',
             12:'An Individual Looking For Retirement Income Needs To Invest In ?',
             13:'Level Premium Is Calculated Based On ?',
             14:'Low Risk Product Gives ?',
             15:'Following The The Beneficiary Child Plan:',
             16:'A Group Of People Insured In A Policy Belond To Which Catagory :',
             17:'Which Is The Suitable Plan For Senior Citizen ?',
             18:'Commission Rates Are Low Under ?',
             19:'Keeping Policy In Force Till Maturity Helps Client:',
             20:'The IRDA Has Laid Down Guidelines For Settlement Of Claims In ?',
             21:'What Are The 3 Main Kinds Of Claims ?',
             22:'I.R.D.A Was Passed By Pariliament In ?',
             23:'Know Your Customer Relates To ?',
             24:'Insurance Of Institute Of India(III) Was Formed In?',
             25:'Controls The Monetary System In India.',
             26:'Following Terms Are Directly Related With Insurance:',
             27:'Ombudsman Passes An Award Within Which Time ?',
             28:'IRDA Does Not Fixes The Code Of Conduct To ?',
             29:'IRDA Is Not Having The Power To:',
             30:'Reserve Bank Of India Was Setup In ?',
             31:'Product Shortlisting Is Based On ?',
             32:'Recommandations To Clients Are Presented:',
             33:'Bank Interest Is Accumulated:',
             34:'Basic Elements Of Life Insurance Plan Are:',
             35:'MPL Abbreviates :',
             36:'Agents Must Have Licensed Under:',
             37:'Satisfied Client Will Lead To:',
             38:'Plays Important Role In:',
             39:'LIC Was Formed On ?',
             40:'Prevention Of Money Laundry Act Came Into Effect From:',
             41:'Customer Protection Act Was Established In:',
             42:'Compliance With AML Is Applicable To:',
             43:'The Person Who Forms The Trust',
             44:'What KYC Needs ?',
             45:'Who Is Regulatory Body Of Money Laundering In Insurance Sector?',
             46:'Investment In Insurance Sector Is Governed By:',
             47:'Duplicate License Fee:',
             48:'The Complaint Under COPA Should Be Filed With In:',
             49:'Insurance Act 1938 Came Into Effect In:',
             50:'An Advisor Will Do Churn To:'
             }
 
correct_answers = { 1: 2,
                    2: 0,
                    3: 3,
                    4: 0,
                    5: 1,
                    6: 2,
                    7: 3,
                    8: 2,
                    9: 2,
                    10: 2,
                    11: 2,
                    12: 2,
                    13: 3,
                    14: 1,
                    15: 3,
                    16: 1,
                    17: 2,
                    18: 0,
                    19: 1,
                    20: 2,
                    21: 0,
                    22: 2,
                    23: 1,
                    24: 1,
                    25: 3,
                    26: 3,
                    27: 1,
                    28: 1,
                    29: 0,
                    30: 2,
                    31: 0,
                    32: 3,
                    33: 1,
                    34: 2,
                    35: 3,
                    36: 0,
                    37: 1,
                    38: 1,
                    39: 1,
                    40: 0,
                    41: 1,
                    42: 1,
                    43: 0,
                    44: 3,
                    45: 1,
                    46: 2,
                    47: 1,
                    48: 3,
                    49: 0,
                    50: 1}
 
 
labels = {}
user_answers = {}
question_frame = VerticalScrolledFrame(root, height=500)
question_frame.pack(fill=tk.X)
 
for i in range(1, 51):
    user_answers[i] = tk.IntVar(value=-1)
    labels[i] = tk.Label(question_frame, text=questions[i])
    labels[i].pack(anchor=tk.W)
    for j in range(4):
        btn = tk.Radiobutton(question_frame,
            text=answers[i][j],
            value=j,
            variable=user_answers[i])
        btn.pack(anchor=tk.W)
 
 
mbutton=tk.Button(root,text='Quit',command=mquit,fg='red',bg='blue')
mbutton.pack()
 
 
lc = tk.Label(root) # the score will be displayed here.
lc.pack()
 
fbutton=tk.Button(root,text='Finish',command=finished,fg='red',bg='blue')
fbutton.pack()
 
 
root.mainloop()

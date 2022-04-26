import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
import time

current_balance = 100000


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        self.shared_data = {"Balance": tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SignIn, pinPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SignIn")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class SignIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14324d')
        self.controller = controller

        self.controller.title('Achban Bank')
        self.controller.state("zoomed")
        self.controller.iconphoto(False,
                                  tk.PhotoImage(file='C:/Users/tobia_rc2sfnf/PycharmProjects/ATM/atm.png'))

        headingLabel1 = tk.Label(self,
                                 text='Achban Bank ATM',
                                 font=('Arial', 40, 'bold'),
                                 foreground='#944c00',
                                 background='#14324d')
        headingLabel1.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#14324d')
        space_label.pack()

        ID_Label2 = tk.Label(self,
                             text='Enter your card number',
                             font=('Arial', 13),
                             foreground='white',
                             background='#14324d')
        ID_Label2.pack(pady=10)

        my_id = tk.StringVar()
        ID_entry_box = tk.Entry(self,
                                textvariable=my_id,
                                font=("Arial", 12),
                                width=30)
        ID_entry_box.focus_set()
        ID_entry_box.pack(ipady=7)

        def check_id():
            if my_id.get() == '10000':
                my_id.set("")
                wrong_id_label['text'] = ''
                controller.show_frame('pinPage')
            else:
                wrong_id_label['text'] = 'Incorrect Id'

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_id,
                                 relief='raised',
                                 borderwidth=2,
                                 width=38,
                                 height=2)
        enter_button.pack(pady=10)

        wrong_id_label = tk.Label(self,
                                  text='',
                                  font=('Arial', 13),
                                  fg='white',
                                  bg='#154670',
                                  anchor='n')
        wrong_id_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file="maestro.png")
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        express_photo = tk.PhotoImage(file="american-express.png")
        express_label = tk.Label(bottom_frame, image=express_photo)
        express_label.pack(side='left')
        express_label.image = express_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Arial', 12))
        time_label.pack(side='right')

        tick()


class pinPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14324d')
        self.controller = controller

        self.controller.title('Achban Bank')
        self.controller.state("zoomed")
        self.controller.iconphoto(False,
                                  tk.PhotoImage(file='C:/Users/tobia_rc2sfnf/PycharmProjects/ATM/atm.png'))

        headingLabel1 = tk.Label(self,
                                 text='Achban Bank ATM',
                                 font=('Arial', 40, 'bold'),
                                 foreground='#944c00',
                                 background='#14324d')
        headingLabel1.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#14324d')
        space_label.pack()

        ID_Label2 = tk.Label(self,
                             text='Enter your pin number',
                             font=('Arial', 13),
                             foreground='white',
                             background='#14324d')
        ID_Label2.pack(pady=10)

        my_pin = tk.StringVar()
        pin_entry_box = tk.Entry(self,
                                 textvariable=my_pin,
                                 font=("Arial", 12),
                                 width=30)
        pin_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            pin_entry_box.configure(fg='black', show='*')

        pin_entry_box.bind('<FocusIn>', handle_focus_in)

        def check_pin():
            if my_pin.get() == '1111':
                my_pin.set("")
                wrong_pin_label['text'] = ''
                controller.show_frame('MenuPage')
            else:
                wrong_pin_label['text'] = 'Incorrect pin'

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_pin,
                                 relief='raised',
                                 borderwidth=2,
                                 width=38,
                                 height=2)
        enter_button.pack(pady=10)

        wrong_pin_label = tk.Label(self,
                                   text='',
                                   font=('Arial', 13),
                                   fg='white',
                                   bg='#154670',
                                   anchor='n')
        wrong_pin_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file="maestro.png")
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        express_photo = tk.PhotoImage(file="american-express.png")
        express_label = tk.Label(bottom_frame, image=express_photo)
        express_label.pack(side='left')
        express_label.image = express_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Arial', 12))
        time_label.pack(side='right')

        tick()


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14324d')
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text='Hello Fasil Mulatu, Welcome to Achban Bank.',
                                 font=('Arial', 40, 'bold'),
                                 foreground='#944c00',
                                 background='#14324d')
        headingLabel1.pack(pady=25)

        options_label = tk.Label(self,
                                 text='Option Menu',
                                 font=('Arial', 13),
                                 foreground='white',
                                 background='#14324d')
        options_label.pack()

        selections_label = tk.Label(self,
                                    text='Please make a selection',
                                    font=('Arial', 13),
                                    foreground='white',
                                    background='#14324d',
                                    anchor='w')
        selections_label.pack(fill='x')

        button_frame = tk.Frame(self, bg="#154670")
        button_frame.pack(fill='both', expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button = tk.Button(button_frame,
                                    text='Withdraw',
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        withdraw_button.grid(row=0, column=0, pady=5)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button = tk.Button(button_frame,
                                   text='deposit',
                                   command=deposit,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        def balance():
            controller.show_frame('BalancePage')

        Balance_button = tk.Button(button_frame,
                                   text='Balance',
                                   command=balance,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        Balance_button.grid(row=2, column=0, pady=5)

        def exit():
            controller.show_frame('SignIn')

        exit_button = tk.Button(button_frame,
                                text='EXIT',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=4, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file="maestro.png")
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        express_photo = tk.PhotoImage(file="american-express.png")
        express_label = tk.Label(bottom_frame, image=express_photo)
        express_label.pack(side='left')
        express_label.image = express_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Arial', 12))
        time_label.pack(side='right')

        tick()


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14324d')
        self.controller = controller

        self.controller.title('Achban Bank')
        self.controller.state("zoomed")
        self.controller.iconphoto(False,
                                  tk.PhotoImage(file='C:/Users/tobia_rc2sfnf/PycharmProjects/ATM/atm.png'))

        headingLabel1 = tk.Label(self,
                                 text='Achban Bank ATM',
                                 font=('Arial', 40, 'bold'),
                                 foreground='#944c00',
                                 background='#14324d')
        headingLabel1.pack(pady=25)

        withdrawl_label = tk.Label(self,
                                   text='Withdraw Menu',
                                   font=('Arial', 13),
                                   foreground='white',
                                   background='#14324d')
        withdrawl_label.pack()

        amount_label = tk.Label(self,
                                text='Select the amount you would like to withdraw',
                                font=('Arial', 14),
                                fg='white',
                                bg='#14324d')
        amount_label.pack(pady=5)

        button_frame = tk.Frame(self, bg='#154670')
        button_frame.pack(fill='both', expand=True)

        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data["Balance"].set(current_balance)
            controller.show_frame('MenuPage')

        fiveHundred_button = tk.Button(button_frame,
                                       text='500',
                                       command=lambda:withdraw(500),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        fiveHundred_button.grid(row=0, column=0, pady=5)

        oneThousand_button = tk.Button(button_frame,
                                       text='1000',
                                       command=lambda: withdraw(1000),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        oneThousand_button.grid(row=1, column=0, pady=5)

        oneFiveHundred_button = tk.Button(button_frame,
                                          text='1500',
                                          command=lambda: withdraw(1500),
                                          relief='raised',
                                          borderwidth=3,
                                          width=50,
                                          height=5)
        oneFiveHundred_button.grid(row=2, column=0, pady=5)

        twoThousand_button = tk.Button(button_frame,
                                       text='2000',
                                       command=lambda: withdraw(2000),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        twoThousand_button.grid(row=3, column=0, pady=5)

        threeThousand_button = tk.Button(button_frame,
                                         text='3000',
                                         command=lambda: withdraw(3000),
                                         relief='raised',
                                         borderwidth=3,
                                         width=50,
                                         height=5)
        threeThousand_button.grid(row=0, column=1, pady=5, padx=555)

        fourThousand_button = tk.Button(button_frame,
                                        text='4000',
                                        command=lambda: withdraw(4000),
                                        relief='raised',
                                        borderwidth=3,
                                        width=50,
                                        height=5)
        fourThousand_button.grid(row=1, column=1, pady=5)

        fiveThousand_button = tk.Button(button_frame,
                                        text='5000',
                                        command=lambda: withdraw(5000),
                                        relief='raised',
                                        borderwidth=3,
                                        width=50,
                                        height=5)
        fiveThousand_button.grid(row=2, column=1, pady=5)

        cash = tk.StringVar()
        other_entry_box = tk.Entry(button_frame,
                                   textvariable=cash,
                                   width=59,
                                   justify='center')
        other_entry_box.grid(row=3, column=1, pady=5, ipady=15)

        other_entry_label = tk.Label(button_frame,
                                     text='other amount',
                                     font=('Arial', 15),
                                     fg='#FFFFFF',
                                     bg='#154670')

        other_entry_label.grid(row=4, column=1, pady=2, ipady=3)

        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data["Balance"].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')

        other_entry_box.bind('<Return>', other_amount)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file="maestro.png")
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        express_photo = tk.PhotoImage(file="american-express.png")
        express_label = tk.Label(bottom_frame, image=express_photo)
        express_label.pack(side='left')
        express_label.image = express_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Arial', 12))
        time_label.pack(side='right')

        tick()


class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14324d')
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text='Achban Bank ATM',
                                 font=('Times New Roman', 40, 'bold'),
                                 foreground='#944c00',
                                 background='#14324d')
        headingLabel1.pack(pady=25)

        headingLabel2 = tk.Label(self,
                                 text='Deposit Menu',
                                 font=('Times New Roman', 15),
                                 foreground='white',
                                 bg='#14324d')
        headingLabel2.pack(pady=4)

        space_label = tk.Label(self, height=4, bg='#14324d')
        space_label.pack()

        enter_amount = tk.Label(self,
                                text='Enter deposit amount',
                                font=('Arial', 13),
                                foreground='white',
                                background='#14324d')
        enter_amount.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 font=('Arial', 13),
                                 width=30)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data["Balance"].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=deposit_cash,
                                 relief='raised',
                                 borderwidth=2,
                                 width=38,
                                 height=2)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self, bg='#154670')
        two_tone_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file="maestro.png")
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        express_photo = tk.PhotoImage(file="american-express.png")
        express_label = tk.Label(bottom_frame, image=express_photo)
        express_label.pack(side='left')
        express_label.image = express_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Arial', 12))
        time_label.pack(side='right')

        tick()


class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#14324d')
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text='Achban Bank ATM',
                                 font=('Times New Roman', 40, 'bold'),
                                 foreground='#944c00',
                                 background='#14324d')
        headingLabel1.pack(pady=25)

        headingLabel2 = tk.Label(self,
                                 text='Balance',
                                 font=('Times New Roman', 20),
                                 foreground='white',
                                 bg='#14324d')
        headingLabel2.pack(pady=4)

        global current_balance
        controller.shared_data["Balance"].set(current_balance)

        balance_label = tk.Label(self,

                                 textvariable=controller.shared_data["Balance"],
                                 font=("Arial", 13),
                                 fg='white',
                                 bg="#14324d",
                                 anchor='c')
        balance_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#154670')
        button_frame.pack(fill='both', expand=True)

        def menu():
            controller.show_frame('MenuPage')

        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=0, column=0, pady=5)

        def exit():
            controller.show_frame('SignIn')

        exit_button = tk.Button(button_frame,
                                text='EXIT',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=4, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file="maestro.png")
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        express_photo = tk.PhotoImage(file="american-express.png")
        express_label = tk.Label(bottom_frame, image=express_photo)
        express_label.pack(side='left')
        express_label.image = express_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Arial', 12))
        time_label.pack(side='right')

        tick()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

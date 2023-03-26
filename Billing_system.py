from tkinter import *
import random
import datetime

bg_color = "#dbbbf5"
fg_color = "black"
lbl_color = '#0A090C'
date_time = datetime.datetime.now()
panner_tikkac = 120
palak_soupc = 50
tandoori_talakc = 65
Honey_Chickenc = 135
Golden_Fry_Prawnc = 120
Chilli_Fishc = 100
Vegetable_Biriyanic = 120
Aloo_Butter_Masalac = 70
Vegetable_Schezwan_Ricec = 150
Mutton_Biriyanic = 160
Chicken_Noodlesc = 110
Chettinad_Curryc = 90
Hot_Donutc = 60
Chocolate_Fountainc = 80
Phirnic = 40
Kulfic = 30
Ice_Cream_Rollsc = 50


class Billing_system:
    # Define the frame

    def __init__(self, root):
        self.root = root
        self.root.geometry = ("1000*700+0+0")
        self.root.maxsize(width=1360, height=1000)
        self.root.minsize(width=1360, height=1000)
        self.root.title("Hotel Mars Restaurant Billing System")
        self.Tax = IntVar()
        self.Tax_value = IntVar()
        self.total_starters = StringVar()
        self.total_main_course = StringVar()
        self.total_desserts = StringVar()
        self.grand_total = StringVar()

        # VARIABLE
        self.c_name = StringVar()
        self.c_num = StringVar()
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()
        self.c_phone = IntVar()
        self.c_bill_no.set(str(x))

        # STARTERS VARIABLE
        self.panner_tikka = IntVar()
        self.palak_soup = IntVar()
        self.tandoori_talak = IntVar()
        self.Honey_Chicken = IntVar()
        self.Golden_Fry_Prawn = IntVar()
        self.Chilli_Fish = IntVar()

        # MAIN DISH VARIABLE
        self.Vegetable_Biriyani = IntVar()
        self.Aloo_Butter_Masala = IntVar()
        self.Vegetable_Schezwan_Rice = IntVar()
        self.Mutton_Biriyani = IntVar()
        self.Chicken_Noodles = IntVar()
        self.Chettinad_Curry = IntVar()

        # Desserts
        self.Hot_Donut = IntVar()
        self.Chocolate_Fountain = IntVar()
        self.Phirni = IntVar()
        self.Kulfi = IntVar()
        self.Ice_Cream_Rolls = IntVar()

        # TITLE OF RESTAURANT
        title = Label(self.root, text="HOTEL MARS RESTAURANT BILLING SYSTEM", bd=20, relief=RAISED, fg="white",
                      bg="#330C2F", font=("times new roman", 30, "bold"), pady=3).pack(fill=X)
        # Customer Details
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="#0A090C", bg=bg_color,
                        relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=2, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=3, ipadx=30, ipady=4, pady=5)

        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=5, ipady=4, ipadx=30, pady=5)

        bill_btn = Button(F1, text="Reset", bd=7, relief=GROOVE, font=("times new roman", 12, "bold"), bg=bg_color,
                          fg=fg_color)
        bill_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)

        # starters
        F2 = LabelFrame(self.root, text='Starters', bd=10, relief=GROOVE, bg=bg_color, fg="#0A090C",
                        font=("times new roman", 13, "bold"))
        F2.place(x=5, y=180, width=325, height=440)

        panner_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Panner tikka")
        panner_lbl.grid(row=0, column=0, padx=10, pady=20)
        panner_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.panner_tikka)
        panner_en.grid(row=0, column=1, ipady=5, ipadx=5)

        palak_soup_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Palak soup")
        palak_soup_lbl.grid(row=1, column=0, padx=10, pady=20)
        palak_soup_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.palak_soup)
        palak_soup_en.grid(row=1, column=1, ipady=5, ipadx=5)

        tandoori_talak_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                   text="Tandoori talak")
        tandoori_talak_lbl.grid(row=2, column=0, padx=10, pady=20)
        tandoori_talak_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.tandoori_talak)
        tandoori_talak_en.grid(row=2, column=1, ipady=5, ipadx=5)

        Honey_Chicken_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                  text="Honey chicken")
        Honey_Chicken_lbl.grid(row=3, column=0, padx=10, pady=20)
        Honey_Chicken_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Honey_Chicken)
        Honey_Chicken_en.grid(row=3, column=1, ipady=5, ipadx=5)

        Golden_Fry_Prawn_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                     text="fried prawn")
        Golden_Fry_Prawn_lbl.grid(row=4, column=0, padx=10, pady=20)
        Golden_Fry_Prawn_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Golden_Fry_Prawn)
        Golden_Fry_Prawn_en.grid(row=4, column=1, ipady=5, ipadx=5)

        Chilli_Fish_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Chilli Fish")
        Chilli_Fish_lbl.grid(row=5, column=0, padx=10, pady=20)
        Chilli_Fish_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Chilli_Fish)
        Chilli_Fish_en.grid(row=5, column=1, ipady=5, ipadx=5)

        # Main course
        F3 = LabelFrame(self.root, text='Main Course', bd=10, relief=GROOVE, bg=bg_color, fg="#0A090C",
                        font=("times new roman", 13, "bold"))
        F3.place(x=330, y=180, width=330, height=380)

        Vegetable_Biriyani_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                       text="Veg. Biriyani")
        Vegetable_Biriyani_lbl.grid(row=0, column=0, padx=10, pady=20)
        Vegetable_Biriyani_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.Vegetable_Biriyani)
        Vegetable_Biriyani_en.grid(row=0, column=1, ipady=5, ipadx=5)

        Aloo_Butter_Masala_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                       text="Aloo Masala")
        Aloo_Butter_Masala_lbl.grid(row=1, column=0, padx=10, pady=20)
        Aloo_Butter_Masala_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.Aloo_Butter_Masala)
        Aloo_Butter_Masala_en.grid(row=1, column=1, ipady=5, ipadx=5)

        Vegetable_Schezwan_Rice_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                            text="Schezwan Rice")
        Vegetable_Schezwan_Rice_lbl.grid(row=2, column=0, padx=10, pady=20)
        Vegetable_Schezwan_Rice_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.Vegetable_Schezwan_Rice)
        Vegetable_Schezwan_Rice_en.grid(row=2, column=1, ipady=5, ipadx=5)

        Mutton_Biriyani_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                    text="Mutton Biriyani")
        Mutton_Biriyani_lbl.grid(row=3, column=0, padx=10, pady=20)
        Mutton_Biriyani_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.Mutton_Biriyani)
        Mutton_Biriyani_en.grid(row=3, column=1, ipady=5, ipadx=5)

        Chicken_Noodles_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Noodles")
        Chicken_Noodles_lbl.grid(row=4, column=0, padx=10, pady=20)
        Chicken_Noodles_en = Entry(F3, bd=8, relief=GROOVE, textvariable=self.Chicken_Noodles)
        Chicken_Noodles_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # Desserts
        F4 = LabelFrame(self.root, text='Desserts', bd=10, relief=GROOVE, bg=bg_color, fg="#0A090C",
                        font=("times new roman", 13, "bold"))
        F4.place(x=660, y=180, width=335, height=380)

        Hot_Donut_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Hot Donut")
        Hot_Donut_lbl.grid(row=0, column=0, padx=10, pady=20)
        Hot_Donut_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.Hot_Donut)
        Hot_Donut_en.grid(row=0, column=1, ipady=5, ipadx=5)

        Chocolate_Fountain_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                       text="Choco Fountain")
        Chocolate_Fountain_lbl.grid(row=1, column=0, padx=10, pady=20)
        Chocolate_Fountain_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.Chocolate_Fountain)
        Chocolate_Fountain_en.grid(row=1, column=1, ipady=5, ipadx=5)

        Phirni_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Phirni")
        Phirni_lbl.grid(row=2, column=0, padx=10, pady=20)
        Phirni_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.Phirni)
        Phirni_en.grid(row=2, column=1, ipady=5, ipadx=5)

        Kulfi_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Kulfi")
        Kulfi_lbl.grid(row=3, column=0, padx=10, pady=20)
        Kulfi_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.Kulfi)
        Kulfi_en.grid(row=3, column=1, ipady=5, ipadx=5)

        Ice_Cream_Rolls_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                    text="Ice Cream Rolls")
        Ice_Cream_Rolls_lbl.grid(row=4, column=0, padx=10, pady=20)
        Ice_Cream_Rolls_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.Ice_Cream_Rolls)
        Ice_Cream_Rolls_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # Bill Invoice
        F5 = Label(self.root, bd=10, relief=GROOVE)
        F5.place(x=995, y=180, width=360, height=380)
        # ===========
        bill_title = Label(F5, text=" Bill Invoice", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txt = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # tax
        F6 = LabelFrame(self.root, text='Tax', bd=10, relief=GROOVE, bg=bg_color, fg="#0A090C",
                        font=("times new roman", 13, "bold"))
        F6.place(x=5, y=620, width=325, height=70)
        Tax_lbl = Label(F6, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="GST for Food Tax")
        Tax_lbl.grid(row=2, column=1, ipady=5, ipadx=5)
        Tax_en = Entry(F6, bd=3, relief=GROOVE, textvariable=self.Tax)
        Tax_en.grid(row=2, column=3, ipady=1, ipadx=3)

        # total
        F7 = LabelFrame(self.root, text='Total', bd=10, relief=GROOVE, bg=bg_color, fg="#0A090C",
                        font=("times new roman", 13, "bold"))
        F7.place(x=330, y=560, width=1030, height=130)
        total_starters_lbl = Label(F7, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                   text="Total Starters")
        total_starters_lbl.grid(row=0, column=0, padx=5, pady=10)
        total_starters_en = Entry(F7, bd=8, relief=GROOVE, textvariable=self.total_starters)
        total_starters_en.grid(row=0, column=1, ipady=5, ipadx=0)

        total_main_course_lbl = Label(F7, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                      text="Total main course")
        total_main_course_lbl.grid(row=0, column=2, padx=5, pady=10)
        total_main_course_en = Entry(F7, bd=8, relief=GROOVE, textvariable=self.total_main_course)
        total_main_course_en.grid(row=0, column=3, ipady=5, ipadx=0)

        total_desserts_lbl = Label(F7, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                   text="Total Desserts")
        total_desserts_lbl.grid(row=0, column=4, padx=5, pady=10)
        total_desserts_en = Entry(F7, bd=8, relief=GROOVE, textvariable=self.total_desserts)
        total_desserts_en.grid(row=0, column=5, ipady=5, ipadx=0)

        grand_total_lbl = Label(F7, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Grand Total")
        grand_total_lbl.grid(row=1, column=0, padx=5, pady=10)
        grand_total_en = Entry(F7, bd=8, relief=GROOVE, textvariable=self.grand_total)
        grand_total_en.grid(row=1, column=1, ipady=5, ipadx=0)

        # Buttons
        total_btn = Button(F7, text="Grand Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                           relief=GROOVE, command=self.total)
        total_btn.grid(row=1, column=2, ipadx=20, padx=30)

        genbill_btn = Button(F7, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=3, ipadx=20)

        clear_btn = Button(F7, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=1, column=4, ipadx=20, padx=30)

        exit_btn = Button(F7, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=1, column=5, ipadx=20)

    # Caluclation
    def total(self):
        self.total_starters_prices = (
                (self.panner_tikka.get()) * panner_tikkac +
                (self.palak_soup.get()) * palak_soupc +
                (self.tandoori_talak.get()) * tandoori_talakc +
                (self.Honey_Chicken.get()) * Honey_Chickenc +
                (self.Golden_Fry_Prawn.get()) * Golden_Fry_Prawnc +
                (self.Chilli_Fish.get()) * Chilli_Fishc
        )
        self.total_main_course_prices = (
                (self.Vegetable_Biriyani.get()) * Vegetable_Biriyanic +
                (self.Aloo_Butter_Masala.get()) * Aloo_Butter_Masalac +
                (self.Vegetable_Schezwan_Rice.get()) * Vegetable_Schezwan_Ricec +
                (self.Mutton_Biriyani.get()) * Mutton_Biriyanic +
                (self.Chicken_Noodles.get()) * Chicken_Noodlesc
        )
        self.total_desserts_prices = (
                (self.Hot_Donut.get()) * Hot_Donutc +
                (self.Chocolate_Fountain.get()) * Chocolate_Fountainc +
                (self.Phirni.get()) * Phirnic +
                (self.Kulfi.get()) * Kulfic +
                (self.Ice_Cream_Rolls.get()) * Ice_Cream_Rollsc
        )
        self.grand_prices = (self.total_starters_prices + self.total_main_course_prices + self.total_desserts_prices)
        self.Tax_value = round(self.grand_prices * (self.Tax.get() / 100))
        self.grand_prices_tax = self.grand_prices + self.Tax_value
        self.total_starters.set("Rs. " + str(self.total_starters_prices))
        self.total_main_course.set("Rs. " + str(self.total_main_course_prices))
        self.total_desserts.set("Rs. " + str(self.total_desserts_prices))
        self.grand_total.set("Rs. " + str(self.grand_prices_tax))

    def customer_details(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "    Welcome To Hotel Mars Restaurant\n")
        self.txt.insert(END,
                        f"\nDate:- {date_time.day}/{date_time.month}/{date_time.year}         Time:- {date_time.hour}:{date_time.minute}")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.c_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n=======================================")
        self.txt.insert(END, "\nProduct             Qty         Price")
        self.txt.insert(END, "\n=======================================")

    def bill_area(self):
        self.customer_details()
        if self.panner_tikka.get() != 0:
            self.txt.insert(END,
                            f"\nPanner Tikka        {self.panner_tikka.get()}           {self.panner_tikka.get() * panner_tikkac}")
        if self.palak_soup.get() != 0:
            self.txt.insert(END,
                            f"\nPalak Soup          {self.palak_soup.get()}           {self.palak_soup.get() * palak_soupc}")
        if self.tandoori_talak.get() != 0:
            self.txt.insert(END,
                            f"\nTandoori Talak      {self.tandoori_talak.get()}           {self.tandoori_talak.get() * tandoori_talakc}")
        if self.Honey_Chicken.get() != 0:
            self.txt.insert(END,
                            f"\nHoney Chicken       {self.Honey_Chicken.get()}           {self.Honey_Chicken.get() * Honey_Chickenc}")
        if self.Golden_Fry_Prawn.get() != 0:
            self.txt.insert(END,
                            f"\nGolden Fry Prawn    {self.Golden_Fry_Prawn.get()}           {self.Golden_Fry_Prawn.get() * Golden_Fry_Prawnc}")
        if self.Chilli_Fish.get() != 0:
            self.txt.insert(END,
                            f"\nChilli Fish         {self.Chilli_Fish.get()}           {self.Chilli_Fish.get() * Chilli_Fishc}")
        if self.Vegetable_Biriyani.get() != 0:
            self.txt.insert(END,
                            f"\nVeg. Biriyani       {self.Vegetable_Biriyani.get()}           {self.Vegetable_Biriyani.get() * Vegetable_Biriyanic}")
        if self.Aloo_Butter_Masala.get() != 0:
            self.txt.insert(END,
                            f"\nAloo Butter Masala  {self.Aloo_Butter_Masala.get()}           {self.Aloo_Butter_Masala.get() * Aloo_Butter_Masalac}")
        if self.Vegetable_Schezwan_Rice.get() != 0:
            self.txt.insert(END,
                            f"\nVeg. Schezwan Rice  {self.Vegetable_Schezwan_Rice.get()}           {self.Vegetable_Schezwan_Rice.get() * Vegetable_Biriyanic}")
        if self.Mutton_Biriyani.get() != 0:
            self.txt.insert(END,
                            f"\nMutton Biriyani     {self.Mutton_Biriyani.get()}           {self.Mutton_Biriyani.get() * Mutton_Biriyanic}")
        if self.Chicken_Noodles.get() != 0:
            self.txt.insert(END,
                            f"\nChicken Noodles     {self.Chicken_Noodles.get()}           {self.Chicken_Noodles.get() * Chicken_Noodlesc}")
        if self.Chettinad_Curry.get() != 0:
            self.txt.insert(END,
                            f"\nChettinad Curry       {self.Chettinad_Curry.get()}           {self.Chettinad_Curry.get() * Chettinad_Curryc}")
        if self.Hot_Donut.get() != 0:
            self.txt.insert(END,
                            f"\nHot Donut           {self.Hot_Donut.get()}           {self.Hot_Donut.get() * Hot_Donutc}")
        if self.Chocolate_Fountain.get() != 0:
            self.txt.insert(END,
                            f"\nChoco Fountain      {self.Chocolate_Fountain.get()}           {self.Chocolate_Fountain.get() * Chocolate_Fountainc}")
        if self.Phirni.get() != 0:
            self.txt.insert(END, f"\nPhirni              {self.Phirni.get()}           {self.Phirni.get() * Phirnic}")
        if self.Kulfi.get() != 0:
            self.txt.insert(END, f"\nKulfi               {self.Kulfi.get()}           {self.Kulfi.get() * Kulfic}")
        if self.Ice_Cream_Rolls.get() != 0:
            self.txt.insert(END,
                            f"\nIce cream Rolls     {self.Ice_Cream_Rolls.get()}           {self.Ice_Cream_Rolls.get() * Ice_Cream_Rollsc}")
        if self.Tax.get() != 0:
            self.txt.insert(END,
                            f"\n=======================================\nTax                 {self.Tax.get()}%          {self.Tax_value}")
        self.txt.insert(END, f"\n=======================================\n")
        self.txt.insert(END,
                        f"Total                           {self.grand_prices_tax}\n=======================================\n         Thank you, Visit again")

        def save_button(self):
            file1 = open(r"C:\Users\SasiMalu\OneDrive\Documents\INTERNSHIP\MyFile.txt", "w")
            file1.write("    Welcome To Hotel Mars Restaurant\n")
            file1.write(
                f"\nDate:- {date_time.day}/{date_time.month}/{date_time.year}         Time:- {date_time.hour}:{date_time.minute}")
            file1.write(f"\nBill No. : {str(self.c_bill_no.get())}")
            file1.write(f"\nCustomer Name : {str(self.c_name.get())}")
            file1.write(f"\nPhone No. : {str(self.c_phone.get())}")
            file1.write("\n=======================================")
            file1.write("\nProduct             Qty         Price")
            file1.write("\n=======================================")

            if self.panner_tikka.get() != 0:
                file1.write(
                    f"\nPanner Tikka        {self.panner_tikka.get()}           {self.panner_tikka.get() * panner_tikkac}")
            if self.palak_soup.get() != 0:
                file1.write(
                    f"\nPalak Soup          {self.palak_soup.get()}           {self.palak_soup.get() * palak_soupc}")
            if self.tandoori_talak.get() != 0:
                file1.write(
                    f"\nTandoori Talak      {self.tandoori_talak.get()}           {self.tandoori_talak.get() * tandoori_talakc}")
            if self.Honey_Chicken.get() != 0:
                file1.write(
                    f"\nHoney Chicken       {self.Honey_Chicken.get()}           {self.Honey_Chicken.get() * Honey_Chickenc}")
            if self.Golden_Fry_Prawn.get() != 0:
                file1.write(
                    f"\nGolden Fry Prawn    {self.Golden_Fry_Prawn.get()}           {self.Golden_Fry_Prawn.get() * Golden_Fry_Prawnc}")
            if self.Chilli_Fish.get() != 0:
                file1.write(
                    f"\nChilli Fish         {self.Chilli_Fish.get()}           {self.Chilli_Fish.get() * Chilli_Fishc}")
            if self.Vegetable_Biriyani.get() != 0:
                file1.write(
                    f"\nVeg. Biriyani       {self.Vegetable_Biriyani.get()}           {self.Vegetable_Biriyani.get() * Vegetable_Biriyanic}")
            if self.Aloo_Butter_Masala.get() != 0:
                file1.write(
                    f"\nAloo Butter Masala  {self.Aloo_Butter_Masala.get()}           {self.Aloo_Butter_Masala.get() * Aloo_Butter_Masalac}")
            if self.Vegetable_Schezwan_Rice.get() != 0:
                file1.write(
                    f"\nVeg. Schezwan Rice  {self.Vegetable_Schezwan_Rice.get()}           {self.Vegetable_Schezwan_Rice.get() * Vegetable_Biriyanic}")
            if self.Mutton_Biriyani.get() != 0:
                file1.write(
                    f"\nMutton Biriyani     {self.Mutton_Biriyani.get()}           {self.Mutton_Biriyani.get() * Mutton_Biriyanic}")
            if self.Chicken_Noodles.get() != 0:
                file1.write(
                    f"\nChicken Noodles     {self.Chicken_Noodles.get()}           {self.Chicken_Noodles.get() * Chicken_Noodlesc}")
            if self.Chettinad_Curry.get() != 0:
                file1.write(
                    f"\nChettinad Curry       {self.Chettinad_Curry.get()}           {self.Chettinad_Curry.get() * Chettinad_Curryc}")
            if self.Hot_Donut.get() != 0:
                file1.write(
                    f"\nHot Donut           {self.Hot_Donut.get()}           {self.Hot_Donut.get() * Hot_Donutc}")
            if self.Chocolate_Fountain.get() != 0:
                file1.write(
                    f"\nChoco Fountain      {self.Chocolate_Fountain.get()}           {self.Chocolate_Fountain.get() * Chocolate_Fountainc}")
            if self.Phirni.get() != 0:
                file1.write(f"\nPhirni              {self.Phirni.get()}           {self.Phirni.get() * Phirnic}")
            if self.Kulfi.get() != 0:
                file1.write(f"\nKulfi               {self.Kulfi.get()}           {self.Kulfi.get() * Kulfic}")
            if self.Ice_Cream_Rolls.get() != 0:
                file1.write(
                    f"\nIce cream Rolls     {self.Ice_Cream_Rolls.get()}           {self.Ice_Cream_Rolls.get() * Ice_Cream_Rollsc}")
            if self.Tax.get() != 0:
                file1.write(
                    f"\n=======================================\nTax                 {self.Tax.get()}%          {self.Tax_value}")
            file1.write(f"\n=======================================")
            file1.write(
                f"\nTotal                           {self.grand_prices_tax}\n=======================================\n         Thank you, Visit again")

        btn = Button(root, bd=7, relief=GROOVE, font=("times new roman", 12, "bold"), bg=bg_color, fg=fg_color,
                     text='PRINT', command=lambda: save_button(self))
        btn.pack(ipady=5, padx=60, ipadx=19, pady=5)
        btn.place(x=1200, y=110)

        root.mainloop()

    def clear(self):
        self.txt.delete('1.0', END)

    def exit(self):
        self.root.destroy()


root = Tk()
object = Billing_system(root)
root.mainloop()

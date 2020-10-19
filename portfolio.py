import tkinter as tk
from PIL import ImageTk, Image

MIN_FIRSTYEAR = 2018
MAX_FIRSTYEAR = 2020
MAX_TIME_PERIOD = 33
MIN_TIME_PERIOD = 5
MAX_COMP_SHARE = 60
MIN_COMP_SHARE = 1
MIN_COMP_GROWTH = 0
MAX_COMP_GROWTH = 5
MIN_CASES = 10000
MAX_CASES = 10000000
MAX_GROWTH = 15
MIN_GROWTH = 0


class MainApplication(tk.Frame):
    '''
    By: Dirk Mueller, Apr 3, 2018
    Software version = Python 3.8.3
    This program is intended to model a product portfolio that successively,
    by launching new products, cannibalizes a product (marked as no. 1).

    As INPUT the software takes the:
    - market size
    - growth of market size
    - existing company share of the total market
    - projected change in company share
    - launch year & time to saturation (with linear increase) for 4 products
    - saturation level of product share in % (with respect to company share)

    A max of 4 new products can be added for a portfolio of max. 5 products.

    The OUTPUT of the software is:
    - company market share in units per year
    - product market share in units per year
    '''

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.image = ImageClass(self)
        self.yeardef = YearDefinition(self)
        self.companydef = CompanyDefinition(self)
        self.casedef = Cases(self)
        self.saturation = SaturationofProducts(self)
        self.launchyrssat = LaunchYearofProducts(self)
        self.errormessage = ErrorMessage(self)
        self.signature = Signature(self)
        self.buttons = Buttons(self, self.yeardef, self.companydef,
                               self.casedef, self.saturation,
                               self.launchyrssat, self.errormessage)


class ImageClass(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        txt = 'Portfolio Creator'
        self.toplabel = tk.Label(root, text=txt, font=(None, 18))
        self.toplabel.grid(row=0, column=0, columnspan=4)
        fname = "portfolio_scaled.png"
        self.img = Image.open(fname)
        self.disp = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(root, image=self.disp).grid(row=1, column=0, 
                                                          columnspan=4)


class YearDefinition(tk.Frame):

    def __init__(self, parent):
        txt = 'First year (yr): '
        self.label = tk.Label(root, text=txt).grid(row=2, column=0)
        self.startyear = tk.StringVar()
        self.startyear = tk.Entry(root, width=12, textvariable=self.startyear)
        self.startyear.grid(row=2, column=1)
        self.startyear.insert(10, '2018')

        self.label = tk.Label(root, text='Time period (yrs): '). \
            grid(row=3, column=0)
        self.timeperiod = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.timeperiod)
        self.entry.grid(row=3, column=1)
        self.entry.insert(10, '10')


class CompanyDefinition(tk.Frame):
    def __init__(self, parent):
        self.label = tk.Label(root, text='Company market share (%): '). \
            grid(row=4, column=0)
        self.sharecompany = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.sharecompany)
        self.entry.grid(row=4, column=1)
        self.entry.insert(10, '30.0')
        self.label = tk.Label(root, text='Company growth (%): '). \
            grid(row=5, column=0)
        self.growthcompany = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.growthcompany)
        self.entry.grid(row=5, column=1)
        self.entry.insert(10, '1.0')


class Cases(tk.Frame):
    def __init__(self, parent):
        self.label = tk.Label(root, text='Amount of cases: '). \
            grid(row=6, column=0)
        self.cases = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.cases)
        self.entry.grid(row=6, column=1)
        self.entry.insert(10, '100000')

        self.label = tk.Label(root, text='Annual case growth (%): '). \
            grid(row=7, column=0)
        self.growth = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.growth)
        self.entry.grid(row=7, column=1)
        self.entry.insert(10, '3.5')


class SaturationofProducts(tk.Frame):
    def __init__(self, parent):
        self.label = tk.Label(root, text='Saturation of prod 2 (%): '). \
            grid(row=7, column=0)
        self.prod2sat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod2sat)
        self.entry.grid(row=7, column=1)
        self.entry.insert(10, '25.0')

        self.label = tk.Label(root, text='Years->sat of prod 2 (yrs): '). \
            grid(row=7, column=2)
        self.prod2yrstosat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod2yrstosat)
        self.entry.grid(row=7, column=3)
        self.entry.insert(10, '4')

        self.label = tk.Label(root, text='Saturation of prod 3 (%): '). \
            grid(row=8, column=0)
        self.prod3sat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod3sat)
        self.entry.grid(row=8, column=1)
        self.entry.insert(10, '20.0')

        self.label = tk.Label(root, text='Years->sat of prod 3 (yrs): '). \
            grid(row=8, column=2)
        self.prod3yrstosat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod3yrstosat)
        self.entry.grid(row=8, column=3)
        self.entry.insert(10, '3')

        self.label = tk.Label(root, text='Saturation of prod 4 (%): '). \
            grid(row=9, column=0)
        self.prod4sat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod4sat)
        self.entry.grid(row=9, column=1)
        self.entry.insert(10, '30.0')

        self.label = tk.Label(root, text='Years->sat of prod 4 (yrs): '). \
            grid(row=9, column=2)
        self.prod4yrstosat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod4yrstosat)
        self.entry.grid(row=9, column=3)
        self.entry.insert(10, '2')

        self.label = tk.Label(root, text='Saturation of prod 5 (%): '). \
            grid(row=10, column=0)
        self.prod5sat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod5sat)
        self.entry.grid(row=10, column=1)
        self.entry.insert(10, '10.0')

        self.label = tk.Label(root, text='Years->sat of prod 5 (yrs): '). \
            grid(row=10, column=2)
        self.prod5yrstosat = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod5yrstosat)
        self.entry.grid(row=10, column=3)
        self.entry.insert(10, '3')


class LaunchYearofProducts(tk.Frame):
    def __init__(self, parent):

        self.label = tk.Label(root, text='Launch year of prod 2 (yr): '). \
            grid(row=11, column=0)
        self.prod2startyr = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod2startyr)
        self.entry.grid(row=11, column=1)
        self.entry.insert(10, '2020')

        self.label = tk.Label(root, text='Launch year of prod 3 (yr): '). \
            grid(row=12, column=0)
        self.prod3startyr = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod3startyr)
        self.entry.grid(row=12, column=1)
        self.entry.insert(10, '2020')

        self.label = tk.Label(root, text='Launch year of prod 4 (yr): '). \
            grid(row=11, column=2)
        self.prod4startyr = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod4startyr)
        self.entry.grid(row=11, column=3)
        self.entry.insert(11, '2019')

        self.label = tk.Label(root, text='Launch year of prod 5 (yr): '). \
            grid(row=12, column=2)
        self.prod5startyr = tk.StringVar()
        self.entry = tk.Entry(root, width=12, textvariable=self.prod5startyr)
        self.entry.grid(row=12, column=3)
        self.entry.insert(10, '2021')


class ErrorMessage(tk.Frame):
    def __init__(self, parent):
        self.labelerror = tk.Label(root, text='',
                                   font=(None, 10), fg="red")
        self.labelerror.grid(row=15, column=0, columnspan=4)


class Signature(tk.Frame):
    def __init__(self, parent):
        txt = 'Version 1.0 \n Dirk Mueller \n Oct 19, 2020'
        self.siglabel = tk.Label(root, text=txt, font=(None, 10),
                                 foreground="gray", anchor=tk.E)
        self.siglabel.grid(row=16, column=0)


class Buttons(tk.Frame):
    def __init__(self, parent, yeardef, compdef, casedef, saturation,
                 launchyear, errmsg):
        self.yeardef = yeardef
        self.compdef = compdef
        self.casedef = casedef
        self.saturation = saturation
        self.launchyear = launchyear
        self.clearedallchecks = True
        self.errmsg = errmsg
        self.okButton = tk.Button(root, text='Ok', width=10,
                                  command=self.processInput)
        self.okButton.grid(row=16, column=2)
        self.cancelButton = tk.Button(root, text='Cancel', width=10,
                                      command=root.destroy)
        self.cancelButton.grid(row=16, column=3)

    def processInput(self):
        self.listbox = tk.Text(root)
        self.listbox.grid(row=17, column=0, columnspan=4)

        # Initialize variables for sanity check in processInput():
        self.fy, self.tp = 0, 0
        self.shcomp, self.grwcomp = 0.0, 0.0
        self.grw = 0.0
        self.cs = 0
        self.pr2sat, self.pr3sat = 0.0, 0.0
        self.pr4sat, self.pr5sat = 0.0, 0.0
        self.pr2yrs, self.pr3yrs = 0.0, 0.0
        self.pr4yrs, self.pr5yrs = 0.0, 0.0
        self.pr2sta, self.pr3sta = 0, 0
        self.pr4sta, self.pr5sta = 0, 0
        self.timebar = []
        try:
            self.fy = abs(int(self.yeardef.startyear.get()))
        except ValueError:
            self.errmsg.labelerror.config(text="Time period not an integer!")
            return
        try:
            self.tp = abs(int(self.yeardef.timeperiod.get()))
        except ValueError:
            self.errmsg.labelerror.config(text="Time period not an integer!")
            return
        try:
            self.shcomp = abs(float(self.compdef.sharecompany.get()))
        except ValueError:
            self.ausgabe.config(text="Company market share not a number!")
            return
        try:
            self.grwcomp = abs(float(self.compdef.growthcompany.get()))
        except ValueError:
            self.ausgabe.config(text="Company growth not a number!")
            return
        try:
            self.cs = abs(int(self.casedef.cases.get()))
        except ValueError:
            self.ausgabe.config(text="Amount of cases not an integer!")
            return
        try:
            self.grw = abs(float(self.casedef.growth.get()))
        except ValueError:
            self.ausgabe.config(text="Market growth not a number!")
            return
        try:
            self.pr2sat = abs(float(self.saturation.prod2sat.get()))
        except ValueError:
            txt = "Saturation level of prod 2 not a number!"
            self.ausgabe.config(text=txt)
            return
        try:
            self.pr3sat = abs(float(self.saturation.prod3sat.get()))
        except ValueError:
            txt = "Saturation level of prod 3 not a number!"
            self.ausgabe.config(text=txt)
            return
        try:
            self.pr4sat = abs(float(self.saturation.prod4sat.get()))
        except ValueError:
            txt = "Saturation level of prod 4 not a number!"
            self.ausgabe.config(text=txt)
            return
        try:
            self.pr5sat = abs(float(self.saturation.prod5sat.get()))
        except ValueError:
            txt = "Saturation level of prod 5 not a number!"
            self.ausgabe.config(text=txt)
            return
        try:
            self.pr2yrs = abs(int(self.saturation.prod2yrstosat.get()))
        except ValueError:
            self.ausgabe.config(text="Years->sat of prod 2 not a number!")
            return
        try:
            self.pr3yrs = abs(int(self.saturation.prod3yrstosat.get()))
        except ValueError:
            self.ausgabe.config(text="Years->sat of prod 3 not a number!")
            return
        try:
            self.pr4yrs = abs(int(self.saturation.prod4yrstosat.get()))
        except ValueError:
            self.ausgabe.config(text="Years->sat of prod 4 not a number!")
            return
        try:
            self.pr5yrs = abs(int(self.saturation.prod5yrstosat.get()))
        except ValueError:
            self.ausgabe.config(text="Years->sat of prod 5 not a number!")
            return
        try:
            self.pr2sta = abs(int(self.launchyear.prod2startyr.get()))
        except ValueError:
            self.ausgabe.config(text="Launch year of prod 2 not a number!!")
            return
        try:
            self.pr3sta = abs(int(self.launchyear.prod3startyr.get()))
        except ValueError:
            self.ausgabe.config(text="Launch year of prod 3 not a number!!")
            return
        try:
            self.pr4sta = abs(int(self.launchyear.prod4startyr.get()))
        except ValueError:
            self.ausgabe.config(text="Launch year of prod 4 not a number!!")
            return
        try:
            self.pr5sta = abs(int(self.launchyear.prod5startyr.get()))
        except ValueError:
            self.ausgabe.config(text="Launch year of prod 5 not a number!!")
            return
        if (self.fy > MAX_FIRSTYEAR or self.fy < MIN_FIRSTYEAR):
            self.errmsg.labelerror.config(text='First year out of range')
            return
        if (self.tp > MAX_TIME_PERIOD or self.tp < MIN_TIME_PERIOD):
            self.errmsg.labelerror.config(text='Time period out of range')
            return
        if (self.shcomp > MAX_COMP_SHARE or self.shcomp < MIN_COMP_SHARE):
            self.errmsg.labelerror.config(text='Company share out of range')
            return
        if (self.grwcomp > MAX_COMP_GROWTH or self.grwcomp < MIN_COMP_GROWTH):
            self.errmsg.labelerror.config(text='Company growth out of range')
            return
        if (self.cs > MAX_CASES or self.cs < MIN_CASES):
            self.errmsg.labelerror.config(text='Amount of cases out of range')
            return
        if (self.grw > MAX_GROWTH or self.grw < MIN_GROWTH):
            txt = 'Annual growth out of range'
            self.errmsg.labelerror.config(text=txt)
            return
        if (self.pr2yrs > MAX_TIME_PERIOD or self.tp < MIN_TIME_PERIOD):
            txt = 'Time period for prod 2 out of range'
            self.errmsg.labelerror.config(text=txt)
            return
        if (self.pr3yrs > MAX_TIME_PERIOD or self.tp < MIN_TIME_PERIOD):
            txt = 'Time period for prod 3 out of range'
            self.errmsg.labelerror.config(text=txt)
            return
        if (self.pr4yrs > MAX_TIME_PERIOD or self.tp < MIN_TIME_PERIOD):
            txt = 'Time period for prod 4 out of range'
            self.errmsg.labelerror.config(text=txt)
            return
        if (self.pr5yrs > MAX_TIME_PERIOD or self.tp < MIN_TIME_PERIOD):
            txt = 'Time period for prod 5 out of range'
            self.errmsg.labelerror.config(text=txt)
            return
        if self.pr2sat + self.pr3sat + self.pr4sat + self.pr5sat > 100.0:
            txt = 'Sum of saturation levels of products 2-5'
            txt = txt + ' cannot be larger than 100%'
            self.errmsg.labelerror.config(text=txt)
            return
        if self.pr2sta + self.pr2yrs > self.fy + self.tp:
            txt = 'Sum of start year of prod 2 and years'
            txt = txt + '->sat is larger than whole time period!'
            self.errmsg.labelerror.config(text=txt)
            return
        if self.pr3sta + self.pr3yrs > self.fy + self.tp:
            txt = 'Sum of start year of prod 3 and years'
            txt = txt + '->sat is larger than whole time period!'
            self.errmsg.labelerror.config(text=txt)
            return
        if self.pr4sta + self.pr4yrs > self.fy + self.tp:
            txt = 'Sum of start year of prod 4 and years'
            txt = txt + '->sat is larger than whole time period!'
            self.errmsg.labelerror.config(text=txt)
            return
        if self.pr5sta + self.pr5yrs > self.fy + self.tp:
            txt = 'Sum of start year of prod 5 and years'
            txt = txt + '->sat is larger than whole time period!'
            self.errmsg.labelerror.config(text=txt)
            return
        self.errmsg.labelerror.config(text="")
        self.listbox.insert(tk.END, 'Time period: ' +
                            str(self.tp) + ' y, Company share: ' +
                            str(self.shcomp) +
                            ' %, Annual growth ' + str(self.grw) + ' %')
        self.establishTimeLine()
        self.calculateLinearGrowth()
        self.calculateCompanyshare()
        self.calculateProductShares2to5()
        self.calculateProductShare1()
        self.timebar = ['\nYear'] + self.timebar
        self.sharesofCompany = ['Share of Company'] + self.sharesofCompany
        self.annualamountofcases = ['Cases'] + self.annualamountofcases

    def establishTimeLine(self):
        for year in range(0, self.tp):
            self.timebar.append(year + self.fy)
        self.listbox.insert(tk.END, '\nTimebar: ')
        self.listbox.insert(tk.END, self.timebar)
        return self.timebar

    def calculateLinearGrowth(self):
        caseyear = self.cs
        self.annualamountofcases = [caseyear]
        for year in range(1, len(self.timebar)):
            cases = int(round((1 + self.grw / 100) * caseyear, 0))
            self.annualamountofcases.append(cases)
            caseyear = cases
        self.listbox.insert(tk.END, '\nCases: ')
        self.listbox.insert(tk.END, self.annualamountofcases)
        return self.annualamountofcases

    def calculateCompanyshare(self):
        self.sharesofCompany = []
        # Calculate Company's share of the market in year 0:
        self.sharesofCompany.append(int(round(self.annualamountofcases[0] *
                                              self.shcomp / 100, 0)))
        # Calculate Company's share of the market in year 1:
        runningCompanyshare = self.shcomp + self.grwcomp
        for year in range(1, len(self.annualamountofcases)):
            c = int(round(self.annualamountofcases[year] *
                          runningCompanyshare / 100, 0))
            runningCompanyshare += self.grwcomp
            self.sharesofCompany.append(c)
        self.listbox.insert(tk.END, '\nCompany units: ')
        self.listbox.insert(tk.END, self.sharesofCompany)
        return self.sharesofCompany

    def calculateProductShares2to5(self):
        pr2to5sta = [self.pr2sta, self.pr3sta, self.pr4sta, self.pr5sta]
        pr2to5yrs = [self.pr2yrs, self.pr3yrs, self.pr4yrs, self.pr5yrs]
        pr2to5sat = [self.pr2sat, self.pr3sat, self.pr4sat, self.pr5sat]
        self.p2to5cases = [[] for i in range(4)]
        for j in range(4):
            diffbefore = pr2to5sta[j] - self.timebar[0]
            # Set units to zero for the years before launch:
            for i in range(0, diffbefore):
                self.p2to5cases[j].append(0)
            # Calculate the units for the rising section:
            for year in range(1, pr2to5yrs[j]):
                cases = int(round(self.sharesofCompany[diffbefore + year - 1] *
                                  pr2to5sat[j] / 100.0 / pr2to5yrs[j] * year, 2))
                self.p2to5cases[j].append(cases)
            casessofar = len(self.p2to5cases[j])
            diffafter = len(self.timebar) - casessofar
            # Calculate the units from 1st year of saturation to end of timebar:
            for year in range(0, diffafter):
                cases = int(round(self.sharesofCompany[casessofar + year] *
                                  pr2to5sat[j] / 100, 0))
                self.p2to5cases[j].append(cases)
            self.listbox.insert(tk.END, '\nCases for product ' + str(j+2) + ': ')
            self.listbox.insert(tk.END, self.p2to5cases[j])
        return self.p2to5cases

    def calculateProductShare1(self):
        self.p1cases = []
        for year in range(0, len(self.timebar)):
            p1inyear = self.sharesofCompany[year] - \
                       self.p2to5cases[0][year] - \
                       self.p2to5cases[1][year] - \
                       self.p2to5cases[2][year] - \
                       self.p2to5cases[3][year]
            self.p1cases.append(p1inyear)
        self.listbox.insert(tk.END, '\nCases for product 1: ')
        self.listbox.insert(tk.END, self.p1cases)
        return self.p1cases


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApplication(root)
    w = 700 # width for the Tk root
    h = 800 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # x and y coordinates for the Tk root window
    x = 0
    y = 0

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.mainloop()
## Successive cannabalization of base product to maintain product portfolio
**********************************************
Software:	&emsp;	Python 3.8.3

Version:	&emsp;  1.0

Date: 	&emsp;		Oct 19, 2020

Author:	&emsp;		Dirk Mueller
**********************************************

**Purpose**

This program models a product portfolio that, by successive launches of new products, cannibalizes a base product.


**Libraries**

The following libraries were used:
- tkinter
- PIL


**Input**

As input the software takes the:
  - market size
  - growth of market size
  - existing company share of the total market
  - projected change in company share
  - launch year & time to saturation (with linear increase) for 4 products
  - saturation level of product share in % (with respect to company share)

A max of 4 new products can be added to form a portfolio of a total of 5 products.


**Output**

The output of the software is:
  - company market share in units per year
  - product market share in units per year


**Architecture**

Classes and methods are been used.


**GUIs**

![](https://github.com/DirkMueller8/product_portfolio/blob/master/landing_page.png)

*Fig 1: The successive cannabalization process for a base product, and the landing (input) page.*


![](https://github.com/DirkMueller8/product_portfolio/blob/master/result_page.png)

*Fig 2: Results page with the calculated annual numbers.*


**Source code**

Example of the source code:

```Python
class ImageClass(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        txt = 'Portfolio Creator'
        self.toplabel = tk.Label(root, text=txt, font=(None, 18))
        self.toplabel.grid(row=0, column=0, columnspan=4)
        fname = "portfolio_scaled.png"
        self.img = Image.open(fname)
        self.disp = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(root, image=self.disp).grid(row=1, column=0, columnspan=4)

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
```
![](https://github.com/DirkMueller8/product_portfolio/blob/master/snapshot.png)

*Fig 3: Excerpt of code showing the tkinter class.*

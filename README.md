## Successive cannabalization of base product to maintain product portfolio
**********************************************
Software:		Python 3.8.3

Version:	  1.0

Date: 			Oct 19, 2020

Author:			Dirk Mueller
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

# Source code

Example of the source code:

![](https://github.com/DirkMueller8/product_portfolio/blob/master/snapshot.png)

*Fig 3: Excerpt of code showing the tkinter class.*
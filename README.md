## Successive cannabalization of product portfolio
**********************************************
Software:		Python 3.8.3

Version Number:	1.0

Date: 			Oct 19, 2020

Author:			Dirk Mueller
**********************************************
This program models a product portfolio that successively, by launching new products, cannibalizes a base product (marked as no. 1).

Libraries used:
- tkinter
- PIL

As INPUT the software takes the:
  - market size
  - growth of market size
  - existing company share of the total market
  - projected change in company share
  - launch year & time to saturation (with linear increase) for 4 products
  - saturation level of product share in % (with respect to company share)

A max of 4 new products can be added for a portfolio of max. total of 5 products.

The OUTPUT of the software is:
  - company market share in units per year
  - product market share in units per year

Classes and methods are been used.

Schematic drawing:

![alt text](https://github.com/DirkMueller8/product_portfolio/blob/master/portfolio_scaled.png "The successive cannabalization process for a base product 1, and abbreviations used in the software.")

Example of the source code:

![alt text](https://github.com/DirkMueller8/product_portfolio/blob/master/snapshot.png "Excerpt of code showing the tkinter class")
# Python-GoogleSheetsAPI
Financial Data Visualization , Investment Portfolio Tracker

This project is about to make an interactive google sheets where i can load financial data and my investment portfolio data and visualize it.
This is the current state of the Google Sheet: https://docs.google.com/spreadsheets/d/1KCCA1KbXo38Av-ykWCWWE7SX8oST2ilE6HsmXZfG-Iw/edit?usp=sharing
## This is my roadmap / project plan

Set Up Google Sheets API:
- gspred library

Load Stock Data and Update Google Sheets
- yfinance library to load the data into a Pandas DataFrame
- make financial calculations and update the dataframe
- upload the data to the Google Sheets

Create Interactive Dashboard
- formulas, charts, and tables to visualize the financial data
- create the interactive elements
- customize the appearance

# Make the Google Sheets Reactive - 

Set up a Trigger in Google Sheets:
- create a dropdown or any other form (where the desired company can be select)
- Google Sheets script to set up an onEdit trigger that detects changes in the cell containing the selected company.

Write a Custom Script Function:
- write a custom script function that gets triggered when the company selection changes.

Set Up a Python Server to Receive Requests:
- using a framework like Flask or Django.
- set up an endpoint (URL) that can receive the HTTP request sent from the Google 

Respond to the Request:
- response back the data to the Google Sheets script function.

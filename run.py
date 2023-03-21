import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('DailySales')


def sales_data():
    """
    Get end of day sales totals by department
    """
    print('Please enter sales by department')
    print('Figures should be in the format requested')
    print('Example dd/mm/yyyy or 1234.56 \n')

    returned_date = input("Please enter todays Date here dd/mm/yyyy: ")
    print(f"Date provided: {returned_date} \n")

    returned_hot_food = input("Please enter todays hot food sales format: 1234.56: ")
    print(f"Hot food sales where {returned_hot_food}\n")

    returned_cakes = input("Please enter todays cake sales, format: 1234.56: ")
    print(f"Cake sales where {returned_cakes}\n")

    returned_bread = input("Please enter todays bread sales, format: 1234.56: ")
    print(f"Bread sales where {returned_bread}\n")

    returned_coffee = input("Please enter todays coffee sales, format: 1234.56: ")
    print(f"Coffee sales where {returned_coffee}\n")

    returned_0_vat = input("Please enter todays 0% VAT sales, format: 1234.56: ")
    print(f"0% VAT sales where {returned_0_vat}\n")

    returned_wine = input("Please enter todays wine sales, format: 1234.56: ")
    print(f"Wine sales where {returned_wine}\n")

    returned_chilled = input("Please enter todays Chilled goods sales, format: 1234.56: ")
    print(f"Chilled goods sales where {returned_chilled}\n")

    returned_minerals = input("Please enter todays mineral sales, format: 1234.56: ")
    print(f"Minerals sales where {returned_minerals}\n")

    returned_sweets = input("Please enter todays sweet sales, format: 1234.56: ")
    print(f"Sweets sales where {returned_sweets}\n")

    returned_chocolate = input("Please enter todays chocolate sales, format: 1234.56: ")
    print(f"chocolate sales where {returned_chocolate}\n")

    total_sales = (2*8)
    print(f'Thank you todays total sales {total_sales}\n')


sales_data() 
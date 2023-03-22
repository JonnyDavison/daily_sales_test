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
    print('Please enter todays sales by department')
    print('Figures should be in the format requested')
    print('Example dd/mm/yyyy or 1234.56 \n')

    returned_date = (input("Please enter todays Date here dd/mm/yyyy: "))
    print(f"Date provided: {returned_date} \n")
    
    returned_hot_food = float(input("Please enter hot food sales eg 12.34: "))
    print(f"Hot food sales where {returned_hot_food}\n")

    returned_cakes = float(input("Please enter cake sales, eg 12.34: "))
    print(f"Cake sales where {returned_cakes}\n")

    returned_bread = float(input("Please enter bread sales, eg 12.34: "))
    print(f"Bread sales where {returned_bread}\n")

    returned_coffee = float(input("Please enter coffee sales, eg 12.34: "))
    print(f"Coffee sales where {returned_coffee}\n")

    returned_0_vat = float(input("Please enter 0% VAT sales, eg 12.34: "))
    print(f"0% VAT sales where {returned_0_vat}\n")

    returned_wine = float(input("Please enter wine sales, eg 12.34: "))
    print(f"Wine sales where {returned_wine}\n")

    returned_chilled = float(input("Please enter Chilled sales, eg 12.34: "))
    print(f"Chilled goods sales where {returned_chilled}\n")

    returned_minerals = float(input("Please enter mineral sales, eg 12.34: "))
    print(f"Minerals sales where {returned_minerals}\n")
   
    returned_sweets = float(input("Please enter sweet sales, eg 12.34: "))
    print(f"Sweets sales where {returned_sweets}\n")

    returned_choc = float(input("Please enter chocolate sales, eg 12.34: "))
    print(f"chocolate sales where {returned_choc}\n")

    total_sales = (returned_hot_food + returned_cakes + returned_bread
                   + returned_coffee + returned_0_vat + returned_wine 
                   + returned_chilled + returned_minerals + returned_sweets 
                   + returned_choc)
    print(f'Thank you, todays total sales {total_sales}\n')


def validate_sales(values):
    """
    Converts string to float 
    """
    try:
        float(values)
        print(f"The value you entered was {values}")
        raise ValueError(
                print(f"Thank you, {values} \n ")
            )

    except ValueError as e:
        print(f'Invalid data {e}, please try again')    


sales_data()
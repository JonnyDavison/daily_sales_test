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

    returned_date = input("Please enter todays Date here dd/mm/yyyy: ")
    print(f"Date provided: {returned_date} \n")
   
    returned_hot_food = input("Please enter todays Hot Food sales eg 12.50: ")
    sales_hot_food = returned_hot_food.split(",")
    validate_sales(sales_hot_food)
    
    returned_cakes = input("Please enter todays Cake sales eg 12.50: ")
    sales_cakes = returned_cakes.split(",")
    validate_sales(sales_cakes)

    returned_bread = input("Please enter todays Bread sales eg 12.50: ")
    sales_bread = returned_bread.split(",")
    validate_sales(sales_bread)

    returned_coffee = input("Please enter todays Coffee sales eg 12.50: ")
    sales_coffee = returned_coffee.split(",")
    validate_sales(sales_coffee)

    returned_0_vat = input("Please enter todays 0% VAT sales eg 12.50: ")
    sales_0_vat = returned_0_vat.split(",")
    validate_sales(sales_0_vat)

    returned_wine = input("Please enter todays Wine sales eg 12.50: ")
    sales_wine = returned_wine.split(",")
    validate_sales(sales_wine)

    returned_chilled = input("Please enter todays Chilled sales eg 12.50: ")
    sales_chilled = returned_chilled.split(",")
    validate_sales(sales_chilled)
 
    returned_minerals = input("Please enter todays Minerals sales eg 12.50: ")
    sales_minerals = returned_minerals.split(",")
    validate_sales(sales_minerals)

    returned_sweets = input("Please enter todays Sweets sales eg 12.50: ")
    sales_sweets = returned_sweets.split(",")
    validate_sales(sales_sweets)    

    returned_choc = input("Please enter todays Chocolate sales eg 12.50: ")
    sales_choc = returned_choc.split(",")
    validate_sales(sales_choc)


def validate_sales(values):
    """
    Converts user input into floats.
    Raises ValueError when input cant be converted into a float,
    or if there is no user value.
    """
    try:
        [float(value) for value in values]
        if len(values) != 1:
            raise ValueError(
                f"1 numeric value required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, you must input a numeric value.\n")


sales_data()
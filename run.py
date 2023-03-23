"""Google sheet import"""
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


def welcome():
    """
    Greets the user and informs of how they should use the program
    """
    print("welcome to Daily Sales, your financial record system")
    print('Please enter todays sales by department')
    print('Figures should be in the format requested')
    print('Example dd/mm/yyyy or 1234.56 \n')


def date_recorded():
    """
    Takes the date as an inout from the user
    """
    returned_date = input("Please enter todays Date here dd/mm/yyyy: ")
    print(f"Date provided: {returned_date} \n")
    return returned_date


def sales_data_hot():
    """
    Get end of day sales total for Hot Food sales
    """

    while True:
        returned_hot_food = input("Please enter Hot Food sales eg 12.50: ")
        sales_hot_food = returned_hot_food.split(",")
        validate_sales(sales_hot_food)

        if validate_sales(sales_hot_food):
            print('Hot Food sales are valid')
            break

    return sales_hot_food


def sales_data_cake():
    """
    Get End of day sales data for Cake
    """
    while True:
        returned_cakes = input("Please enter Cake sales eg 12.50: ")
        sales_cakes = returned_cakes.split(",")
        validate_sales(sales_cakes)

        if validate_sales(sales_cakes):
            print('Cakes sales are valid')
            break

    return sales_cakes


def sales_data_bread():
    """
    Gets end of day sales data for Bread
    """
    while True:
        returned_bread = input("Please enter Bread sales eg 12.50: ")
        sales_bread = returned_bread.split(",")
        validate_sales(sales_bread)

        if validate_sales(sales_bread):
            print('Bread sales are valid')
            break

    return sales_bread


def sales_data_coffee():
    """
    Gets end of day sales data for Coffee
    """
    while True:
        returned_coffee = input("Please enter Coffee sales eg 12.50: ")
        sales_coffee = returned_coffee.split(",")
        validate_sales(sales_coffee)

        if validate_sales(sales_coffee):
            print('Coffee sales are valid')
            break

    return sales_coffee


def sales_data_0_vat():
    """
    Gets end of day sales data for 0% VAT items
    """
    while True:
        returned_0_vat = input("Please enter 0% VAT sales eg 12.50: ")
        sales_0_vat = returned_0_vat.split(",")
        validate_sales(sales_0_vat)

        if validate_sales(sales_0_vat):
            print('0% VAT sales are valid')
            break

    return sales_0_vat


def sales_data_wine():
    """
    Gets end of day sales data for Wine
    """
    while True:
        returned_wine = input("Please enter Wine sales eg 12.50: ")
        sales_wine = returned_wine.split(",")
        validate_sales(sales_wine)

        if validate_sales(sales_wine):
            print('Wine sales are valid')
            break

    return sales_wine


def sales_data_chilled():
    """
    Gets end of day sales data for Chilled Produce
    """
    while True:
        returned_chilled = input("Please enter Chilled sales eg 12.50: ")
        sales_chilled = returned_chilled.split(",")
        validate_sales(sales_chilled)

        if validate_sales(sales_chilled):
            print('Chilled sales are valid')
            break

    return sales_chilled


def sales_data_minerals():
    """
    Gets end of day sales data for Minerals
    """
    while True:
        returned_minerals = input("Please enter Minerals sales eg 12.50: ")
        sales_minerals = returned_minerals.split(",")
        validate_sales(sales_minerals)

        if validate_sales(sales_minerals):
            print('Mineral sales are valid')
            break

    return sales_minerals


def sales_data_sweets():
    """
    Gets end of day sales data for Sweets
    """
    while True:
        returned_sweets = input("Please enter Sweets sales eg 12.50: ")
        sales_sweets = returned_sweets.split(",")
        validate_sales(sales_sweets)

        if validate_sales(sales_sweets):
            print('Sweet sales are valid')
            break

    return sales_sweets


def sales_data_choc():
    """
    Gets end of day sales data for Chocolate
    """
    while True:
        returned_choc = input("Please enter Chocolate sales eg 12.50: ")
        sales_choc = returned_choc.split(",")
        validate_sales(sales_choc)

        if validate_sales(sales_choc):
            print('Chocolate sales are valid')
            break

    return sales_choc
    # move the return statemetns togethet in a stack


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
    except ValueError as error:
        print(f"Invalid data: {error}, you must input a numeric value.\n")
        return False

    return True


def update_sales_sheet(data):
    """
    Updates the Google sheet
    """
    print('Trying to update spread sheet')
    sales_sheet = SHEET.worksheet('sales')
    sales_sheet.append_row(data)
    print("oh golly it worked")


welcome()
# """
# Updating date input
# """
# date = date_recorded()
# date_data = int(date)
# update_sales_sheet(date_data)


# Updateing hot food sales data10
data_hot = sales_data_hot()
hot_food_sales_data = [float(num) for num in data_hot]
update_sales_sheet(hot_food_sales_data)

# Updateing hot food sales data
data_cake = sales_data_cake()
cake_sales_data = [float(num) for num in data_hot]
update_sales_sheet(cake_sales_data)


sales_data_bread()
sales_data_coffee()
sales_data_0_vat()
sales_data_wine()
sales_data_chilled()
sales_data_minerals()
sales_data_sweets()
sales_data_choc()

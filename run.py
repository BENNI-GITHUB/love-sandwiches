import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPEAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPEAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figure input from the users.
    """
    print("Please enter the sales data from the last market")
    print("Data should be sixnumbers saparated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter the data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(value):
    """
    Check the value amount is 6 and the value are int
    """
    try:
        if len(value) != 6:
            raise ValueError(
        f"Exactly 6 values are required, you provided {len(value)}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again \n")

        
get_sales_data()


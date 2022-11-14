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
SHEET = GSPREAD_CLIENT.open('the_fruit_shop')

FRUIT_LIST = {
    Banana Box 10kg
    Apple Box 10kg
    Pear Box 10kg
    Pineapple 12 units
    Papaya Box 10kg
    Avocado Box 10kg
    Orange Box 10kg
    Lemon box 5kg
}

def get_order():
    """ 
    Get order input from the costumer
    """

    print("Please, enter your product order")
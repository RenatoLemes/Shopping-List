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
    Banana Box 10kg - € 14.99
    Apple Box 10kg - € 14.99
    Pear Box 10kg - € 14.99
    Pineapple 12 units - € 11.99
    Papaya Box 10 units - € 16.99
    Avocado Box 10kg - € 21.99
    Orange Box 10kg - € 14.99
    Lemon box 5kg - € 8.99
}

def get_order():
    """ 
    Get order input from the costumer
    """

    print("Please, enter your order")

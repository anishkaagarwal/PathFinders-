import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- Google Sheets Setup ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)


# Replace with your spreadsheet ID
SPREADSHEET_ID = "1CQSDaaG9IFiAd0vChBWTL3rtPJGEr1v2YerQm79Xdh4"

# Open the sheet
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# --- Test: Add a row ---
row = [str(datetime.now()), "Test User", "AI, Data Science", "Problem Solving", "Data Scientist"]
sheet.append_row(row)

print("✅ Test row added successfully!")

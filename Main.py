import pywhatkit
import pandas as pd
import time
import pyautogui

df = pd.read_csv("IEEEnumbers - Sheet1 - IEEEnumbers - Sheet1.csv (1).csv", encoding='utf-8')
df.columns = df.columns.str.strip()
if 'Phone number' in df.columns:
    df.drop_duplicates(subset=['Phone number'], keep='first', inplace=True)
    df['Phone number'] = df['Phone number'].astype(str)
    def format_number(phone):
        phone = phone.strip()
        if phone.startswith("20"):  
            return f"+{phone}"  
        elif phone.isdigit() and int(phone) > 0:  
            return f"+20{phone}"  
        else:
            return "+20" + phone  

    df['Phone number'] = df['Phone number'].apply(format_number)

    print("✅ Phone numbers cleaned. Starting WhatsApp auto-messaging...")

    # Message to send
    message = """ 
    """

    for phone_number in df['Phone number']:
        try:
            print(f"📩 Sending message to {phone_number}...")
            pywhatkit.sendwhatmsg_instantly(phone_number, message, tab_close=True, wait_time=15)
            time.sleep(2)  
            pyautogui.press("enter")  
            time.sleep(4)  
        except Exception as e:
            print(f"❌ Failed to send to {phone_number}: {e}")

    print("All messages sent automatically!")

else:
    print("❌ Error: Column 'Phone number' not found!")

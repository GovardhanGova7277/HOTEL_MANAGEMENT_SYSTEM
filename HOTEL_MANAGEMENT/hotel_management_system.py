##3. Hotel seat and food reservation: where admin will add hotels and their seats food and
# user will be able to reserve seat and food before they arrive.
##
print('---------------------------------------------------------------')
##The process to book a table at BBQ Nation or any similar restaurant typically involves the following steps:
##
##1. Choose a Booking Method:
##   - BBQ Nation and many other restaurants offer multiple booking methods. You can choose the one that is most convenient for you:
##     - Online Booking: Many restaurants, including BBQ Nation, have their official websites or mobile apps where you can make a reservation. You can also use third-party restaurant reservation platforms like OpenTable or Resy.
##     - Walk-In: If you prefer not to book in advance, you can simply walk into the restaurant and request a table. However, this option may not guarantee immediate seating, especially during peak hours.
##
##2. Check Availability:
##   - When booking online or via phone, you'll need to provide details such as the date, time, number of guests, and any special requests (e.g., special occasions, dietary restrictions). The restaurant staff will check their availability for the specified date and time.
##
##3. Confirm the Reservation:
##   - After checking availability, the restaurant staff will confirm your reservation and provide you with a booking reference number or confirmation details. Make sure to note down this information.
##
##4. Arrive on Time:
##   - On the day of your reservation, make sure to arrive at the restaurant on time. Punctuality is important, especially during busy hours.
##
##5. Enjoy Your Dining Experience:
##   - Once you're seated, enjoy your dining experience at BBQ Nation or the chosen restaurant. If you have any special requests or preferences, don't hesitate to communicate them with the restaurant staff.
##
##6. Payment:
##   - After your meal, you'll receive the bill. Pay the bill as per the restaurant's payment methods (cash, credit card, etc.).
##
##7. Provide Feedback:
##   - After your dining experience, you may have the opportunity to provide feedback on the service, food quality, and overall experience. Many restaurants value customer feedback to improve their services.
##
##Please note that the exact booking process may vary depending on the specific BBQ Nation location or restaurant chain, so it's a good idea to check the restaurant's official website or contact them directly for the most accurate and up-to-date information on booking a table. Additionally, making a reservation well
##in advance, especially for popular restaurants, is recommended to secure your desired dining time.


import pymysql
from prettytable import PrettyTable
import pywhatkit
db=pymysql.connect(host='localhost',user='root',password='7277',database='hotel')

cur=db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS TABLES (T_NUMBER INT AUTO_INCREMENT PRIMARY KEY,NUMBER_OF_SEATS INT,CUSTOMER_NAME VARCHAR(20))")

cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS(NAME VARCHAR(20),BOOKING_DATE VARCHAR(20),BOOKING_TIME VARCHAR(20),GUESTS INT,SP_REQ VARCHAR(20))")


def whatsapp():
    print('!! WELCOME TO BBQ NATION !!')
    name=input("What's your name: ")
    date=input('Table Booking Date: ')
    time=input('Table Booking Time: ')
    guest=int(input('Number of Guests: '))
    sp_req=input('Any Special Requests: ')
    
    pywhatkit.sendwhatmsg_instantly(f'+91{9441057677}',f'Name: {name}\nTable Booking Date: {date}\nTable Booking Time: {time}\nNumber of Guests: {guest}\nSpecial Request: {sp_req}')

    cur.execute(f"insert into customer values('{name}','{date}','{time}',{guest},'{sp_req}')")
    db.commit()
    

def view():
    password=input('PASSWORD: ')
    if password=='admin':
        cur.execute('select * from customer')
        results=cur.fetchall()
        table=PrettyTable()

        table.field_names=['NAME','DATE','TIME','GUEST','SPECIAL_REQUEST']

        for result in results:
            table.add_row(result)
        print(table)
            
    db.commit()
    
        
def add_table():
    password=input('PASSWORD: ')
    if password=='admin':
        table_number=int(input('Insert Table numbers: '))
        no_of_seats=int(input('Number of Seats for the table: '))
        cur.execute(f"insert into tables(T_NUMBER,NUMBER_OF_SEATS) values({table_number},{no_of_seats})")

    db.commit()

        
def book_table():
    name=input("What's your name: ")
    password=input('PASSWORD: ')
    if password=='admin':
        booking_details()
        table_number=int(input('Enter the table number: '))
        cur.execute(f"update tables set CUSTOMER_NAME='{name}' where  T_NUMBER={table_number}")
    db.commit()

        
def booking_details():
    password=input('PASSWORD: ')
    if password=='admin':
        cur.execute(f"select * from tables")

        results=cur.fetchall()
        
        table=PrettyTable()

        table.field_names=['T_NUMBER','NUMBER_OF_SEATS','CUSTOMER_NAME']

        for result in results:
            table.add_row(result)
            
        print(table)
        
    db.commit()

    
def view_table():
    name=input('Enter Your Name: ')
    cur.execute(f"select * from tables where CUSTOMER_NAME='{name}'")
    results=cur.fetchall()
    table=PrettyTable()
    table.field_names=['T_NUMBER','NUMBER_OF_SEATS','CUSTOMER_NAME']
    for result in results:
        table.add_row(result)
    print(table)
    
def feedback():
    print('!! THANKS FOR VISITING !!')
    feedback=input('FEEDBACK(STARS *****): ')
    pywhatkit.sendwhatmsg_instantly(f"+91'{9441057677}'",f"{feedback}")


choice=input('''1. Book Via Whatsapp\n
2. Give the feedback\n
Enter your choice: ''')

if choice=='1':
    whatsapp()
elif choice=='user':
    view_table()
    feedback()
elif choice=='admin':
    while True:
        option=input("1. TO VIEW DETAILS\n2. TO ADD TABLES\n3. TO BOOK THE TABLE\n4. TO VIEW THE BOOKING DETAILS\nENTER YOUR CHOICE: ") 
        if option=='1':
            view()
        elif option=='2':
            add_table()
        elif option=='3':
            book_table()
        elif option=='4':
            booking_details()
        else:
            print('INVALID CHOICE')
            break
        




def report_issue():
    print("\nWhat issue are you experiencing?")
    print("1. My order hasn't arrived")
    print("2. I received the wrong order")
    print("3. The order was damaged")
    print("4. Other")
    print("5. Exit")

    choice = input("Please enter the number of your choice: ")

    if choice == '1':
        order_id = input("Please enter your order ID: ")
        print(f"We're sorry that your order with ID {order_id} hasn't arrived.")
        print("Our team will investigate the issue and get back to you shortly.")
    elif choice == '2':
        order_id = input("Please enter your order ID: ")
        print(f"We're sorry that you received the wrong order with ID {order_id}.")
        print("Please hold on while we arrange for the correct order to be sent to you.")
    elif choice == '3':
        order_id = input("Please enter your order ID: ")
        print(f"We're sorry that your order with ID {order_id} was damaged.")
        print("We'll send a replacement or offer you a refund.")
    elif choice == '4':
        print("Please describe the issue you're facing: ")
        issue_description = input()
        print("Thank you for the information. We'll look into the issue and get back to you.")
    elif choice == '5':
        print("Thank you for using our service! Have a great day!")
    else:
        print("Error: please input a valid number (1-5)")

def order_status():
    order_id = input("Please enter your order ID: ")
    print(f"Checking the status of your order with ID {order_id}...")
    # Placeholder for order status check logic
    print("Your order is currently being prepared and will be delivered in approximately 30 minutes.")
    print("You can also check the status of your order in the app.")

def order_history():
    customer_id = input("Please enter your customer ID: ")
    print(f"Retrieving order history for customer ID {customer_id}...")
    # Placeholder for order history retrieval logic
    print("Here are your recent orders:")
    print("1. Order ID: 12345 - Delivered")
    print("2. Order ID: 67890 - In Progress")
    print("3. Order ID: 54321 - Canceled")

def compensation():
    print("We apologize for the inconvenience. You may be eligible for compensation.")
    print("1. Refund")
    print("2. Discount on next order")
    print("3. Free delivery on next order")
    print("4. Exit")

    choice = input("Please enter the number of your choice: ")

    if choice == '1':
        print("A refund will be processed within the next 5-7 business days.")
    elif choice == '2':
        print("A discount code will be sent to your email.")
    elif choice == '3':
        print("Free delivery will be applied to your next order.")
    elif choice == '4':
        print("Thank you for using our service! Have a great day!")
    else:
        print("Error: please input a valid number (1-4)")

def customer_service():
    print("Connecting you to a customer service representative. Please wait...")
    # Placeholder for customer service connection logic

def chatbot():
    name = input("Hello! Welcome to Food Delivery Support. What's your name? ")
    print(f"Nice to meet you, {name}! How can we assist you today?")

    while True:
        print("\nHow can we help you today?")
        print("1. Report an issue")
        print("2. Check order status")
        print("3. View order history")
        print("4. Compensation options")
        print("5. Speak to a customer service representative")
        print("6. Exit")
        
        response = input("Please enter the number of your choice: ")

        if response == '1':
            report_issue()
        elif response == '2':
            order_status()
        elif response == '3':
            order_history()
        elif response == '4':
            compensation()
        elif response == '5':
            customer_service()
        elif response == '6':
            print(f"Alright, {name}. If you need any help in the future, feel free to reach out. Have a great day!")
            break
        else:
            print("Error: please input a valid number (1-6)")

chatbot()

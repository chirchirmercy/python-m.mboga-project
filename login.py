class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def check_details(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False
login = Login('username', 'password')
valid = login.check_details('username', 'password')
if valid:
    print('Login successful')
else:
    print('Invalid username or password')

class Signup:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    
    def create_account(self):
        print(f"Account with email '{self.email}', username '{self.username}', and password '{self.password}' has been created.")
signup = Signup('chep@gmail.com', 'mercy', '454532')
signup.create_account()


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def display_product_details(self):
        return f"Buy {self.name} today with only {self.price} Ksh with {self.description}."
     


product = Product("widget",50.0,"high quality")
print(product.display_product_details())


class Review:
    def __init__(self, customer, seller, rating, comment):
        self.customer = customer
        self.seller = seller
        self.rating = rating
        self.comment = comment

    def display_review_details(self):
        return f"{self.customer} have bought products from {self.seller} at {self.rating} % and have prove faith is a {self.comment}"
        
review= Review("mercy", "faith", 4.5, "Great seller!")
print(review.display_review_details())



class Stock:
    def __init__(self, seller, buyer, quantity, price):
        self.seller = seller
        self.buyer = buyer
        self.quantity = quantity
        self.price = price

    def display_stock_details(self):
        return f"{self.seller} bought tomatoes,sukumawiki and potatoes from {self.buyer} which hold {self.quantity} kg at ksh {self.price}"
        

stock = Stock("marion", "caren",40,50.0)
print(stock.display_stock_details())



class Payment:
    def __init__(self, amount, id_number, payment_date,new_account_balance):
        self.id_number = id_number
        self.amount = amount
        self.payment_date = payment_date
        self.new_account_balance=new_account_balance 
    def display_payment_details(self):
        return f" confirm you have receive Ksh {self.amount}  from ID Number {self.id_number}  on {self.payment_date} and your account balance is Ksh {self.new_account_balance}"
        

payment = Payment(200.0, 456767,30-2-2023,500.00)
print(payment.display_payment_details())



class Registration:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def login(self):
        if self.username == self.email and self.password == password and self.username == self.email==email:
            print("Login successful!")
        else:
            print("Invalid username or password or email.")

    def signup(self):
        print(f"Account with email '{self.email}', username '{self.username}', and password '{self.password}' has been successfully created.")


# Test the Registration class
registration = Registration('Mary', 'password456', 'mary@example.com')

registration.signup()  # User sign up

registration.login()  # User login


class Discount:
    def __init__(self, customer_name, total_purchase, discount_percentage):
        self.customer_name = customer_name
        self.total_purchase = total_purchase
        self.discount_percentage = discount_percentage

    def calculate_discount(self):
        if self.total_purchase >= 100:
            self.discount_percentage = 0.1
        return f"Confirm  {self.customer_name} has made a purchase of {self.total_purchase} and received {self.discount_percentage} discount."


discount = Discount("Faith", 100, 0.4)
print(discount.calculate_discount())
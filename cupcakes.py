from abc import ABC, abstractmethod
from hashlib import new
from pprint import pprint
import csv
from turtle import write_docstringdict

class Cupcake(ABC):
    def __init__(self, flavor, price, sprinkled):
        self.flavor = flavor
        self.price = price
        self.sprinkled = sprinkled
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    # @abstractmethod >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ????????????? <<<<<<<<<<<<<<<<<<<<<<<<
    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = 'mini'
    def __init__(self, flavor, price, sprinkled, wait_time):
        self.flavor = flavor
        self.price = price
        self.sprinkled = sprinkled
        self.sprinkles = []
        self.wait_time = wait_time


class dounut(Cupcake):
    def __init__(self, flavor, price, sprinkled, wait_time):
        self.flavor = flavor
        self.price = price
        self.sprinkled = sprinkled
        self.sprinkles = []
        self.wait_time = wait_time


def reader(file_name):
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
        # for row in reader:
        #     # print(row)
        #     return(row)

# reader('sample.csv')


cupcake1 = Cupcake("vanilla", 2.99, True)
cupcake2 = Mini("Chocolate", 1.99, True, 30)
cupcake3 = dounut('Strawberry', 3.99,  False, 20)
cupcake1.add_sprinkles("M&Ms")
cupcake2.add_sprinkles("Mint")

cupcake_list = [cupcake1, cupcake2, cupcake3]

def new_csv_file(name_of_file, cupcakes):
    with open(name_of_file, "a") as csvfile:
        field_names = ["flavor", "price", "sprinkled", "sprinkles", "wait_time"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        # writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, 'wait_time'):
                writer.writerow({'flavor': cupcake.flavor, "price":cupcake.price, "sprinkled": cupcake.sprinkled, "sprinkles": cupcake.sprinkles, "wait_time": cupcake.wait_time})
            else:
                writer.writerow({'flavor': cupcake.flavor, "price":cupcake.price, "sprinkled": cupcake.sprinkled, "sprinkles": cupcake.sprinkles})

# new_csv_file("sample.csv", cupcake_list)

def add_new_cupcake(name_of_file, cupcake):
    with open(name_of_file, "a", newline='\n') as csvfile:
        field_names = ["flavor", "price", "sprinkled", "sprinkles", "wait_time"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        
        if hasattr(cupcake, 'wait_time'):
            writer.writerow({'flavor': cupcake.flavor, "price":cupcake.price, "sprinkled": cupcake.sprinkled, "sprinkles": cupcake.sprinkles, "wait_time": cupcake.wait_time})
        else:
            writer.writerow({'flavor': cupcake.flavor, "price":cupcake.price, "sprinkled": cupcake.sprinkled, "sprinkles": cupcake.sprinkles})

# ============================== 5.4 =======================================

def find_cupcake(cupcake_flavor):
    with open('cupcake_list.csv') as csvfile:
        cup = csv.DictReader(csvfile)
        cup = list(cup)
        for cupcake in cup:
            if cupcake['flavor'] == cupcake_flavor:
                return cupcake

def add_to_order(obj):
    with open("order.csv", "a", newline='\n') as csvfile:
        field_names = ["flavor", "price", "sprinkled", "sprinkles", "wait_time"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writerow(obj)

find_cupcake('Vanilla')

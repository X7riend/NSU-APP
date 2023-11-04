import sqlite3

#connect to sqlite database
#connection = sqlite3.connect('databasename.db')

#create cursor to interact with database
#cursor = connection.cursor()


class InFlightCateringService:
    def __init__(self):
        self.menu = self.loadMenuItems()
        self.passengers = []
        self.orders = {}

    def loadMenuItems(self):
        # Skeleton code to mimic loading menu items from a database
        # Simulate a list of menu items fetched from a database query
        menu_items = [
            {"id": 1, "name": "Peanuts", "price": 5.0},
            {"id": 2, "name": "Chips", "price": 4.0},
            {"id": 3, "name": "Cookies", "price": 3.0},
        ]

        #actual from database
        #self.cursor.execute('SELECT * FROM menu_items')
        #menu_items = self.cursor.fetchall()

        return menu_items

    def setMealPreferences(self, passengerId, mealPreferences):
        passenger = self.findPassengerById(passengerId)
        passenger['preferences'] = mealPreferences
        self.savePreferences(passenger)

    def findPassengerById(self, passengerId):
        # Skeleton code to mimic finding a passenger by ID in a database
        # Simulate searching for a passenger in the database
        passenger_from_db = next((p for p in self.passengers if p['id'] == passengerId), None)
        return passenger_from_db

    def savePreferences(self, passenger):
        # Skeleton code to mimic saving passenger preferences to a database
        # Simulate updating a passenger's preferences in the database
        for i, p in enumerate(self.passengers):
            if p['id'] == passenger['id']:
                self.passengers[i] = passenger

    def processOrders(self):
        for passenger in self.passengers:
            if 'preferences' in passenger:
                self.createOrder(passenger, passenger['preferences'])

    def createOrder(self, passenger, preferences):
        order = {"passenger_id": passenger['id'], "items": []}
        for preference in preferences:
            menu_item = next((item for item in self.menu if item['id'] == preference), None)
            if menu_item:
                order["items"].append(menu_item)
        self.orders[passenger['id']] = order

    def getAllPassengers(self):
        return self.passengers

# Sample Driver
if __name__ == '__main__':
    service = InFlightCateringService()
    # Sample passengers
    service.passengers = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"},
    ]
    # Sample passenger preferences
    service.setMealPreferences(1, [1, 2])
    service.setMealPreferences(2, [2, 3])
    # Process orders
    service.processOrders()

    # Display orders
    for passenger_id, order in service.orders.items():
        print(f"Passenger ID {passenger_id}'s order: {order['items']}")

#make sure to close database connection
#connection.close()
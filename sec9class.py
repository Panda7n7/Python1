
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant:{self.restaurant_name}')
        print(f'Cuisine type:{self.cuisine_type}')

    def open_restaurant(self):
        print("The restaurant is open")


restaurant = Restaurant('鹿其林', '中式')
restaurant.describe_restaurant()
restaurant.open_restaurant()


"""
Class Car:
    def __init__(self,seats):
    self.seat = seats                 #initialise attributes

    #methods inside class
    def enter_car_mode():
    self.seats = 2
"""
class User:
    #attributes
    def __init__(self, user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #methods
    def follow(self, user):
        user.followers+=1
        self.following+=1
user_1 = User("001","umar")
user_2 = User("002","adeel")
print(user_1.followers)

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
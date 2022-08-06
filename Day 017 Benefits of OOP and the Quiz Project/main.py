class User:
    def __init__(self, user_id, username):  # initialise attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, other_user):
        self.following += 1
        other_user.followers += 1


user_1: User = User("001", "Paul")
user_2: User = User("002", "John")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

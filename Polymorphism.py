class User:
    def login(self):
        print("User logging in")

class Admin(User):
    def login(self):
        print("Admin logging in with extra checks")

class Guest(User):
    def login(self):
        print("Guest logging in with limited access")
        

users=[User(), Admin(), Guest()]

for u in users:
    u.login()
class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.__password = password
        
    def login(self, password: str) -> bool:
        if (password==self.__password):
            print(f"{self.username} logged in successfully.")
            return True
        
        else:
            print("Login failed! Incorrect password.")
            return False
        
    def __getPassword(self):
        return self.__password
    
user1 = User ("farrahpepino", "secret123")
user1.login("farrah")
user1.login("secret123")
print(user1.username)
# print(user1.__password)
# print(user1.getPassword())
print(user1._User__getPassword())
class User: 
    def __init__ (self, username) -> None:
        self.username = username
    
    def login(self) -> None:
        print(f"{self.username} logged in.")
    
    
class Admin(User):
    def __init__ (self, username:str, level: int)-> None:
        super().__init__(username)
        self.level = level
    
    def delete_user(self, user: str) -> None:
        print(f"{self.username} deleted {user}.")

user = User("farrah")
user.login()

admin = Admin("root", 5)
admin.login()
admin.delete_user("farrah")
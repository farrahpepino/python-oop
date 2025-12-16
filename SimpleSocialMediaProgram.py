# Classes: Admin, User, Guest, Post 
# Variables: username, password, post content
# Functions: Login, Delete user, post

posts = list(dict())
class Post(): 
    def create_post(self, username, content) -> None:
        post = {"username": username, "content": content }
        posts.append(post)
        print(f"Post created! {post}")
    
    def get_all_posts(self):
        print(f"Getting all posts... {posts}")
        
class User(Post):
    #this function initializes the attributes(variables) of the class User. This function does not return anything.
    def __init__ (self, username, password) -> None:
        self.username = username
        self.__password = password #The reason why you need the two underscores is because the variable should be private and should not be accessed directly
        
    def login(self, password):
        if (self.__password == password):
            print(f"{self.username} successfully logged in!")
    

# This class inherits attributes and behaviours from class User and also has its own function, which is deleting users.
class Admin(User):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        
    def delete_user(self, username):
        print(f"{self.username} deleted User {username}.")
        


john: User = User('johnsmith', 'secret123') 
mark: Admin = Admin('markzuckerberg', "secret1234")

john.login('secret123')
john.create_post(john.username, "Hello! This is my first post!")
john.get_all_posts()
mark.login('secret1234')
mark.delete_user('johnsmith')




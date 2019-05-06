#1 creating a class
#2 create method called class
#3 is a dictonary

class InstagramAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.photos = []
    
    def follow(self, another_account):
        try:
            another_account.followers.append(self.username)
        except:
            ('Not a valid instagram account')

    def add_photo(self, photo):
        self.photos.append(photo)

    def get_followers(self):
        return self.followers

    def __repr__(self):
        return '<username: {}, password {}, followers {}, photos: {}'.format(self.username,self.password,self.followers,self.photos)

my_account = InstagramAccount('Ross Bautista', 'Secure')
second_account = InstagramAccount('Charlene Queano', '123456')
third_account = InstagramAccount('Francis Martinez', '888888')

my_account.follow(second_account)

third_account.follow(second_account)

my_account.add_photo({'photo_id': 1, 'url': 'https://picsofdogs.com', 'likes': 0})

print(second_account.get_followers())

print(my_account)
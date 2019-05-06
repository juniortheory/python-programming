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
        if isinstance(another_account, InstagramAccount):
            another_account.followers.append(self.username)
        else:
            print('Not a valid instagramaccount')
        '''
        try:
            another_account.followers.append(self.username)
        except:
            print('Not a valid instagram account')
        '''
    #access the keys in the dictionary to make sure all keys is matched with photo_id, url and likes    
    def add_photo(self, photo):
        if isinstance(photo, dict):
            all_keys = photo.keys()
            if 'photo_id' in all_keys and 'url' in all_keys and 'likes' in all_keys:
                self.photos.append(photo)

    def get_followers(self):
        return self.followers

    def __repr__(self):
        return '<username: {}, password {}, followers {}, photos: {}'.format(self.username,self.password,self.followers,self.photos)

account_1 = InstagramAccount('John', 'Secure')

account_2 = InstagramAccount('jane', 'password')

account_1.follow('Vinay')


'''
my_account = InstagramAccount('Ross Bautista', 'Secure')
second_account = InstagramAccount('Charlene Queano', '123456')
third_account = InstagramAccount('Francis Martinez', '888888')

my_account.follow(second_account)

third_account.follow(second_account)

my_account.add_photo({'photo_id': 1, 'url': 'https://picsofdogs.com', 'likes': 0})

print(second_account.get_followers())

print(my_account)
'''
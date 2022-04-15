import requests
import json

class GetImageFromInstagram:

    def __init__(self, username):
        self.username= username


    def get_image(self):
        response = requests.get('https://www.instagram.com/{}/?__a=1'.format(self.username))
        image_url= json.loads(response.text)["graphql"]["user"]["profile_pic_url_hd"]
        image= requests.get(image_url)
        return image.content


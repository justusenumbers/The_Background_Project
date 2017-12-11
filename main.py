import requests #requestsb library for HTTP requests
import json

payload = {
"key" : "API_KEY_GOES_HERE", #API Key goes here
"q" : "Wallpaper",
"image_type":"photo",
"category" : "backgrounds",
"min_width" : "960",
"min_height" : "720",
"editors_choice" : "True",
"per_page" : "10",
"safesearch" : "True"
}

url = "https://pixabay.com/api/"
response = requests.get(url,params = payload)

#ADD TRY STATEMENT FOR WHEN API NOT PRESENT


for pictureURL in json.loads(response.text.encode("utf-8"))["hits"]:
     with open ("/home/justusenumbers/Projects/The_Background_Project/res/"+str(pictureURL["id"])+".jpg", "wb") as outfile:
         outfile.write(requests.get(pictureURL["userImageURL"]).content)
         print (pictureURL["id"], "Successfully Douwnloaded!" )

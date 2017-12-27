import requests #requestsb library for HTTP requests
import json
import os
import time

payload = {
"key" : "API_KEY_GOES_HERE", #API_KEY_GOES_HERE
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
json_res = json.loads(response.text.encode("UTF-8"))

with open("/home/justusenumbers/Projects/The_Background_Project/res/response.txt", "w") as resfile:
    resfile.write(json.dumps(json_res, indent=4, sort_keys=True))
    print("Response Written")
#ADD TRY STATEMENT FOR WHEN API NOT PRESENT: SKIP DOWNLOAD

for pictureURL in json_res["hits"]:
     with open ("/home/justusenumbers/Projects/The_Background_Project/res/img/"+str(pictureURL["id"])+".jpg", "wb") as outfile:
         outfile.write(requests.get(pictureURL["webformatURL"]).content)
         print (pictureURL["id"], "Successfully Douwnloaded!" )
#NEED TO TEST IF FILE PRESENT AND SKIP IF SO

background_Pictures_List = os.listdir("/home/justusenumbers/Projects/The_Background_Project/res/img")
background_Index = 0

while (True):
    print("picture",background_Index)
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/justusenumbers/Projects/The_Background_Project/res/img/"+background_Pictures_List[background_Index])
    #gconftool-2 --type=string --set /desktop/gnome/background/picture_options stretched    # stretch the image
    print("Background Set")
    time.sleep(5)
    background_Index+=1
    if background_Index == len(background_Pictures_List):
        print("Back to 0")
        background_Index  = 0
#NEED TO ADD RECURRING LOOP

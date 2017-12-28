import requests #requests library for HTTP requests
import json
import os
import time

#PIXABAY API INFO
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
pixabay_json_res = json.loads(response.text.encode("UTF-8"))

#PIXABAY JSON RESPONSE (not necessary, but good to look at for troubleshooting purposes)
with open("/home/justusenumbers/Projects/The_Background_Project/res/response.json", "w") as resfile:
    resfile.write(json.dumps(pixabay_json_res, indent=4, sort_keys=True))
    print("Response Written")

background_Pictures_List = os.listdir("/home/justusenumbers/Projects/The_Background_Project/res/img")

for pictureURL in pixabay_json_res["hits"]:
    if str(pictureURL["id"])+".jpg" in background_Pictures_List:
        print(str(pictureURL["id"])+".jpg", "already exists")
    else:
        with open ("/home/justusenumbers/Projects/The_Background_Project/res/img/"+str(pictureURL["id"])+".jpg", "wb") as outfile:
            outfile.write(requests.get(pictureURL["webformatURL"]).content)
            print (pictureURL["id"], "Successfully Douwnloaded!" )

#SETTING THE BACKGROUND (GNOME)
background_Index = 0

while (True):
    print("picture",background_Index)
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/justusenumbers/Projects/The_Background_Project/res/img/"+background_Pictures_List[background_Index]) #set background image (GNOME)
    #os.system("gsettings set org.gnome.desktop.background picture-options 'scaled'") #scales picture to fit on the screen (good for high definition images)
    print("Background Set")
    time.sleep(5) #Time to wait before setting the next background in seconds.
    background_Index+=1
    if background_Index == len(background_Pictures_List): #If at the end of list of pictures, start over.
        print("Back to 0")
        background_Index  = 0

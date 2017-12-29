import requests #requests library for HTTP requests
import json
import os
import time

def pixabay_Download():
    #PIXABAY API INFO
    payload = {
    "key" : "API_KEY_GOES_HERE", #API_KEY_GOES_HERE
    "q" : "Wallpaper",
    "image_type":"photo",
    #"category" : "backgrounds",
    "editors_choice" : "True",
    "per_page" : "10",
    "safesearch" : "True"
    }

    #REQUEST
    url = "https://pixabay.com/api/"
    response = requests.get(url,params = payload)
    pixabay_json_res = json.loads(response.text.encode("UTF-8"))

    #SAVE PIXABAY JSON RESPONSE TO A FILE (not necessary, but good to look at for troubleshooting purposes)
    with open("./res/response.json", "w") as resfile:
        resfile.write(json.dumps(pixabay_json_res, indent=4, sort_keys=True))
        print("JSON Response for Pixabay Written")

    #CHECKS IF FILE EXISTS, IF IT DOES, SKIPS TO THE NEXT ONE
    for pictureURL in pixabay_json_res["hits"]:
        if os.path.isfile("./res/img/"+str(pictureURL["id"])+".jpg"):
            print(str(pictureURL["id"])+".jpg", "already exists")
        else:
            with open ("./res/img/"+str(pictureURL["id"])+".jpg", "wb") as outfile:
                outfile.write(requests.get(pictureURL["webformatURL"]).content)
                print (pictureURL["id"], "Successfully Douwnloaded!" )
    print("Finished getting pixabay images")

#FIND CURRENT DIRECTORY
working_dir = os.getcwd()
print("Working Directory",working_dir)

try:
    pixabay_Download()
except:
    print ("Can't reach Pixabay, check internet connection or API info")

#lIST THE FILES IN THE /res/img FOLDER
background_Pictures_List = os.listdir("./res/img") #Make sure you run this before calling API fuction.

#SETTING THE BACKGROUND (GNOME)
background_Index = 0
while (True):
    print("picture",background_Index)
    os.system("gsettings set org.gnome.desktop.background picture-uri file://"+working_dir+"/res/img/"+background_Pictures_List[background_Index]) #set background image (GNOME)
    print("Background Set")
    time.sleep(5) #Time to wait before setting the next background in seconds.
    background_Index+=1
    if background_Index == len(background_Pictures_List): #If at the end of list of pictures, start over.
        print("Back to 0")
        background_Index  = 0

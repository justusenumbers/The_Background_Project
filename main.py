#import

key = "k,jghkljbhlij" #API Key goes here
image_type = "photo"
category = "backgrounds"
min_width = 960
min_height = 720
editors_choice = True
safesearch = True

url = "https://pixabay.com/api/?key="+ key +"&image_type="+ image_type + "&category=" + category + "&min_width=" + str(min_width)+ "&min_height=" + str(min_height) + "&editors_choice="+ str(editors_choice) + "&safesearch=" + str(safesearch)#

print(url)

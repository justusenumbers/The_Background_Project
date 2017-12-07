import requests #requestsb library for HTTP requests

payload = {
"key" : "API_KEY_GOES_HERE", #API Key goes here
"image_type":"photo",
"category" : "backgrounds",
"min_width" : "960",
"min_height" : "720",
"editors_choice" : "True",
"safesearch" : "True"
}

url = "https://pixabay.com/api/"
response = requests.get(url,params = payload)

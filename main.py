
import requests

client_id = '5737f5f3-ca60-4f6b-9b4f-e786eb78625a'

koordinatURL = 'https://frost.met.no/locations/v0.jsonld'

name = input("Skriv inn sted:")

parameter = {
    'names' :  name
}

r = requests.get(koordinatURL, parameter, auth=(client_id, ''))

r_json = r.json()

if r.status_code == 200:
    print("Statuskode", r.status_code, "godkjent")
else:
    print("Statuskode", r.status_code, "ikke godkjent")

list_data = r_json.get("data")
dict_0 = list_data[0]
dict_geometry = dict_0.get("geometry")
list_coordinate = dict_geometry.get("coordinates")
longitude = list_coordinate[0]
latitude = list_coordinate[1]


#bruk \complete på api.met.no

completeURL = "https://api.met.no/weatherapi/nowcast/2.0/complete"

headers = {
    'User-Agent' : 'University of Agder : MAS417 Project: Group3',
    'From' : 'endrem@student.uia.no',
}

parameter2 = {
    "lat" : latitude,
    "lon" : longitude
}

r2 = requests.get(completeURL, parameter2, headers=headers)

if r2.status_code == 200:
    print("Statuskode", r2.status_code , "Godkjent")
else:
    print("Statuskode", r2.status_code , "Ikke godkjent")

r2_json = r2.json()


print(r2_json)
dict_properties = r2_json.get("properties")
list_timeseries = dict_properties.get("timeseries")
dict_meta = list_timeseries[0]
dict_data = dict_meta["data"]
dict_instant = dict_data["instant"]
dict_details = dict_instant["details"]
list_details = list(dict_details) #liste av keys
mengde = dict_instant.values()
list_mengde = list(mengde)
dict_mengde = list_mengde[0]
values = dict_mengde.values()
list_values = list(values)
dict_next = dict_data["next_1_hours"]
dict_summary = dict_next["summary"]
string_symbol = dict_summary["symbol_code"]


if len(list_values) >= 6:
    print("Lufttemperatur:", list_values[0], "C")
    print("Nedbørshastighet:" , list_values[1] , "m/s")
    print("Relativ fuktighet:" , list_values[2] , "%")
    print("Vindretning:" , list_values[3], "grader")
    print("Vindhastighet" , list_values[4] , "m/s")
    print("Vindkast:", list_values[5] , "m/s")
    print("Værsymbol:", string_symbol)

elif len(list_values) < 6:
    print("Lufttemperatur:", list_values[0], "C")
    print("Nedbørshastighet:", list_values[1], "m/s")
    print("Relativ fuktighet:", list_values[2], "%")
    print("Vindretning:", list_values[3], "grader")
    print("Vindhastighet", list_values[4], "m/s")
    print("Værsymbol:", string_symbol)



image_symbol = (string_symbol + ".png")
print(image_symbol)


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread(image_symbol)
imgplot = plt.imshow(img)
plt.show()

#test
# import opencv
import cv2
import numpy as np


# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image_symbol, cv2.COLOR_BGR2GRAY)

# apply guassian blur on src image
gauss_image = cv2.GaussianBlur(gray_image, (5, 5), cv2.BORDER_DEFAULT)

# display input and output image
cv2.imshow("Gaussian Smoothing", gauss_image)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

option = input("Save weather icon as stl file? (y/n): ")
if option != "y":
    quit()

#image2 = cv2.imread('sol_gauss.png')
image_array = np.array(gauss_image)
print(image_array[0][0]) #prints first entry
print(image_array.shape) #prints size of array
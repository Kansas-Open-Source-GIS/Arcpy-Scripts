## Created By: Jerred Schmidt (jschmidt@winfieldks.org)
## Date: December 29, 2015
## Description: Downloads and creates a json file from ArcGIS server. Then converts it into a feature class
## may need modified if you are dealing with an unsecured service
##

import urllib, json, arcpy

userName = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
ipAddress = "YOUR_IP_ADDRESS"
arcpy.env.workspace = "YOUR_WORKSPACE"
GIS_SERVER_generateToken_URL = "YOUR_GIS_SERVER_generateToken_URL"
LAYER_QUERY_URL = "YOUR_LAYER_QUERY_URL"
output_name = "YOUR_OUTPUT_NAME"

#Get the access token from the GIS server
tokenURL = GIS_SERVER_generateToken_URL + "tokens/generateToken?username=" + userName + "&password=" + urllib.urlencode(password) + "&f=json&ip=" + ipAddress
token_response = urllib.urlopen(tokenURL)
token_data = json.loads(token_response.read())
token = token_data['token']

url = LAYER_QUERY_URL + "&token=" + token
response = urllib.urlopen(url)
data = json.loads(response.read())
with open('downloaded_json.json', 'w') as outfile:
    json.dump(data, outfile)
    
#Create the output geodatabase
arcpy.CreateFileGDB_management(arcpy.env.workspace, "temp.gdb")

#Create the output feature class or table
arcpy.JSONToFeatures_conversion("downloaded_json.json", os.path.join("temp.gdb", output_name))

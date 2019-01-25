import urllib, json, ast
url = 'http://api.openweathermap.org/data/2.5/weather?q=Madrid&APPID=mykey'
response = urllib.urlopen(url)
data = json.loads(response.read())
a=ast.literal_eval(json.dumps(data)) 
print(a)

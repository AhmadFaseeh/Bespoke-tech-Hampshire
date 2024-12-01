
#Hi there is a project realated to this topic, you can check it out here: https://github.com/
# firstly i used this library to get the data from the url. then i used the `json()` method to parse
import requests                
      #Id of the api key
apiKey='edb0cd56a9c9d49ab891022e4bf93978'
 # this is the input from the user
userInput=input("Enter city name:")   
   # this is the url from which i get the data
weather_data= requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=imperial&APPID={apiKey}") 
 # if the city is not found then it will print this message
if weather_data.json()['cod']=='404': 
    print("City not found")    
else:
    # this is the data which i got from the api
    weather=weather_data.json()['weather'][0]['main']  
    
    temp=round(weather_data.json()['main']['temp'])

    humidity=round(weather_data.json()['main']['humidity'])
   
    windSpeed=round(weather_data.json()['wind']['speed'])  

       
    print(f"The weather in {userInput} is :{weather}. The temperature is {temp}°F .The humidity is {humidity}% and the wind speed is {windSpeed}mph") 
    
   #Either we can simply call the function or we can call it with the arguments
   
   #We can use the weather _data.json() to get the data from the json file



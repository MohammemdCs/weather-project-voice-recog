import speech_recognition as sr
import turtle
import requests
recognizer = sr.Recognizer()
print("tell a city name")
try:
    with sr.Microphone() as mic:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        user_input = recognizer.recognize_google(audio)



except sr.UnknownValueError:
    print("Could not understand. Try again.")
    recognizer = sr.Recognizer()
    exit()

api_key = '057b4ca4ac53a04a5a0d2a1b5f527a91'

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")


if weather_data.status_code == 200:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temp= round((temp-32)*5/9)
    screen = turtle.Screen()
    screen.title("Weather Flashcard")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 0)
    pen.write(f"City: {user_input}\nWeather: {weather}\nTemp: {temp}ºC", align="center", font=("Arial", 18, "bold"))
    screen.mainloop()
else:
    screen = turtle.Screen()
    screen.title("Weather Flashcard")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 0)
    pen.write(f"City: {user_input}\nnah man it ain't a city", align="center", font=("Arial", 18, "bold"))
    screen.mainloop()



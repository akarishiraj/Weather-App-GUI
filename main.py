import tkinter as tk
import requests
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Weather App")
root.geometry("600x500")


# Key: 2c481575c96a35678b7b4ec3d1f441d6
# API url: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def format_response(weather):
    try:
        city = (weather['name'])
        condition = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])
        final_str = 'City:%s\nCondition:%s\nTemperature:%s' % (city, condition, temp)
    except:
        final_str = 'There was problem retrieving information'
    return final_str


def get_weather(city):
    weather_key = '2c481575c96a35678b7b4ec3d1f441d6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    # print(response.json())
    weather = response.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

    result['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size = int(frame_two.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


img = Image.open('./bg.png')
img = img.resize((600, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

heading_title = tk.Label(bg_lbl, text='Know Temperature of 10,000 Cities!', fg='black', bg='sky blue',
                         font=('times new roman', 16, 'bold'))
heading_title.place(x=80, y=18)

frame_one = tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_one.place(x=80, y=60, width=450, height=50)

txt_box = tk.Entry(frame_one, font=('times new roman', 25), width=17)
txt_box.grid(row=0, column=0, sticky="w")

btn = tk.Button(frame_one, text="Get Weather", fg='green', font=('times new roman', 16, 'bold'),
                command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_two.place(x=80, y=130, width=450, height=300)

result = tk.Label(frame_two, font=40, bg='white', justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(result, bg='white', bd=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()

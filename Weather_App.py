from tkinter import *
from PIL import ImageTk,Image
import requests
import json



root=Tk()
root.title("Weather app")
#root.geometry("500x500")
#root.configure(background="#ffcccc")

def output():
    global condition_colour
    global condition
    try:
   
        api_request=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city.get()+","+state.get()+","+Country.get()+"&appid=b98e11892721adc7fc032693db2dcf53")
        api=json.loads(api_request.content)
        condition=api["weather"][0]["main"]
        description=api["weather"][0]["description"]
        Temperature=api["main"]["temp"]
        temp_c=round(Temperature-273.15,2)
        
        if condition=="Clouds":
            condition_colour="#33ccff"
        elif condition=="Clear":
            condition_colour="#ffffff"
        elif condition=="Tornado":
            condition_colour="#808080"
        elif condition=="Squall":
            condition_colour="#3d3d3d"
        elif condition=="Ash":
            condition_colour="#ff3300"
        elif condition=="Dust":
            condition_colour="#996633"
        elif condition=="Sand":
            condition_colour="#ff6600"
        elif condition=="Fog":
            condition_colour="#ffccff"
        elif condition=="Haze":
            condition_colour="#ccffcc"
        elif condition=="Smoke":
            condition_colour="#666699"
        elif condition=="Mist":
            condition_colour="#9999ff"
        elif condition=="Snow":
            condition_colour="#ffffcc"
        elif condition=="Rain":
            condition_colour="#0066cc"
        elif condition=="Drizzle":
            condition_colour="#66ffff"
        elif condition=="Snow":
            condition_colour="#ffffcc"
        elif condition=="Thunderstrom":
            condition_colour="#993333"

        #root.configure(background=condition_colour)
        my_label=Label(root,text="Current Weather condition: " +condition+" " +"\n"+"Description: "+description,background=condition_colour,font=("Roman Times","15","bold"),relief="sunken",justify="left")
        my_label.grid(row=6,column=0,columnspan=3,stick=W+E+N+S)
        
    except Exception as e:
        api="Error.."
def submit():
    try:
        global weather_colour
        api_request2=requests.get("http://api.waqi.info/feed/"+city.get()+"/?token=9ef9f902ab4a0be0ea91df9be80b0bc8a41ef662")
        api=json.loads(api_request2.content)
        aq=api["data"]["aqi"]
        citynm=api["data"]["city"]["name"]
        if aq>=0 and aq<=50:
            weather_colour="#0C0"
            quality="Good"
            #return "Good"
        elif aq>50 and aq<=100:
            weather_colour="#FFFF00"
            quality="Moderate"
            #return "Moderate"
        elif aq>100 and aq<=150:
            weather_colour="#ff6600"
            quality="Unhealthy for Sensitive Group"
        elif aq>150 and aq<=200:
            weather_colour="#ff3300"
            quality="Unhealthy"
        elif aq>201 and aq<=300:
            weather_colour="#cc00cc"
            quality="Very Unhealthy"
        elif aq>300:
            weather_colour="#990000"
            quality="Hazardous"

        lb=Label(root,text=quality+"\n"+"Air Quality Index= "+str(aq),background=weather_colour,font=("Roman Times","17","bold"),relief="sunken",justify="left")
        lb.grid(row=5,column=0,columnspan=3,stick=W+E+N+S)
        #root.configure(background=weather_colour)
    except Exception as e:
        api="Error.."
def teempu():
    global condition_colour
    global condition
    try:
   
        api_request=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city.get()+","+state.get()+","+Country.get()+"&appid=b98e11892721adc7fc032693db2dcf53")
        api=json.loads(api_request.content)
        condition=api["weather"][0]["main"]
        description=api["weather"][0]["description"]
        Temperature=api["main"]["temp"]
        temp_c=round(Temperature-273.15,2)
        
        if condition=="Clouds":
            condition_colour="#33ccff"
        elif condition=="Clear":
            condition_colour="#ffffff"
        elif condition=="Tornado":
            condition_colour="#808080"
        elif condition=="Squall":
            condition_colour="#3d3d3d"
        elif condition=="Ash":
            condition_colour="#ff3300"
        elif condition=="Dust":
            condition_colour="#996633"
        elif condition=="Sand":
            condition_colour="#ff6600"
        elif condition=="Fog":
            condition_colour="#ffccff"
        elif condition=="Haze":
            condition_colour="#ccffcc"
        elif condition=="Smoke":
            condition_colour="#666699"
        elif condition=="Mist":
            condition_colour="#9999ff"
        elif condition=="Snow":
            condition_colour="#ffffcc"
        elif condition=="Rain":
            condition_colour="#0066cc"
        elif condition=="Drizzle":
            condition_colour="#66ffff"
        elif condition=="Snow":
            condition_colour="#ffffcc"
        elif condition=="Thunderstrom":
            condition_colour="#993333"

        #root.configure(background=condition_colour)
        my_label=Label(root,text="Current Temperature in Kelvin: "+str(Temperature)+"\n"+"Current Temperature in Celcius: "+str(temp_c),background=condition_colour,font=("Roman Times","15","bold"),relief="sunken",justify="left")
        my_label.grid(row=4,column=0,columnspan=3,stick=W+E+N+S)
        
    except Exception as e:
        api="Error.."
    


citynm1=Entry(root)
citynm1.grid(row=0,column=0,stick=W+E+N+S)
submit=Button(root,text="Air Quality",command=submit,background="#ccffff",fg="black",relief="raised",font=("Arial","15","bold"))
submit.grid(row=2,column=1,stick=E+W+N+S,padx=4,pady=4)

city=Entry(root,font=("Arial","15","bold"),relief="sunken")
city.grid(row=1,column=0,stick=W+E+N+S)
city_label=Label(root,text="City Name",font=("Arial","15","bold"))
city_label.grid(row=0,column=0,stick=W+E+N+S)
state=Entry(root,font=("Arial","15","bold"),relief="sunken")
state.grid(row=1,column=1,stick=W+E+N+S)
state_label=Label(root,text="State Name",font=("Arial","15","bold"))
state_label.grid(row=0,column=1,stick=W+E+N+S)
Country=Entry(root,font=("Arial","15","bold"),relief="sunken")
Country.grid(row=1,column=2,stick=W+E+N+S)
Country_label=Label(root,text="Country Name",font=("Arial","15","bold"))
Country_label.grid(row=0,column=2,stick=W+E+N+S)

def button_clear():
    city.delete(0,END)
    state.delete(0,END)
    Country.delete(0,END)

weather_btn=Button(root,text="Weather Condition",command=output,bg="#ccffff",fg="black",relief="raised",font=("Arial","15","bold"))
weather_btn.grid(row=2,column=2,stick=E+W+N+S,padx=4,pady=4)#,padx=10,pady=10,ipadx=20)
tempu=Button(root,text="Temperature",command=teempu,bg="#ccffff",fg="black",relief="raised",font=("Arial","15","bold"))
tempu.grid(row=2,column=0,stick=W+E+N+S,padx=4,pady=4)
clearbtn=Button(root,text="Clear",padx=4,pady=4,command=button_clear,background="#e6ffcc",relief="raised",font=("Arial","15","bold"))
clearbtn.grid(row=3,column=1,padx=4,pady=4,stick=W+E+N+S)


root.mainloop()




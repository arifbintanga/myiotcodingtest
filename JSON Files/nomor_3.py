import random
import tkinter as Tk
from itertools import count

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd

plt.style.use('classic')
# values for first graph
timestampX = []
humidity = []
# values for second graph
temperature = []

index = count(start = 1655323806,step=2)

pause = True
start = True

df = pd.DataFrame(list(zip(timestampX, humidity, temperature)),columns =['timestamp', 'humidity','temperature'])


humidity_min,humidity_max,humidity_median,humidity_mean = 0,0,0,0
temperature_min,temperature_max,temperature_median,temperature_mean = 0,0,0,0

def animate(i):
    # Generate values
    if not pause:
        timestampX.append(next(index))
        humidity.append(random.uniform(87, 97))
        temperature.append(random.uniform(17, 27))
        aggregate()

        # Get all axes of figure
        ax1, ax2 = plt.gcf().get_axes()
        # Clear current data
        ax1.cla()
        ax2.cla()
        # Plot new data
        ax1.plot(timestampX, humidity)
        ax2.plot(timestampX, temperature)

def aggregate():
        df1 = pd.DataFrame(list(zip(timestampX, humidity, temperature)),columns =['timestamp', 'humidity','temperature'])
        global df
        df = df1
        df["roomArea"]="roomArea1"

        nomor_3 = df.to_json('./nomor_3.json', orient='index')
        aggSensorData = df.groupby(['roomArea']).agg({'humidity': ['mean', 'min', 'max','median'],'temperature':['mean', 'min', 'max','median']})
        aggSensorData.columns = ['humidity_mean', 'humidity_min', 'humidity_max', 'humidity_median','temperature_mean', 'temperature_min', 'temperature_max', 'temperature_median']
        aggSensorData = aggSensorData.reset_index()
        global humidity_min,humidity_max,humidity_median,humidity_mean
        global temperature_min,temperature_max,temperature_median,temperature_mean

        humidity_mean = aggSensorData.loc[0,"humidity_mean"]
        humidity_min = aggSensorData.loc[0,"humidity_mean"]
        humidity_max = aggSensorData.loc[0,"humidity_mean"]
        humidity_median = aggSensorData.loc[0,"humidity_mean"]
        temperature_mean = aggSensorData.loc[0,"temperature_mean"]
        temperature_min = aggSensorData.loc[0,"temperature_mean"]
        temperature_max = aggSensorData.loc[0,"temperature_mean"]
        temperature_median = aggSensorData.loc[0,"temperature_mean"]

    
def setPause():
    global pause
    pause = True

def setResume():
    global pause
    pause = False
    start = False

# GUI
root = Tk.Tk()
root.geometry("")
label = Tk.Label(root, text="Simulated Temperature & Humidity").grid(column=0, row=0)

root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)

# graph 1
canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
canvas.get_tk_widget().grid(column=0, row=1, sticky="nsew",columnspan=3)

# Create two subplots in row 1 and column 1, 2
plt.gcf().subplots(1, 2)
ani = FuncAnimation(plt.gcf(), animate, interval=2000, blit=False)

# Create a Button
start = Tk.Button(root, text = 'Start', bd = '5',command = setResume)
stop = Tk.Button(root, text = 'Stop', bd = '5',command = setPause)
# Set the position of button on the top of window.  
start.grid(column=0, row=2, sticky="e") 
stop.grid(column=1, row=2, sticky="ew")

a,b,c,d = Tk.DoubleVar(),Tk.DoubleVar(),Tk.DoubleVar(),Tk.DoubleVar()
e,f,g,h  = Tk.DoubleVar(),Tk.DoubleVar(),Tk.DoubleVar(),Tk.DoubleVar()


#Create a text label
label = Tk.Label(root, text="Mean Humidity").grid(column=0, row=3, sticky="W")
label = Tk.Label(root, text="Max Humidity").grid(column=0, row=4, sticky="W")
label = Tk.Label(root, text="Min Humidity").grid(column=0, row=5, sticky="W")
label = Tk.Label(root, text="Median Humidity").grid(column=0, row=6, sticky="W")
label = Tk.Label(root, text="Mean Humidity").grid(column=0, row=3, sticky="W", padx=400)
label = Tk.Label(root, text="Max Humidity").grid(column=0, row=4, sticky="W", padx=400)
label = Tk.Label(root, text="Min Humidity").grid(column=0, row=5, sticky="W", padx=400)
label = Tk.Label(root, text="Median Humidity").grid(column=0, row=6, sticky="W", padx=400)

def every_second():
    global a
    a.set(humidity_mean)
    b.set(humidity_max)
    c.set(humidity_min)
    d.set(humidity_median)
    e.set(temperature_mean)
    f.set(temperature_max)
    g.set(temperature_min)
    h.set(temperature_median)
    root.after(1000, every_second)

root.after(2000, every_second)

#Create a text variable label
label = Tk.Label(root, textvariable=a).grid(column=0, row=3, sticky="W", padx=100)
label = Tk.Label(root, textvariable=b).grid(column=0, row=4, sticky="W", padx=100)
label = Tk.Label(root, textvariable=c).grid(column=0, row=5, sticky="W", padx=100)
label = Tk.Label(root, textvariable=d).grid(column=0, row=6, sticky="W", padx=100)
label = Tk.Label(root, textvariable=e).grid(column=0, row=3, sticky="W", padx=500)
label = Tk.Label(root, textvariable=f).grid(column=0, row=4, sticky="W", padx=500)
label = Tk.Label(root, textvariable=g).grid(column=0, row=5, sticky="W", padx=500)
label = Tk.Label(root, textvariable=h).grid(column=0, row=6, sticky="W", padx=500)

Tk.mainloop()



import plotly.graph_objects as go
import pandas as pd
import tkinter as tk
from PIL import ImageTk, Image
def click():
    global img
    df = pd.read_csv('taxData2021.csv')

    fig = go.Figure(data=go.Choropleth(
        locations=df['code'], # Spatial coordinates
        #z = df['Property Taxes'].astype(float), # Data to be color-coded
        z = df['T09'].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Reds',
        colorbar_title = "Tax",
    ))

    fig.update_layout(
        title_text = 'Tax Data 2021',
        geo_scope='usa', # limite map scope to USA
    )
    fig.write_image("fig.png")
    
    img = ImageTk.PhotoImage(Image.open("fig.png"))
    label = tk.Label(window, image=img)
    label.pack()


window = tk.Tk()
window.title("Map")
button = tk.Button(window,width=10,height=2,text="Plot",command=click)
button.pack()
window.mainloop()



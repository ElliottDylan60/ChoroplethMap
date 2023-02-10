
import plotly.graph_objects as go
import pandas as pd
import tkinter as tk
from PIL import ImageTk, Image
selectedLeft = "T01"
selectedRight = "T24"
def T1Click():
    global selectedLeft
    clearLeftButton()
    btnT1.configure(bg='gray')
    selectedLeft = "T01"
    update()
def T9Click():
    global selectedLeft
    clearLeftButton()
    btnT9.configure(bg='gray')
    selectedLeft = "T09"
    update()
def T10Click():
    global selectedLeft
    clearLeftButton()
    btnT10.configure(bg='gray')
    selectedLeft = "T10"
    update()
def T16Click():
    global selectedLeft
    clearLeftButton()
    btnT16.configure(bg='gray')
    selectedLeft = "T16"
    update()
def T24Click():
    global selectedRight
    clearRightButton()
    btnT24.configure(bg='gray')
    selectedRight = "T24"
    update()
def T25Click():
    global selectedRight
    clearRightButton()
    btnT25.configure(bg='gray')
    selectedRight = "T25"
    update()
def T40Click():
    global selectedRight
    clearRightButton()
    btnT40.configure(bg='gray')
    selectedRight = "T40"
    update()
def T41Click():
    global selectedRight
    clearRightButton()
    btnT41.configure(bg='gray')
    selectedRight = "T41"
    update()
def clearLeftButton():
    btnT1.configure(bg='#f0f0f0')
    btnT9.configure(bg='#f0f0f0')
    btnT10.configure(bg='#f0f0f0')
    btnT16.configure(bg='#f0f0f0')
def clearRightButton():
    btnT24.configure(bg='#f0f0f0')
    btnT25.configure(bg='#f0f0f0')
    btnT40.configure(bg='#f0f0f0')
    btnT41.configure(bg='#f0f0f0')
def update():
    global img
    global img2
    
    """
        Left Image
    """
    print(selectedLeft)
    df = pd.read_csv('taxData2021.csv')

    fig = go.Figure(data=go.Choropleth(
        locations=df['code'], # Spatial coordinates
        #z = df['Property Taxes'].astype(float), # Data to be color-coded
        z = df[selectedLeft].astype(float), # Data to be color-coded
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
    #label = tk.Label(window, image=img)
    leftMap.configure(image=img)
    """
        Right Image
    """
    df = pd.read_csv('taxData2021.csv')

    fig = go.Figure(data=go.Choropleth(
        locations=df['code'], # Spatial coordinates
        #z = df['Property Taxes'].astype(float), # Data to be color-coded
        z = df[selectedRight].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Reds',
        colorbar_title = "Tax",
    ))

    fig.update_layout(
        title_text = 'Tax Data 2021',
        geo_scope='usa', # limite map scope to USA
    )
    fig.write_image("fig2.png")
    
    img2 = ImageTk.PhotoImage(Image.open("fig2.png"))
    #label = tk.Label(window, image=img)
    rightMap.configure(image=img2)
    


window = tk.Tk()
window.title("Map")
window.geometry("1400x500")
"""
    Left Map Buttons
"""
btnT1 = tk.Button(window,width=10,height=2,text="T01",command=T1Click, bg="gray")
btnT1.place(x=0, y=0)
btnT9 = tk.Button(window,width=10,height=2,text="T09",command=T9Click)
btnT9.place(x=100, y=0)
btnT10 = tk.Button(window,width=10,height=2,text="T10",command=T10Click)
btnT10.place(x=200, y=0)
btnT16 = tk.Button(window,width=10,height=2,text="T16",command=T16Click)
btnT16.place(x=300, y=0)
leftMap = tk.Label(window)
leftMap.place(x=0, y=40)
"""
    Right Map Buttons
"""
btnT24 = tk.Button(window,width=10,height=2,text="T24",command=T24Click, bg="gray")
btnT24.place(x=1025, y=0)
btnT25 = tk.Button(window,width=10,height=2,text="T25",command=T25Click)
btnT25.place(x=1125, y=0)
btnT40 = tk.Button(window,width=10,height=2,text="T40",command=T40Click)
btnT40.place(x=1225, y=0)
btnT41 = tk.Button(window,width=10,height=2,text="T41",command=T41Click)
btnT41.place(x=1325, y=0)
rightMap = tk.Label(window)
rightMap.place(x=700, y=40)
update()
window.mainloop()



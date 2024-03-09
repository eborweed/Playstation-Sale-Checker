from email.mime import image
from logging import root
import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
import urllib.request
import io
import time
import GlobalVariables
from Searching import Searchbar
import csv

def DisplayButtonClick():
   
  
   try:
    if displaywindow.winfo_exists() != 1:
     print("hi")
     displaywindow.geometry("300x300")
     displaywindow.title("Display")
     with open('games.csv') as file:
      reader=csv.reader(file)
      
      for row in reader:
       tk.Label(displaywindow,text=row).pack()
   except:
     print("shit")
     displaywindow=tk.Toplevel()
     displaywindow.geometry("300x300")
     displaywindow.title("Display")
     with open('games.csv') as file:
      reader=csv.reader(file)
      
      for row in reader:
       tk.Label(displaywindow,text=row).pack()
   displaywindow.mainloop()
       
       
        
def main():
    
# Create a Tkinter window
 window = tk.Tk()
 
 # Set the window title
 window.title('Price Checker App')
 
 # Set the window size
 window.geometry('300x300')
 
 # Create a label
 
 
 textbox=tk.Entry(width=50)
 textbox.pack()
 # Create a button
 inputbutton = tk.Button(window, text='INPUT!', command= lambda: inputButtonClick(window,textbox))
 
 inputbutton.pack()
 label = tk.Label(window, text='Input Button!')
 DisplayButton = tk.Button(window,text='display',command=DisplayButtonClick)
 DisplayButton.pack()
 # Start the main event loop
 window.mainloop()
def SelectButtonClick(name,price,link):   
    with open('games.csv', 'a',newline='') as file:
     writer = csv.writer(file)
     field=['Title','Price','Link']
     writer.writerow([name,price,link])
     
     
     

def inputButtonClick(window,textbox):
    GlobalVariables.gamename= textbox.get()
    names, images, prices, oldPrices, links, gamenum = Searchbar.Searchbar(GlobalVariables.gamename) #Find 
    print('Button clicked!')
    inputwindow= tk.Toplevel()
    inputwindow.title("Input window")
    inputwindow.geometry('600x600')
    photos= [0,0,0,0,0,0,0,0]

    for i in range(0,gamenum):
      selectbuttons={}
      with urllib.request.urlopen(images[i]) as u:
       raw_data = u.read()
      
      image = Image.open(io.BytesIO((raw_data)))
      image=image.resize((50,50))
      
      
      photos[i]= ImageTk.PhotoImage(image)
     # Create a label widget to display the image
      imagelabel = tk.Label(inputwindow, image=photos[i])
      
      imagelabel.place(rely=0.125*i,relx=0)
      #gamename displayed in the middle of the image to its side
      tk.Label(inputwindow,text=names[i]).place(rely=(0.125)*i+0.125*0.25, x=50) 

      

      tk.Label(inputwindow,text=prices[i].text +" cut from " + oldPrices[i]).place(rely=(0.125)*i+0.125*0.25, x=350)
    selectbutton0= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[0],prices[0].text,links[0])).place(rely=(0.125)*0+0.125*0.25,x=500)
    selectbutton1= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[1],prices[1].text,links[1])).place(rely=(0.125)*1+0.125*0.25,x=500)
    selectbutton2= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[2],prices[2].text,links[2])).place(rely=(0.125)*2+0.125*0.25,x=500)
    selectbutton3= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[3],prices[3].text,links[3])).place(rely=(0.125)*3+0.125*0.25,x=500)
    selectbutton4= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[4],prices[4].text,links[4])).place(rely=(0.125)*4+0.125*0.25,x=500)
    selectbutton5= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[5],prices[5].text,links[5])).place(rely=(0.125)*5+0.125*0.25,x=500)
    selectbutton6= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[6],prices[6].text,links[6])).place(rely=(0.125)*6+0.125*0.25,x=500)
    selectbutton7= tk.Button(inputwindow, text="add to wishlist",command= lambda: SelectButtonClick(names[7],prices[7].text,links[7])).place(rely=(0.125)*7+0.125*0.25,x=500)
   
    inputwindow.mainloop()
   
       
 

if __name__ == '__main__':
    main()


# coding: utf-8

# In[2]:


from tkinter import *


# In[5]:


class Window(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master = master
        
        self.init_window()
        
    def init_window(self):
        
        self.master.title("Colour Predictor")
        
        self.pack(fill=BOTH, expand=1)
        
        quitButton = Button(self, text="Quit", command=self.client_exit)
        
        quitButton.place(x=0, y=0)
        
    def client_exit(self):
        exit()
# In[7]:

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()


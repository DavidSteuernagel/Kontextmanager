#!/usr/bin/env python
# coding: utf-8

# In[2]:


file = open ("./text.txt","w")
file.write("Hallo")
file.close()
#Datei bleibt geöffnet, wenn  man das Schließen vergisst


# In[7]:


with open ("./text.txt","w") as file:
    file.write("Hallo")
#Datei wird automatisch geschlossen, auch bei Fehlern


# In[11]:


#Contextlib

#Beispiel ohne Contextlib

class MyContext:
    def __enter__ (self):
        print("Start")
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("End")

with MyContext():
    print ("Drin")


# In[16]:


#Beispiel mit Contextlib

from contextlib import contextmanager

@contextmanager
def my_context():
    print ("Start")   #wie __enter__
    yield             #übergibt Kontrolle an den with-Block
    print ("End")     #wie __exit__

with my_context():
    print ("Drin")


# In[ ]:


import threading

lock = threading.Lock()

with lock:
    #nur ein Thread darf diesen Code gleichzeitig ausführen
    critical_section()


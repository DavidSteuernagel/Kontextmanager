#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time                                        # time-modul wird importiert, um die aktuelle Zeit zu messen

class Timer:                                       # neue Klasse wird erstellt, kann später verwendet werde, um, die Zeit zu messen
    def __enter__(self):                           # startet die Zeitmessung
        self.start=time.time()                     # speichert den aktuellen Zeitpunkt
        return self                                # gibt das Timer-Objekt zurück ->with-Block als t ansprechbar

    def __exit__(self, exc_type, exc_val, exc_tb): # wird automatisch ausgeführt,
                                                   # wenn der with Block endet, trotz möglicher Fehler
                                                   # exc_type, exc_val, exc_tb sind Standardparameter, die für die Fehlerbehandlung
                                                   #-> werden hier nicht verwendet, müssen aber trotzdem vorhanden sein
        self.end=time.time()                       #speichert wieder den aktuellen Zeitpunkt
        print (f'Vergangene Zeit: {self.end-self.start:.4f} Sekunden')# berechnet den Unterschied zwischen den beiden Zeiten und
                                                                      # rundet auf 4 Nachkommastellen und gibt ihn aus

with Timer () as t:
    sorted([x for x in range(1000000, 0, -1)])

# hier wird automatisch __enter__ () aufgerufen und die Startzeit gemessen
# Der Codeblock, in diesem Fall die Schleife, wird ausgeführt
# dann wird automatisch __exit__() aufgerufen, die Endzeit gemessen, und die Differenz der beiden Zeiten wird ausgegeben


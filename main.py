#importing all the required packages
import eel
import pandas as pd
import numpy as np


@eel.expose                                     #connecting to javascript at frontend

#receiving data from JS
def JSDataToPython():
    print("Hello from JS")


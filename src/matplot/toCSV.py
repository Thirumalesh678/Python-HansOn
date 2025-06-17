import numpy as np
import pandas as pd
 
data = {
    'colors' : ["red", "green", "yellow", "magenta", "brown", "purple"] ,
     'Quantity' : [25,90,145,35,170,110]
}
df = pd.DataFrame(data)
df.to_csv('colors.csv',index=False)
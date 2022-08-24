# importamos la libreria panda 
import pandas as pd
from pushbullet import Pushbullet
from dotenv import load_dotenv
import os 
load_dotenv() 

# abrimos el archivo exel
df = pd.read_excel("producto.xlsx")
print(df)

print("---------------")

# producto cantidad


# se filtra por la columna "cantidad" los que tienen menos 5
menos5 = df[df["CANTIDAD"]<5]
print(menos5)

diccionario = menos5.to_dict('list')

productos_faltantes = diccionario['PRODUCTO']
productos_faltantes = str(productos_faltantes).replace('[', "").replace(']', ",")
print('producto_faltante  ', productos_faltantes)

KEY = os.getenv("API_KEY")
if not menos5.empty:
    pb = Pushbullet(KEY)

    push = pb.push_note("Aviso de stock", f"Los siguientes producto estan en falta: {productos_faltantes}")

# Get all devices that the current user has access to.
print(pb.devices)
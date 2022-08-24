from flask import Flask, render_template
from flask import request

import pandas as pd 

def actualizar_excel(proveedor, cel, email): 

    # creacion de diccionario y dataframe 
    datos = {"Proveedor" : [proveedor],
            "Email": [email], 
            "Celular": [cel]
            }
    print(datos)

    # crear dataframe 
    datos_df= pd.DataFrame.from_dict(datos)

    # Guardar archivo en un df 
    excel_df = pd.read_excel('Datos.xlsx')
    posicion = excel_df.shape[0] + 1

    # Append nuevo dato
    with pd.ExcelWriter("Datos.xlsx", mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
        datos_df.to_excel(writer, sheet_name='Sheet1', startrow=posicion, header=False, index=False )
        print("Se ha agregado un prooveedor correctamente.")

app = Flask(__name__)

@app.route("/carga-proveedor", methods=['POST', 'GET'])
def proveedor():
    if request.method == 'POST':
        proveedor = request.form['proveedor']
        print(proveedor)
        email = request.form['email']
        print(email)
        cel = request.form["telefono"]
        print(cel)
        actualizar_excel(proveedor, cel, email) 
        return render_template('proveedor.html')
    return render_template('proveedor.html')

@app.route("/carga-producto", methods=['GET', 'POST'])
def producto():
    if request.method == 'POST':
        my_list = []
        my_list.append(request.form['nombre'])
        my_list.append(request.form['proveedor'])
        my_list.append(request.form['costo'])
        my_list.append(request.form['cantidad'])
        print(my_list)

        my_dict = {}
        my_dict['Columns'] = ['nombre', 'proveedor', 'costo', 'cantidad']
        my_dict['values'] = my_list
        print(my_dict)

        my_dict_df = pd.DataFrame.from_dict(my_dict)
        print(my_dict_df)

        # save to excel

        my_dict_df.to_excel('listado_proveedores.xlsx')

    return render_template('productos.html')

if __name__ == '__main__': #por defecto es main el código
    app.run(debug= True, port="4000", host="0.0.0.0")
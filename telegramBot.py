import logging 
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import pandas as pd 

# metodo para rastrear eventos (para ver lo que hace el bot)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")
logger = logging.getLogger()

# token del bot 
TOKEN = '5791582892:AAFrnf7QRi6BWJUGcQGmZ1DFtuDiX7S8OH0'
       
# lee y valida el texto 
def echo (update, context): 
    bot = context.bot 
    chatId = update.message.chat_id
    
    # obtener el id del mensaje 
    updateMsg = getattr(update, 'message', None) # guardamos todos los datos del mensaje 
    messageId = updateMsg.message_id 
    
    # obtener el texto que envio al chat
    text = update.message.text
       
    # extraer pedido y cantidad 
    pedido = text[10:text.index('\n')]
    cantidad = text[(text.index('\n')+13):(len(text))]

    # creacion de diccionario y dataframe 
    datos = {"Pedido" : [pedido],
            "Cantidad": [cantidad]
            }
    
    datos_df= pd.DataFrame.from_dict(datos)
    
    # Guardar archivo en un df 
    excel_df = pd.read_excel('Datos.xlsx')   
    posicion = excel_df.shape[0] + 1

    # Append nuevo dato
    with pd.ExcelWriter("Datos.xlsx", mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
        datos_df.to_excel(writer, sheet_name='Sheet1', startrow=posicion, header=False, index=False )  
        print("Se ha agregado un pedido correctamente.")
        print(datos)
    
# main
if __name__ == '__main__': 
    # obtener info del bot 
    myBot = telegram.Bot(token =  TOKEN)

updater = Updater(myBot.token, use_context=True) # updater: recibe mensajes y comandos 
dp = updater.dispatcher  # dispathcher: comandos que puede recibir 

# mensajes!
dp.add_handler(MessageHandler (Filters.text, echo))

# polling 
updater.start_polling()
updater.idle() # finalizar con ctrl c  
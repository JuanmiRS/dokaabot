import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()

from telegram.ext import Updater

# token del bot proporcionado por BotFather
TOKEN = '5858964270:AAFgrZrOSCphlLjC9P-0hIk6lVsNTfRqVWQ'

# Crea una instancia del objeto Updater
updater = Updater(token=TOKEN, use_context=True)

# Obtiene el objeto Dispatcher para registrar comandos y manejar actualizaciones
dispatcher = updater.dispatcher

# Inicia el bot
updater.start_polling()

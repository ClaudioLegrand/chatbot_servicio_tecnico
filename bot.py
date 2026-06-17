# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# TOKEN = "8897589497:AAFk4Hkyk9pl7pO4QdsRtV_yCIjmJgkpPYk"

# garantias_dni = {
#     "12345678": True,
#     "87654321": False,
#     "11223344": True
# }

# garantias_factura = {
#     "F001": True,
#     "F002": False,
#     "F003": True
# }

# usuarios = {}

# async def start(update, context):
#     user_id = update.message.chat_id
#     usuarios[user_id] = {"estado": "esperando_nombre"}
#     await update.message.reply_text("👋 Bienvenido al servicio técnico de celulares.\n¿Cuál es tu nombre?")

# async def mensaje(update, context):
#     user_id = update.message.chat_id
#     texto = update.message.text.strip()

#     if user_id not in usuarios:
#         await update.message.reply_text("Por favor iniciá la consulta con /start")
#         return

#     estado = usuarios[user_id]["estado"]

#     if estado == "esperando_nombre":
#         if len(texto) < 2:
#             await update.message.reply_text("⚠️ Por favor ingresá un nombre válido.")
#             return
#         usuarios[user_id]["nombre"] = texto
#         usuarios[user_id]["estado"] = "esperando_documento"
#         await update.message.reply_text(f"Hola {texto} 👋\nIngresá tu DNI o número de factura:")

#     elif estado == "esperando_documento":
#         if texto.upper().startswith("F"):
#             clave = texto.upper()
#             en_garantia = garantias_factura.get(clave)
#         else:
#             en_garantia = garantias_dni.get(texto)

#         if en_garantia is None:
#             await update.message.reply_text("⚠️ No encontramos ese dato. Verificá e intentá de nuevo.")
#             return

#         usuarios[user_id]["documento"] = texto

#         if en_garantia:
#             usuarios[user_id]["estado"] = "fin_garantia"
#             await update.message.reply_text(
#                 "✅ Tu equipo está en garantía.\n\n"
#                 f"👤 Cliente: {usuarios[user_id]['nombre']}\n"
#                 f"📄 Documento: {texto}\n"
#                 f"🎫 Ticket: TKT-{user_id}\n\n"
#                 "📅 Un técnico te va a contactar para coordinar el turno."
#             )
#         else:
#             usuarios[user_id]["estado"] = "esperando_falla"
#             await update.message.reply_text(
#                 "❌ El equipo no está en garantía.\n\n"
#                 "Seleccioná el tipo de falla:\n"
#                 "1 - Pantalla rota\n"
#                 "2 - Batería\n"
#                 "3 - Puerto de carga\n"
#                 "4 - Otro problema"
#             )

# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje))

# print("Bot corriendo...")
# app.run_polling()

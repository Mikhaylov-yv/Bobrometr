from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import scr.get_class as get_class
import scr.bot_data as bot_data

updater = Updater(token = bot_data.token, use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= 'Пришлите мне ваше фото, я попробую определить есть ли там бобёр')

def img(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text= 'Это фотография')
    fil_id = update.message.photo[0].file_id
    new_file = context.bot.getFile(fil_id)
    print(new_file.file_path)
    class_name, msg = get_class.predict_class(new_file.file_path)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= f'Похоже это {class_name}' + '\n' + msg)


start_handler = CommandHandler('start', start)
img_handler = MessageHandler(Filters.photo & (~Filters.command), img)
dispatcher.add_handler(img_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
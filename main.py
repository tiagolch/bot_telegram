import telebot


CHAVE_API = '<ChaveFornecidaPelo_BotFather_doTelegram>'
bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['Escala_Broadcast'])
def ver_escala(mensagem):
    text = """
        ESCALA - BROADCAST
        JANEIRO

        02/01 - DOMINGO
        MANHÃ
        Câmera 01: 
        Corte: Fernanda

        NOITE: NÃO HAVERÁ CULTO

        09/01 - DOMINGO
        MANHÃ
        Câmera 01: Lauro
        Corte: Tiago 

        NOITE
        Câmera 01: T.H 
        Corte: Sophia

        16/01 - DOMINGO
        MANHÃ
        Câmera 01: Breno
        Corte: Tiago

        NOITE
        Câmera 01: TH
        Corte: Sophia

        23/01 - DOMINGO
        MANHÃ
        Câmera 01: Lauro
        Corte: Fernanda

        NOITE
        camera: TH
        Corte: Sophia

        30/01 - DOMINGO
        MANHÃ
        Câmera 01: Breno
        Corte: Tiago

        NOITE
        camera: 
        Corte: Fernanda
    """
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['Escala_DI'])
def ver_escala(mensagem):
    text = """
        ESCALA - DI
        JANEIRO

        02/01 - DOMINGO
        MANHÃ
        Vanessa

        NOITE: NÃO HAVERÁ CULTO

        09/01 - DOMINGO
        MANHÃ
        Ciclana 

        NOITE
        Beltrana

        16/01 - DOMINGO
        MANHÃ
        Fulana

        NOITE
        Vanessa

        23/01 - DOMINGO
        MANHÃ
        Fulana 2

        NOITE
        Sophia

        30/01 - DOMINGO
        MANHÃ
        Beltrana

        NOITE
        Fernanda
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=['Escala_Diaconato'])
def ver_escala(mensagem):
    text = """
        ESCALA - Diaconato
        JANEIRO

        02/01 - DOMINGO
        MANHÃ
        Wagner
        Fulano 
        Ciclano

        NOITE: NÃO HAVERÁ CULTO

        09/01 - DOMINGO
        MANHÃ
        Ciclana 
        Wagner
        Fulano 
        Ciclano

        NOITE
        Beltrana
        Wagner
        Fulano 
        Ciclano

        16/01 - DOMINGO
        MANHÃ
        Fulana
        Wagner
        Fulano 
        Ciclano

        NOITE
        Vanessa
        Wagner
        Fulano 
        Ciclano

        23/01 - DOMINGO
        MANHÃ
        Fulana 2
        Wagner
        Fulano 
        Ciclano

        NOITE
        Sophia
        Wagner
        Fulano 
        Ciclano

        30/01 - DOMINGO
        MANHÃ
        Beltrana
        Wagner
        Fulano 
        Ciclano

        NOITE
        Fernanda
        Wagner
        Fulano 
        Ciclano
    """
    bot.send_message(mensagem.chat.id, text)


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    text = """
    Escolha uma das opções abaixo: (click em um link)

        /Escala_Broadcast - Para ver a escala da equipe de transmissão
        /Escala_DI - Para ver a escala da responsavel 
        /Escala_Diaconato- Para ver a escala dos envolvidos
    
Voce deve escolher uma das opções acima para que eu possa te ajudar.
    """
    bot.reply_to(mensagem, text)

bot.polling()

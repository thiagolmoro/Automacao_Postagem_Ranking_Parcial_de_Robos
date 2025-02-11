# pip install pyautogui pyperclip pyscreenshot

import pyautogui as pa # importa o pacote pyautogui
import time # importa o pacote time
import pyscreenshot # importa o pacote pyscreenshot
import pyperclip # importa o pacote pyperclip

pa.PAUSE = 0.5

time.sleep(1)

dia = "17"
mes = "10"
ano = "2023"
mini_win = "WINV23"
mini_wdo = "WDOX23"

pa.hotkey("win", "1") # Aperta a combinação de tecla Windows + 6
time.sleep(10) # Faz o código aguardar 10 segundos antes de executar o próximo comando
pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
pa.write("http://tgrafi.co/rank") # digita esse texto no local em que o cursor estiver
time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
pa.press("enter") # Aperta a tecla Enter
time.sleep(5) # Faz o código aguardar 2 segundos antes de executar o próximo comando

pa.click(x=384, y=272)

pa.scroll(-380)

time.sleep(5)

image = pyscreenshot.grab(bbox=(298, 198, 1600, 980)) # faz a captura da tela com os parametros locais indicados, sendo x1, y1, x2 e y2
# image.show() # exibe a imagem capturada

# Caminho da imagem - D:\Google Drive - Trader\3 - Ranking Parcial dos Robôs para hoje\
image.save("D:/Google Drive - Trader/3 - Ranking Parcial dos Robôs para hoje/"+ano+"_"+mes+"/"+ano+"_"+mes+"_"+dia+"/Captura.png") # salva a imagem capturada e salva nesse caminho com o nome Captura.png

time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
pa.hotkey("alt", "f4") # Aperta a combinação de tecla Alt + f4 para fechar a janela


# POSTAR NO FACEBOOK E INSTAGRAM
pa.hotkey("win", "2") # Aperta a combinação de tecla Windows + 6
time.sleep(10) # Faz o código aguardar 10 segundos antes de executar o próximo comando
pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
pa.write("https://business.facebook.com/creatorstudio/home") # digita esse texto no local em que o cursor estiver
pa.press("enter") # Aperta a tecla Enter
time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("enter") # Aperta a tecla Enter
time.sleep(8) # Faz o código aguardar 8 segundos antes de executar o próximo comando
pa.click(x=353, y=121)
pa.press("tab") # Aperta a tecla tab
pa.press("down") # Aperta a tecla para baixo
pa.press("down") # Aperta a tecla para baixo
pa.press("space") # Aperta a tecla espaço
pa.click(x=353, y=121)
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("enter") # Aperta a tecla Enter
pa.press("enter") # Aperta a tecla Enter
time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando

pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando

caminho = "D:/Google Drive - Trader/3 - Ranking Parcial dos Robôs para hoje/"+ano+"_"+mes+"/"+ano+"_"+mes+"_"+dia
pyperclip.copy(caminho) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
pa.press("enter") # Aperta a tecla Enter
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.write("Captura.png")
pa.press("enter") # Aperta a tecla Enter

# TEXTO PARA O FACEBOOK
pa.press("tab") # Aperta a tecla tab
pa.press("space") # Aperta a tecla espaço
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab

frase_facebook = "🚀 Veja agora o Ranking Parcial dos 10 melhores Robôs de hoje 📈\n\nVeja em: http://tgrafi.co/rank 🤖💡\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nAcesse www.tradergrafico.com.br e saiba mais! 📌\n\n#"+mini_win+" #"+mini_wdo+" #b3 #thautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife #money #traderlifestyle #traderbrasil #dolar #investimento  🚀🔝"
pyperclip.copy(frase_facebook) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando

#TEXTO PARA O INSTAGRAM
pa.hotkey("shift", "tab") # Aperta a combinação de tecla Shift + Tab
pa.press("right") # Aperta a tecla para direita
pa.press("enter") # Aperta a tecla Enter
pa.press("tab") # Aperta a tecla tab

frase_instagram = "🚀 Veja agora o Ranking Parcial dos 10 melhores Robôs de hoje 📈\n\nVeja em: http://tgrafi.co/rank 🤖💡\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nClique no link na bio e saiba mais! 📌\n\n#"+mini_win+" #"+mini_wdo+" #b3 #thautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #daytrading #trading #investidores #tradergrafico #miniindice #daytraderlife #money #traderlifestyle #traderbrasil #dolar #investimento  🚀🔝"
pyperclip.copy(frase_instagram) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("enter") # Aperta a tecla Enter

time.sleep(15) # Faz o código aguardar 15 segundos antes de executar o próximo comando


# POSTAR NO TWITTER
pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
time.sleep(2) # Faz o código aguardar 5 segundos antes de executar o próximo comando
pa.write("https://twitter.com/home") # digita esse texto no local em que o cursor estiver
time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
pa.press("enter") # Aperta a tecla Enter
time.sleep(10) # Faz o código aguardar 5 segundos antes de executar o próximo comando

pa.click(x=795, y=248)

frase = "Veja agora o Ranking Parcial dos 10 melhores Robôs de hoje\nVeja em: http://tgrafi.co/rank\n\n#"+mini_win+" #"+mini_wdo+" #b3 #thautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #trader "
pyperclip.copy(frase) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("enter") # Aperta a tecla Enter
time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando

pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando
pyperclip.copy(caminho) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver

time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
pa.press("enter") # Aperta a tecla Enter
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.write("Captura.png")
time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
pa.press("enter") # Aperta a tecla Enter

time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando

pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab
pa.press("tab") # Aperta a tecla tab    
pa.press("enter") # Aperta a tecla Enter

time.sleep(10) # Faz o código aguardar 10 segundos antes de executar o próximo comando

pa.hotkey("alt", "f4") # Aperta a combinação de tecla Alt + f4 para fechar a janela


# # POSTAR NO TELEGRAM
# pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
# time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
# pa.write("https://t.me/tradergrafico")  # digita esse texto no local em que o cursor estiver
# pa.press("enter") # Aperta a tecla Enter
# time.sleep(8) # Faz o código aguardar 8 segundos antes de executar o próximo comando

# pa.click(x=708, y=1011)
# time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando
# pa.hotkey("ctrl", "l") # Aperta a combinação de tecla Ctrl+l
# time.sleep(3) # Faz o código aguardar 3 segundos antes de executar o próximo comando

# pyperclip.copy(caminho) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
# pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
# time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
# pa.press("enter") # Aperta a tecla Enter
# pa.press("tab") # Aperta a tecla tab
# pa.press("tab") # Aperta a tecla tab
# pa.press("tab") # Aperta a tecla tab
# pa.press("tab") # Aperta a tecla tab
# pa.press("tab") # Aperta a tecla tab

# pa.write("Captura.png")
# time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
# pa.press("enter") # Aperta a tecla Enter

# time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando

# texto_telegram = "🚀 Veja agora o Ranking Parcial dos 10 melhores Robôs de hoje 📈\n\nVeja em: http://tgrafi.co/rank 🤖💡\n\nNão fique de fora! Seu sucesso é a nossa maior recompensa. Vem conosco e faça parte dessa revolução! 🌟\n\nAcesse www.tradergrafico.com.br e saiba mais! 📌\n\n#"+mini_win+" #"+mini_wdo+" #b3 #thautobot #dinheiro #robos #bolsadevalores #sucesso #daytrader #daytrade #cm #mercadofinanceiro #bmf #investimentos #traderlife #bovespa #tophedger #vidadetrader #trader #daytrading #trading #investidores #tradergrafico #miniindice #dolar #investimento  🚀🔝"

# pyperclip.copy(texto_telegram) # copia a frase para o clipboard para poder passar pelo problema de caracter especial que o pyautogui não reconhece como acentos e ç
# pa.hotkey("ctrl", "v") # cola a frase no local em que o cursor estiver
# time.sleep(2) # Faz o código aguardar 2 segundos antes de executar o próximo comando
# pa.press("enter") # Aperta a tecla Enter

# time.sleep(5) # Faz o código aguardar 5 segundos antes de executar o próximo comando
# pa.hotkey("win", "2") # Aperta a combinação de tecla Windows + 2
# time.sleep(4) # Faz o código aguardar 4 segundos antes de executar o próximo comando
# pa.hotkey("alt", "f4") # Aperta a combinação de tecla Alt + f4 para fechar a janela
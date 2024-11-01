arquivo_png = open( "wallpaper.jpg", 'rb')
arquivo_saida = open( "wallpaper_ori_saida.jpg", 'wb')

retorno_png = arquivo_png.read()
arquivo_saida.write(retorno_png)
print(retorno_png)

arquivo_png.close()
arquivo_saida.close()
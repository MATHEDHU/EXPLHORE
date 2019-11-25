import cv2
import numpy as np                        # Importar a biblioteca         
from matplotlib import pyplot as plt

Perfil = cv2.imread('C:\\Users\\MATHEUS EDHUARDO\\Desktop\\EXPLHORI\\Perfil 01.jpg',cv2.IMREAD_COLOR)      
                                          # Criar uma variável que receberá o comando de abertura do arquivo.
                                        
#  Criar histograma

color = ('b', 'g', 'r')
for i, col in enumerate(color):
   histr = cv2.calcHist([Perfil], [i], None, [256], [0, 256])
   plt.plot(histr, color = col)
   plt.xlim([0, 256])
cv2.imshow("Perfil 01", Perfil)           # Comando responssavel por fazer com que a imahgem apareca na tela.

plt.show()
cv2.waitKey(0)                            # Tempo ao qual a imagem permanecerá na tela após um click do usuário.
cv2.destroyAllWindows()                   # Fecha todas as janelas abertas pelo programa.

"""
print (carregarImagem.shape)           # Mostra as dimensões da imagem.
cv2.imwrite("Teste.PNG", carregarImagem)        # Salva um novo arquivo.

print (carregarImagem.item(0,0,2),carregarImagem.item(0,0,1),carregarImagem.item(0,0,0))
# O comando acima serve para mostrar as cores do pixel (posição em y,posição em x, canal da cor (R(2),G(1),B(0))


carregarImagem.itemset((0,0,2),255)   # Modifica o tom de vermelho.
carregarImagem.itemset((0,0,1),0)     # Modifica o tom de verde.
carregarImagem.itemset((0,0,0),0)     # Modifica o tom de azul.


cv2.imwrite("teste2.PNG", carregarImagem)
# Função que modifica um pixel ((posição em y, posição em x, canal que deseja ser modificado), novo valor do canal)

# Fragmento = carregarImagem[y:y,x:x] 
# Este comando é capaz de selecionar uma area especifica da imagem                                                                                                     [(y onde começa):(y onde termina),(x onde começa):(x onde termina)]

cv2.imwrite("teste2.PNG", Fragmento)  # este comando pode salvar a area da imagem selecionada.

carregarImagem[y:y,x:x] = Fragmento   # Este comando serve como um Ctrl V, pois coloca a area da imagem selecionada em outro local OBS: o tamanho da imagem deve ser respeitado.

cv2.imwrite("teste3.PNG", carregarImagem)

##########################################          Histograma:     #################################################

Img = cv2.imread("Capturar1.PNG")

plt.hist(Img.ravel(),256,[0, 256])
cv2.imshow("Imagem Original", Img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

# Para Criar um histograma colorido de cada cor.

color = ('b', 'g', 'r')
for i, col in enumerate(color):
   histr = cv2.calcHist([Img], [i], None, [256], [0, 256])
   plt.plot(histr, color = col)
   plt.xlim([0, 256])
cv2.imshow("Capturar1", Img)
plt.show()
cv2.waitKey(0)
destroyAllWindows()
"""
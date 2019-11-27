import cv2
import numpy as np                        # Importar a biblioteca         
from matplotlib import pyplot as plt

Perfil = cv2.imread('C:\\Users\\MATHEUS EDHUARDO\\Desktop\\EXPLHORI\\Perfil 01.jpg')

print (Perfil.shape)     # Dimenssões da imagem.

def ARM(y, x):
    for i in range(y, 0, -1):
        for j in range(x, 0, -1):
            (b, g, r) = Perfil[0, 0]
    return print("Cor do pixel em (%i, %i) - Vermelho: %d, Verde: %d, Azul: %d" % (i, j, r, g, b))

H = Perfil.shape[0]      # print ("Altura (height): %d pixels"%(Perfil.shape[0]))
L = Perfil.shape[1]      # print ("Largura (width): %d pixels"%(Perfil.shape[1]))
C = Perfil.shape[2]      # print ("Canais (channels): %d"%(Perfil.shape[2]))


for i in range(H, 0, -1):
        for j in range(L, 0, -1):
            print(ARM(i, j))






"""
print(arm(H, L))

print ("Cor do pixel em (%i, %i) - Vermelho: %d, Verde: %d, Azul: %d" % (i, j, r, g, b))

(b, g, r) = Perfil[305, 250]
print ("Cor do pixel em (250, 305) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))
 
(b, g, r) = Perfil[30, 250]
print ("Cor do pixel em (250, 30) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))
"""

import matplotlib
import matplotlib.pyplot as plt
#img=matplotlib.image.imread('./test.png')
#print img
import neurolab as nl
net = nl.load('autoencoder2_16_second_weights.txt')
img=list(map(lambda x:x*255,net.layers[0].np['w']))
img1=[img[i:i+2] for i in range(len(img)-2)]
img2=[img1[i:i+16] for i in range(len(img1)-16)]
print img
plt.imshow(img,cmap='gray',vmin=0,vmax=255)#,origin='lower')
plt.show()
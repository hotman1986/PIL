def imresize(im,sz):
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))


#cumulative distribution function,对直方图均衡化
def histeq(im,nbr_bins=256):
    imhist,bins = histogram(im.flatten(),nbr_bins,normed = True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf[-1] #归一化
    
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape),cdf
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def pca(X):
    num_data,dim = X.shape
    mean_X = X.mean(axis=0)
    X = X-mean_X
    if dim>num_data:
        M = np.dot(X,X.T)
        e,EV = linalg.eigh(M)
        tmp = np.dot(X.T,EV).T
        V = tmp[::-1]
        S = sqrt(e)[::-1]
        for i in range(V.shape[1]):
            V[:,i]/=S
    else:
        U,S,V=np.linalg.svd(X)
        V=V[:num_data]
    return V,S,mean_X

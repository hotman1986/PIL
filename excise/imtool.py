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

# coding=UTF-8
from skimage import transform,data
import skimage
#from readFile import images
import matplotlib.pyplot as plt

#resize the image
#param images[] size
def resize_image(images,size):
    newimages = [skimage.transform.resize(image, (size, size))
                for image in images]
    return newimages

#new = resize_image(images,16)


def example_resize():
    img = data.camera()
    dst=transform.resize(img, (80, 60))
    plt.figure('resize the image')

    plt.subplot(121)
    plt.title('before resize')
    plt.imshow(img,plt.cm.gray)

    plt.subplot(122)
    plt.title('after resize')
    plt.imshow(dst,plt.cm.gray)

    plt.show()

#example_resize()

# size大于1就是放大,小于1就是缩小
# rescale the image
# param image[] size
def rescale_image(imges,size):
    newimages = [skimage.transform.rescale(image, size)
                 for image in images]
    return newimages
    #print(img.shape)  # 图片原始大小
    #print(transform.rescale(img, 0.1).shape)  # 缩小为原来图片大小的0.1倍
    #print(transform.rescale(img, [0.5, 0.25]).shape)  # 缩小为原来图片行数一半，列数四分之一
    #print(transform.rescale(img, 2).shape)  # 放大为原来图片大小的2倍
#resize_image(images,2)

def example_rescale():
    img = data.camera()
    dst1=transform.rescale(img, 2)
    dst2 = transform.rescale(img, 0.5)
    dst3 = transform.rescale(img, [0.5, 0.75])
    plt.figure('rescale the image')

    plt.subplot(121)
    plt.title('before rescale')
    plt.imshow(img,plt.cm.gray)

    plt.subplot(122)
    plt.title('after resize')
    plt.imshow(dst1,plt.cm.gray)

    plt.show()

#example_rescale()


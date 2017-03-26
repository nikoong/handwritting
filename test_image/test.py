from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=0.2,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=False,
        fill_mode='nearest')

img = load_img('/home/nikoong/Algorithm_test/handwritting/test_image/test1_closed.jpg',grayscale=True)  # this is a PIL image

x = img_to_array(img) 

x = x.reshape((1,) + x.shape) 

i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='five', save_prefix='test', save_format='jpg'):
    i += 1
    if i >= 19:
        break  


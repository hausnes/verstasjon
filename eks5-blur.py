from PIL import Image, ImageDraw, ImageFilter

# Her legg me tekst over eit bilete
# For meir informasjon: https://www.tutorialspoint.com/python_pillow/python_pillow_writing_text_on_image.htm
innlastabilde = Image.open('bileter/ver-regn.png')
#innlastabilde.show()
tekstbilde = ImageDraw.Draw(innlastabilde)
tekstbilde.text((28,36), "Jo Bjornar Hausnes", fill=(255, 0, 0))
innlastabilde.save('bileter/temp.png')

# Her gjer me eit bilete uskarpt (blur). NB: Du kan velgje mellom ein rekke teknikkar og grader av blur.
# https://www.tutorialspoint.com/python_pillow/python_pillow_blur_an_image.htm
originaltBilete = Image.open('bileter/ver-regn.png')
originaltBilete.show()
# BoxBlur filter
boxImage = originaltBilete.filter(ImageFilter.BoxBlur(5))
boxImage.show()

#Save Boxblur image
boxImage.save('bileter/boxblur.jpg')

# No, kombiner desse to teknikkane! Blur eit bilete og legg tekst over resultatet.
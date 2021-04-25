from PIL import Image, ImageDraw, ImageFilter
innlastabilde = Image.open('bileter/ver-regn.png')
#innlastabilde.show()
tekstbilde = ImageDraw.Draw(innlastabilde)
tekstbilde.text((28,36), "Jo Bjornar Hausnes", fill=(255, 0, 0))
innlastabilde.save('bileter/temp.png')
import barcode
from barcode.writer import ImageWriter

ean = barcode.get('code128', code=';21=NZ5170?', writer=ImageWriter())
filename = ean.save('code128')
print(filename)

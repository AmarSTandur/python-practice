# import qrcode
# img = qrcode.make('https://youtu.be/PgWfHj3qsHA?si=Y7fqD7_RrZ_H3s2p ')
# type(img)  # qrcode.image.pil.PilImage
# img.save("amar.png")


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://youtu.be/PgWfHj3qsHA?si=Y7fqD7_RrZ_H3s2p')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
type(img)  # qrcode.image.pil.PilImage
img.save("amar123.png")
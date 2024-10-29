from PIL import Image
from lfsr import LFSR

class ImageEncrypter:
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.image = Image.open(file_name).convert('RGB')

    def open_image(self):
        return self.image.load()

    def pixelate(self):
        # Get the pixels from the image and store them in a 2D array
        pixels = self.open_image()
        pixel_array = []
        for i in range(self.image.size[0]):
            row = []
            for j in range(self.image.size[1]):
                pixel = pixels[i, j]
                row.append(pixel)
            pixel_array.append(row)
        return pixel_array

    def encrypt(self):
        pixel_array = self.pixelate()
        # Encrypt each pixel in the image using the LFSR object
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                pixel = pixel_array[i][j]
                random_value_red = self.lfsr.step()
                random_value_green = self.lfsr.step()
                random_value_blue = self.lfsr.step()
                new_red = pixel[0] ^ random_value_red
                new_green = pixel[1] ^ random_value_green
                new_blue = pixel[2] ^ random_value_blue
                pixel_array[i][j] = (new_red, new_green, new_blue)
        return pixel_array

    def save_image(self, file_name: str, encrypted: bool):
        if encrypted:
            pixel_array = self.encrypt()
        else:
            pixel_array = self.pixelate()
        # Create a new image from the pixel array and save it
        encrypted_image = Image.new('RGB', self.image.size)
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                encrypted_image.putpixel((i, j), pixel_array[i][j])
        encrypted_image.save(file_name)

def main():
    # Create LFSR object with seed "1001101010" and tap at position 5
    lfsr = LFSR('1001101010', 5)

    # Create ImageEncrypter object with the LFSR object and the file name of the image to encrypt
    encrypter = ImageEncrypter(lfsr, 'football.png')

    # Encrypt or decrypt the image based on the presence of the encrypted image file
    try:
        Image.open('football_encrypted.png')
        # Decrypt the image if it exists
        encrypter.save_image('football_decrypted.png', encrypted=True)
    except FileNotFoundError:
        # Otherwise, encrypt the image
        encrypter.save_image('football_encrypted.png', encrypted=False)

if __name__ == "__main__":
    main()
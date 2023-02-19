from PIL import Image
from pytesseract import pytesseract

img = Image.open("101.jpg")

pytesseract.tesseract_cmd = r'C:\Users\odemirelnt\AppData\Local\Tesseract-OCR\tesseract.exe'

myconfig = r"--psm 3 --oem 3"
text = pytesseract.image_to_string(img, lang="tur", config=myconfig)

def main():

    text = pytesseract.image_to_string(img, lang="tur", config=myconfig)

    file1 = open("101.txt", "a")
    file1.write(text)
    file1.write("------------\n")
    file1.close()

if __name__ == '__main__':
    main()


"""Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific."""

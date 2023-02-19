# Image Recognation From jpeg

It allows you to convert your jpeg information to txt file. After that, you can use regex to write as csv.

It is for turkish jpeg data, if you use your own language, you should change this code:

text = pytesseract.image_to_string(img, lang="tur", config=myconfig) --> 
text = pytesseract.image_to_string(img, lang="eng", config=myconfig)

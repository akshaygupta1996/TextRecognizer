# TextRecognizer

This is a python based project on handwritten text recognition.
I have used mainly 2 libraries:
1)OpenCV
2)Numpy

Input Will be an Image with handwritten text and output of will be the recognized text. its not 100% accurate but have positive results.
Concept of supervised machine learning is used. Firstly i have provided training data. 

Training data:
26 alphabets each written 10 times is provived as the training data

Path for training Data:


There are maily 2 python scripts , one to train the application and other to recognize new image.

1)imagetoarray.py
2)recognizeimage.py

The first script reads each dataset sequentially. Convert that image to 8*8 pixel, threshold the image. Then after converting that 
thresholded image into array it appends the array to the file(training file).
The image is converted into 3D RBG array matrix

Step By Step of SecondScript( recognizeimage.py)
1) Reads the image
2) Find blocks of text using OpenCV
3) Arrange the blocks in sequential manner with the help of [x ,y ,w, h] values
4) Crop each character from the image
5) Convert the image to 8*8 pixel
6) Threshold the image
    Two thresholding functions are used:
    1) Opencv Adaptive Threshold Algorithm
    2) An Algorithm is implemented that first calculates the mean of 
       all the pixel values in an image and then converts them accordingly.
       The image is converted in 2 pixel values only [0 0 0 ] and [255 255 255]
7) Convert the image to 3D RGB array
8) Predict the character using the training test file using an algorithm .

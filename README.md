# CV-recognition

Contents:

    Folder zoom:  Takes an  image.jpg and a template.jpg, that has to be part of the original image. 
    zoomGenerator take the original image, creates various copies of it zoomed in and out and stores them in the folder 
    zoomedImages,  with the zoom factor in the   name of the file : zoom{%of zoom}.jpg
    zoomRecognition reads all the images generated, takes the template , zooms it and matches it with the image.

    Folder symbols: From an image with various symobls on it, as well as 
    a file that contains images with each and every individual symbol, 
    distortedGenerator creates a variety of distorted images  
    symbolRecognition locates the individual symbols in the distorted images
    
    share.py: some functions and variables that are used by many scripts. 
    
    __pychace__: ignore
    
HOW TO USE:

    You only need to run the zoomRecognition.py & symbolRecodnition.py scripts in the appropriate folders
    the generators have been run. you may use them if you want to adjust zoom and distortion factors
    or if you want to test the code with your own images
    

# CV-recognition

gui.py :

        SUMMARY: this program take as input a large image, stored as "rescourses/plaketa.jpg", variable : imgFile  
        and a folder with a variety of templates ,"rescourses/templates", variable : templateFolder
        additionaly a frame is cut as a subimage of the original image.
        The user is promted the COMMANDS ,WASD to move , Z,X to zoom and Q to quit (capital or lowercase)
        If the frame is moved to a position that it contains one of the templates, it gets detected and marked with a 
        white rectangle. Aditionally, it is removed from the dict as it's possition is now known



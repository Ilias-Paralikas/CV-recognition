# CV-recognition


HOW TO USE:

        *)For simulation purposes you must place the images that is supposed to be the whole board in
        rescourses as : plaketa.jpg. Will not be present in the final project.
        
        1)Place the templates that you want to be located in rescourses/templates as: templateName.jpg .
        
        2)Also load them in rescourses/locationDict.pkl either manually as dictionary in pickle form
          or using the templateLocations.py script and following the instructions there
        
        WARNIGN, each template image must have a respective location in locationDict.
        
        3)Finally run gui.py to locate the templates and print the locations that were provided by the dict


                
CONTENTS:

        gui.py :

                SUMMARY: this program take as input a large image, stored as "rescourses/plaketa.jpg", variable : imgFile  
                and a folder with a variety of templates ,"rescourses/templates", variable : templateFolder
                additionaly a frame is cut as a subimage of the original image.
                The user is promted the COMMANDS ,WASD to move , Z,X to zoom and Q to quit (capital or lowercase)
                If the frame is moved to a position that it contains one of the templates, it gets detected and marked with a 
                white rectangle. Aditionally, it is removed from the dict as it's possition is now known


        templateLocations.py :

                This script is used to load the locations of the templates manually.
                Alternatively, it can be loaded in '/rescourses/locationDict' as a pkl file (pickle)

                ATTENTION!      for the template to be recognised, there must be a file with the same name as
                                the key given in the dict 


        rescourses : 

                templates :
                        
                        the templates that we want to detect and locate
                        NAMES MUST MATCH!

                locationDict.pkl :

                        a dictionary that matches the name of the template, when found , with the location in the board
                        NAMES MUST MATCH!

                plaketa.jpg : 
                
                        to be deleted in the final project, is here for visualization

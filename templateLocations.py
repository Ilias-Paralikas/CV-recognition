import pickle

# we want the instructions to be very clear, that's why we  insist in getting either 1 or 0
COMMAND = input(
    'type: \n1 if you want to replace excisting dict and \n0 if you want to keep the values(of the names that dont overlap)\n')
while COMMAND != '0' and COMMAND != '1':
    COMMAND = input(
        'type: \n1 if you want to replace excisting dict and \n0 if you want to keep the values(of the names that dont overlap)\n')

# the file that we want to store the dict and it's path
templateLocationDictFile = 'rescourses/locationDict.pkl'

if COMMAND == '1':
    # we want empty dict, so we initialize it
    templateLocationDict = {}
elif COMMAND == '0':
    # we want to keep the previous values so we read them from the file
    try:
        with open(templateLocationDictFile, 'rb') as file:
            templateLocationDict = pickle.load(file)

        # if it is not empty we want to display the current values
        if templateLocationDict:
            print('Current Values :')
            for key in templateLocationDict:
                print(key, ":", templateLocationDict[key])
        else:
            print('Dict is empty')

    except:
        print('Dict file does not excist, initialised to empty')
        templateLocationDict = {}


# we ask the user for the name and coordinates
print('Give New Values')
while input('press ENTER to continue, type anything else to stop :\n') == "":
    templateName = input('give the name of the template :\n')
    templateX = int(input('give the X location of the template :\n'))
    templateY = int(input('give the Y location of the template :\n'))

    templateLocationDict[templateName] = (templateX, templateY)

# if it not empty
if templateLocationDict:
    with open(templateLocationDictFile, 'wb') as file:
        pickle.dump(templateLocationDict, file, pickle.HIGHEST_PROTOCOL)
else:
    print('Given dict is empty')
    deleteDict = input(
        'are you sure you want to delete it?\n type :\n1 for yes \n,0 for no\n')
    if deleteDict == '1':
        with open(templateLocationDictFile, 'wb') as file:
            pickle.dump(templateLocationDict, file, pickle.HIGHEST_PROTOCOL)

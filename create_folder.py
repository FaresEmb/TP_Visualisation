import os


def create_folder(stations_names):
    path = os.getcwd()
    print ("The current working directory is %s" % path)
    
    path+="/stations"

    try:
        os.rmdir(path)
    except OSError:
        print ("Deletion of the directory %s failed" % path)
    else:
        print ("Successfully deleted the directory %s" % path)


    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)

    for name in stations_names:
        try:
            os.mkdir(path+"/"+name)
        except OSError:
            print ("Creation of the directory %s failed" % path+"/"+name)
        else:
            print ("Successfully created the directory %s " % path+"/"+name)
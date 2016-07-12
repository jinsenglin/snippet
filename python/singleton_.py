theone = None

def newTheOne():
    global theone
    if theone:
        raise Exception('theone already inited')
    print "initing theone"
    theone = 1
    return theone

newTheOne()
newTheOne()

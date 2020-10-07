def getHT(tag):
    topLocation = int(tag.find("top"))
    heightLocation = int(tag.find("height"))
    if topLocation and heightLocation: 
        top = tag[ topLocation + 5 : topLocation + 8 ]
        height = tag[ heightLocation + 8 : heightLocation + 11 ]
    else:
        return False
    if height[-1] == 'p':
        height =  tag[ heightLocation + 8 : heightLocation + 10]
    return (int(top), int(height))
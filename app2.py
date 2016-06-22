import cvfy

app = cvfy.register("gh:107.170.77.168:61369601:3000:8000")

@cvfy.crossdomain
@app.listen()
def getsizes():
    
    ## all data is received in sequence of listing in the input component
    ## all data is sent in sequence of listing in the output component
    
    ## receiving the data
    alltext = cvfy.getTextArray()
    allimages = cvfy.getImageArray()
    
    ## get size of both images
    size1 = str(len(allimages[0].read()))
    size2 = str(len(allimages[1].read()))
    
    ## sending back the data
    data1 = alltext[0] + ' ' + size1 + ' bytes'
    data2 = alltext[1] + ' ' + size2 + ' bytes'
    cvfy.sendTextArray([data1, data2])
    
    ## telling the APP server that request returned successfully -- important
    
    return 'OK'
    
## running the app
app.run()

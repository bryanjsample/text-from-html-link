import initialize
import createHtml

### MAKE SURE YOU HAVE SAVED THE CSV FILE INTO THE SAME FOLDER AS THIS FILE

### RUN TO WRITE MESSAGE !!! type FIRSTNAME for first name in message prompt. type LASTNAME for last name in message prompt.

def main():

    #establish source folder
    initVars = initialize.establish_src()
    src = initVars[0]
    csvFile = initVars[1]

    #create html file if it doesnt already exist
    createHtml.createTemplate(src)
        
    #add contents to html file
    createHtml.makeLinks(src, csvFile)

main()


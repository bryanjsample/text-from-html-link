
def src():
    ### PASTE THE FILE PATH OF THE FOLDER CONTAINING YOUR TARGET CSV FILE
    src = ''
    return src

def message(first, last):
    #initialize variable for new line (DO NOT EDIT)
    new = '%0a'


### WRITE OUT MESSAGE YOU WANT TO SEND
### TO WRITE FIRST NAME INSERT  {first}  
### TO WRITE LAST NAME INSERT  {last}
### AT THE VERY BEGINNING OF EACH NEW LINE INSERT  {new}  WITH NO SPACE AFTERWARDS

### !!! ENSURE THAT THERE ARE NO EXTRA SPACES IN YOUR MESSAGE !!! 

### EXAMPLE (disregard all hashes)
    
    ###Hey {first}, this is Bryan from BSU!
    ###{new}Thanks for touring campus! If you are ready to apply, you can follow the attached link to visit our application page.
    ###{new}If you have any questions dont hesitate to reach out!
    ###{new}https://www.bemidjistate.edu/admissions/apply/


    ### USER INPUT MESSAGE INTO THIS BLOCK
    message = f'''

Hey {first} {last}, this is Bryan from BSU!
{new}Thanks for touring campus! If you are ready to apply, you can follow the attached link to visit our application page.
{new}If you have any questions dont hesitate to reach out!
{new}https://www.bemidjistate.edu/admissions/apply/

'''

    return message

# README

---

## Setup Instructions

1. **Install Python 3.1.2.0**
- imports needed:
    1. csv
    2. os
    3. bs4

2. **Import Python files into a folder**
- **Store the folder in a safe location**
- **This is the folder you are always working with.**

#### At this point, you have completed general setup.

#### Proceed to [Initialize and Run Script](#initialize-and-run-script)

---

## Initialize and Run Script

>#### Important **Notes**
>##### Three hashes ( ### ) = Notation that is important to user
>##### One hash ( # ) = Notation about underling script (unimportant to user)
>##### If the profile does not have any phone number associated it will not have any links

### 1. Ensure that folder exists containing the following files
- `README.html`
- `EDITME.py`
- `createHtml.py`
- `mainScript.py`

### 2. Create a seperate folder for your specific task (SOURCE FOLDER)
- Example : `/Documents/Dec 20 Texts`

### 3. Extract target spreadsheet from Hobson's
1. **First Column : Last Name**
2. **Second Column : First Name**
3. **Third Column : Phone Number (no formatting)**
4. **Fourth Column: Mobile Number (no formatting)**
> Any subsequent columns will not affect the outcome
> **!! Ensure that the first four columns are correct !!**

### 4. Export spreadsheet as CSV file
- **!!! SAVE CSV FILE INSIDE OF YOUR SOURCE FOLDER !!!**

### 5. Initialize variables and prepare to run
1. **Open `EDITME.py`**
    1. **Edit line 4 defining src**
        1. Paste path to taget folder inside of single quotes
            - `src = **'PASTE FILE PATH HERE'**`
            - should look similar to
                - `src = '/C:/User/Documents/Dec 20 Texts'`
    2. **Read lines 12-24 for information on how to format text prompt**
        - If you want to add emojis: it will be easier to add manually after clicking link
    3. **Edit text block beginning on line 30**
        1. This is where you enter your message prompt
            - First Name = {first}
            - Last Name = {last}
            - New Line = {new}
    4. **!! Save file in .py (python3) formatting and close !!**
2. **Execute `mainScript.py`**

### 6. Obtain HTML file
- Navigate to your source folder inside of your file explorer
- You should see a file titled `texting_list.html`

### 7. Email / transfer HTML file
- You can email the html file to yourself in order to access on your phone
1. **Save the file onto your phone inside of "On This iPhone"**

### 8. Open files app on your phone
1. Navigate to `On This iPhone`
2. Select `texting_list.html`
    - HTML viewer should open, allowing you to click links and select boxes
#### OR to use searchbar
1. Navigate to `On This iPhone`
2. Long press `texting_list.html`
   1. Open in Microsoft Edge
### 9. Send text messages
- Each link inside of the HTML file will automatically:
    1. Open messages
    2. Autopopulate phone number
    3. Autopopulate message field
1. **Select link you would like to send**
2. **Confirm send through notifications app**
3. **Recent apps > HTML file**
4. **Check box to confirm message sent**
5. **Select next link**

---

### Footnotes
##### Any profiles that do not have an associated phone number will be printed in the console
##### To search for a number within the HTML file : Enter the number into search bar and press search button
##### If page is refreshed or files app is closed : Checkboxes will reset to empty

---





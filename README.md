
# README

---

## Setup Instructions

1. **Install Python 3.1.2.0**
- imports needed:
    1. csv
    2. os
    3. bs4

2. **Import Python files into a folder.**
- **Store the folder in a safe location.**
- **This is the folder you are always working with.**

#### At this point, you have completed general setup.

#### Proceed to [Initialize and Run Script](#initialize-and-run-script)

---

## Initialize and Run Script

>##### NOTE: If the profile does not have any phone number associated it will not have any links.

### 1. Ensure that folder exists containing the following files:

- `createHtml.py`
- `initialize.py`
- `mainScript.py`

#### ***THIS IS YOUR SOURCE (SRC) FOLDER***

### 2. Extract target spreadsheet from Hobson's
1. **First Column : Last Name**
2. **Second Column : First Name**
3. **Third Column : Phone Number (no formatting)**
4. **Fourth Column: Mobile Number (no formatting)**
> Any subsequent columns will not affect the outcome.
> **!! Ensure that the first four columns are correct !!**

### 3. Export spreadsheet as CSV file
- **!!! SAVE CSV FILE INSIDE OF YOUR *SOURCE FOLDER* !!!**

### 4. Run `mainScript.py`

1. You will be prompted to enter your message.
2. Enter your message, hitting enter each time you want to insert a line break.
    - To represent a first name, type `FIRSTNAME`
    - To represent a last name, type `LASTNAME`
3. After hitting enter, you will be asked if the message segment looks correct.
   1. If no, you will re-write that line.
   2. If yes, continue.
4. You will be asked if you are finished with your message.
   1. If no, you will continue writing the next line of your message.
   2. If yes, continue.
5. You will be asked once again if your message looks correct.
   1. If no, repeat steps 1-4.
   2. If yes, program will proceed.
   
>The program will check to see if **FIRSTNAME** or **LASTNAME** is present in your message.
>If one or both is missing, you will be prompted to ensure that it was intentional.
>- If no, repeat steps 1-5.
>- If yes, program will proceed.

### 5. Obtain HTML file
- Navigate to your source folder inside of your file explorer
- A new folder named `year-month-day_X` will be present
  - `X` = number of folder being made (will automatically increase)
- Inside of new folder, you will find your CSV file, and also **an HTML file named *`text_list.html`***

### 6. Email / transfer HTML file
- You can email the html file to yourself in order to access on your phone
1. **Save the file onto your phone inside of "On This iPhone"**

### 7. Open files app on your phone
1. Navigate to `On This iPhone`
2. Select `text_list.html`
    - HTML viewer should open, allowing you to click links and select boxes
#### OR to use searchbar
1. Navigate to `On This iPhone`
2. Long press `text_list.html`
   1. Open in Microsoft Edge
### 8. Send text messages
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





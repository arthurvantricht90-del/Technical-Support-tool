# Technical-Support-tool
This repository contains code for a Python tool created to increase efficiency as a Technical Support Officer


## To run the tool:
- Download the main zip file. This should contain:
  - main.py (the main code - run from here)
  - mail_library.py (pieces of text that are assembled into complete e-mails in the main code)
  - HNI_database.json file (database containing MCC and MNC codes of mobile network operators worldwide (see https://mcc-mnc.com/)
- Make sure the working directory is that directory which contains all three files mentioned above.



## Goal of the tool:
- This tool was created to increase efficiency in ticket managament for my Technical Support Officer job.
- It takes input (like phone number, port date, ICCID, etc.), and assembles the values into a neat, standardized format ready to used as a ticket observation.
- In doing so, repetitive actions are reduced and efficiency is increased while maintaining cleanliness.



# Manual for tool usage:
### MAIN OBSERVATION TAB
- Affected phone number is automatically formatted into 04xx xx xx xx format in the output.
- Port Done Date becomes 'Joined' of the tool recognizes a native phone number.
- 'Connected To' field expects input in VPLMN id format like '02F610'. From this VPLMN id, the corresponding mobile network operator is looked for in the HNI database and printed in the output.

- The Tab key or Enter key go to next field.
- Press cntrl + z/y to go previous or next.
- The text field in the bottom is meant for additional information. Can be zoomed in and out.

- Select 'Generate Observation' to generate the observation. It's automatically copied to clipboard.
- 'Clear Fields' clears all fields.
  

### FAILED CALL OBSERVATION TAB
- Failed call observation generator for Homer call traces
- A number and B number automatically outputs number in the +32x xx xx xx xx format.
- 'Generate Observation' generates the observation and copies to clipboard.

### MAIL TEMPLATE SELECTOR
- 'Open Mail Template Selector' opens a new window in which a mail is assembled depending on selected dropdown options.
- If Affected phone number is filled in in MAIN OBSERVATION TAB, 'Mobile' is selected in the first dropdown.
- If Phone Model is filled in, 'Android' or 'iPhone' is automatically filled in.
- 'Copy Template' copies assembled mail onto clipboard.
- Notification Message is automatically generated in the same language as selected in the Mail Language. 

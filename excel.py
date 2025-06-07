import pandas as pd

File_path = input("Enter your excel file path: ")
Dataframe = pd.read_excel(rf"{File_path}")

#Creating copy of main dataframe to do changes
new_copy = Dataframe.copy()


Emails_col = ""
DF_Columns = Dataframe.columns

#Checking the name of column which contains email address
for column in DF_Columns:
    if "Email" or "email" in column:
        Emails_col = column

#Creating empty lists to store data which we want in new excel file
NAME = []
NAME_STRING_LENGTH = []
EMAILS = []

#Getting emails from the main file into a list
emails = [email for email in Dataframe[Emails_col]]

#Spliting emails to get user first name
for email in emails:
    if email.count(".") > 1 and "@" in email:
        split_email = email.split(".")
    else:
        split_email = email.split("@")
    NAME.append(split_email[0])

#Sorting user names as per length of their name
NAME.sort(key=len, reverse=True)

#Creating a list in which email address are of same user as per index
for name in NAME:
    for i in range(0, len(emails)):
        if name in emails[i]:
            EMAILS.append(emails[i])

#Creating new list to remove duplicates
NEW_EMAILS = []
[NEW_EMAILS.append(x) for x in EMAILS if x not in NEW_EMAILS]

#Adding two list in another list
new_excel = [NAME, NEW_EMAILS]

#Removing old columns and rows and creating new
new_copy = new_copy.drop(new_copy.columns, axis=1)
new_copy["Name"] = new_excel[0]
new_copy[Emails_col] = new_excel[1]

#At last creating a new excel file
new_copy.to_excel("emails.xlsx")

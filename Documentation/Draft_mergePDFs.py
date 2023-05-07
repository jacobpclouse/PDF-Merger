# This Python Program was written on Linux Mint using VScode, your milage may vary on OS and configuration.

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import os # used to create folder and traverse directory paths and the files within
from PyPDF2 import PdfReader, PdfMerger # used to merge PDFs
# Read more about the functionality of PyPDF2 at: https://pypi.org/project/PyPDF2/

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to print out my Logo ---
def myLogo():
    print("Created and Tested by: ")
    print("   __                  _         ___ _                       ")
    print("   \ \  __ _  ___ ___ | |__     / __\ | ___  _   _ ___  ___  ")
    print("    \ \/ _` |/ __/ _ \| '_ \   / /  | |/ _ \| | | / __|/ _ \ ")
    print(" /\_/ / (_| | (_| (_) | |_) | / /___| | (_) | |_| \__ \  __/ ")
    print(" \___/ \__,_|\___\___/|_.__/  \____/|_|\___/ \__,_|___/\___| ")
    print("Dedicated to Peter Zlomek and Harely Alderson III")


# --- Function to Merge Full PDFs in any order ---
def generalMerge():
    print("General Merge")
    print("All files in a folder will be combine in numbers/alphabetical order")
    pathToFolder = input("Please specifiy the path to the folder containing the PDFs that you would like to merge: ")
    outputPDFName = input("What do you want the output to be named?: ")
    print("\n")

    # opening up folder and looping through pdfs
    merger = PdfMerger()    
    for filename in os.listdir(pathToFolder):
        print(f"Selected Filename: {filename}")
        # merger.append(f"{pathToFolder}/{filename}") # this may need to be changed in case of windows vs linux
        filepath = os.path.join(pathToFolder, filename)
        print(f"FilePath: {filepath}")
        merger.append(filepath)
        print("\n\n")
    merger.write(f"{outputPDFName}.pdf")
    merger.close()
    print("\n\n")
    myLogo()


# --- Function to Merge Full PDFs in a specified order dictated by the user ---
def selectiveMerge():
    print("Selective Merge")
    print("User will determine how many documents they want to merge manually")
    # pdfsToMergeArray = []
    pathToFolder = input("Please specifiy the path to the folder containing the PDFs that you would like to merge: ")
    outputPDFName = input("What do you want the output to be named?: ")
    numberOfFilesToMerge = int(input("How many items do you want to merge?: "))

    print("\n")

    # Querying User for Order
    merger = PdfMerger() 
    starterVal = 1
    while starterVal <= numberOfFilesToMerge:
        print(f"Starter Value: {starterVal} of Total Files: {numberOfFilesToMerge}")
        filename = input(f"What is the file you want to add in the {starterVal} spot?: ")
        print('\n')

        # Below allows for files in different directories to be addeded to the output
        isSamePath = input(f"Is the path to this file: {pathToFolder}? (YES or NO) ")
        if isSamePath.upper() == 'YES':
            print("Same path")
            filepath = os.path.join(pathToFolder, filename)
        else:
            sepPath = input("What is the path to this file?: ")
            filepath = os.path.join(sepPath, filename)
        print(filepath)
        
        merger.append(filepath)
        print("\n")
        starterVal += 1


    # opening up folder and looping through pdfs
    merger.write(f"{outputPDFName}.pdf")
    merger.close()
    print("\n\n")
    myLogo()  


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
chooseMerge = input("What kind of merge do you want: GENERAL or SELECTIVE? ")
print(chooseMerge.upper())
print('\n')

# Catch statement to prevent invalid selections
while chooseMerge == '':
    chooseMerge = input("Can't be left blank, please input either GENERAL or SELECTIVE: ")

# execute general merge
if chooseMerge.upper() == 'GENERAL':
    generalMerge()

# execute selective merge
elif chooseMerge.upper() == 'SELECTIVE':
    selectiveMerge()

# if nonsense, end the script
else:
    print("Response Not Recognized, Ending Program...")

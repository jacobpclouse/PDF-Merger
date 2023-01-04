# This Python Program was written on Linux Mint using VScode, your milage may vary on OS and configuration.

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import os # used to create folder and traverse directory paths and the files within
# import PyPDF2 # used to merge PDFs
from PyPDF2 import PdfReader, PdfMerger

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Variables
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


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
    pathToFolder = input("Please specifiy the path to the folder containing the PDFs that you would like to merge: ")
    outputPDFName = input("What do you want the output to be named?: ")
    print("\n")

    # opening up folder and looping through images
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

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
generalMerge()
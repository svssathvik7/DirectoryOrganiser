import os   #to deal with the directories
import shutil   #dealing with files
import json     #dealing with dictionary loading from files
import sys      #exiting the program
directory_path = input("Enter directory path : ")
def get_files_in_directory(directory_path):
    return os.listdir(directory_path)

#class to deal with the menu
class Menu:
    preferences = dict() #has the extensions & folders
    def __init__(self):
        f = open("data.txt","r")
        data = f.read()
        Menu.preferences = json.loads(data)
        Menu.displayMenu()
        
    def displayMenu():  #displays the menu
        print("Hello! Glad you are here to organise your files : ")
        print("Enter 1 : Get the current preferences")
        print("Enter 2 : Set new preferences")
        print("Enter 3 : Organise a directory")
        print("Enter 4 : EXIT")
        print("Enter 5 : Credits/Feedback")
        try:
            user_inp = int(input())
        except:
            print("Enter valid option")
        if(user_inp == 1):
            Menu.printPreferences()
            Menu.displayMenu()
        elif(user_inp == 2):
            Menu.setPreferences()
        elif(user_inp == 3):
            Menu.organiseFolder()
        elif(user_inp == 4):
            sys.exit()
        elif(user_inp == 5):
            Menu.showCredits()
            
    def organiseFolder():   #groups extensions into folders
        ob1 = Directory(flist)
        Menu.displayMenu()
        
    def printPreferences(): #prints the already saved preferences
        print('\n'.join([f'{key} --> {value}' for key, value in Menu.preferences.items()]))
        
    def setPreferences():   #change the preference dictionary
        print("Do you want to add(A) preference or delete(D) preference? ")
        try:
            user_inp = input().lower()
            if user_inp == 'a':
                Menu.addPreference()
            elif user_inp == 'd':
                Menu.delPreference()
            Menu.displayMenu()
        except:
            print("Enter valid details")
            Menu.setPreferences()
            
    def addPreference():    #adds a new preference
        try:
            user_inp_key, user_inp_value = input("Enter the extension(.extn) Foldername(Fldr)").split()
            pref = Menu.getPreferences()
            pref[user_inp_key] = user_inp_value
            Menu.preferences = pref
            Menu.displayMenu()
        except:
            print("Enter valid pair of values separated by space")
            Menu.addPreference()
            
    def delPreference():    #deletes existing preference
        try:
            Menu.printPreferences()
            print("Enter the extension type you want to delete or (A)to delete all : ")
            user_inp = input()
            pref = Menu.getPreferences()
            if user_inp == 'A' or user_inp == 'a':
                f = open("data.txt","w")
                f.write(json.dumps({}))
            else:
                del pref[user_inp]
            Menu.displayMenu()
        except:
            print("Enter valid extension type")
            Menu.delPreference()
    def showCredits():
        os.system("cls" if os.name=='nt' else "clear")
        print("Developed by SVS SATHVIK")
        print("Contact mail = sathvikworkmail@gmail.com")
        print("Languages : Python3")
        print("Modules : os, shutil, json, sys")
        print("Developed using VSCode")
        print(end="\n\n")
        Menu.displayMenu()
    @staticmethod
    def getPreferences():
        return Menu.preferences
    
#class to deal/organise the directory
class Directory:
    def __init__(self,flist):
        self.Flist = flist
        self.sortOut()
    def sortOut(self):
        preferences = Menu.getPreferences() #static method of Menu
        for i in preferences.values():
            if os.path.exists(i):
                continue
            else:
                os.mkdir(os.path.join(i))   #created subfolders
        for i in (preferences):
            for j in self.Flist:
                if j.endswith(i):   #checks for preferred extensions
                    src_path = os.path.join(j)
                    dest_path = os.path.join(preferences[i],j)
                    shutil.move(src_path,dest_path)
                else:
                    pass
flist = get_files_in_directory(directory_path)
menu_object = Menu()
director_object = Directory(flist)
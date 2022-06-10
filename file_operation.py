import os
print(os.getcwd())
os.chdir("C:\\Users\\sai ganesh\\Documents\\final project GANESH")
print(os.getcwd())
inp1=input("Enter the string that to be updated in orginal file: ")
replace_stri=input("Enter the word that needs to be replaced: ")
for i in os.listdir():
    if i.split(".")[-1]=='txt' and i.split(".")[0]=='example':
        with open(i,'r+') as f:
            new_f=f.readlines()
            f.seek(0)
            for text in new_f:
                if replace_stri in text:
                    fin=text.replace(replace_stri,inp1)
                    f.write(fin)
                else:
                    pass
            f.truncate()
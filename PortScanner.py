
import os
banner = """

$$$$$$$$\  $$$$$$\  $$\      $$\       $$$$$$$\                       $$\            $$$$$$\                                                             
\__$$  __|$$  __$$\ $$ | $\  $$ |      $$  __$$\                      $$ |          $$  __$$\                                                            
   $$ |   $$ /  \__|$$ |$$$\ $$ |      $$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\         $$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
   $$ |   $$ |      $$ $$ $$\$$ |      $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        \$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
   $$ |   $$ |      $$$$  _$$$$ |      $$  ____/ $$ /  $$ |$$ |  \__| $$ |           \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
   $$ |   $$ |  $$\ $$$  / \$$$ |      $$ |      $$ |  $$ |$$ |       $$ |$$\       $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
   $$ |   \$$$$$$  |$$  /   \$$ |      $$ |      \$$$$$$  |$$ |       \$$$$  |      \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
   \__|    \______/ \__/     \__|      \__|       \______/ \__|        \____/        \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|      
                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                        
                                                                                                                                                 
                                                                                                                                                 
"""
print(banner)
print("Normal port taramas?? i??in 1")
print("Servis Taramas?? i??in 2")
print("A????k taramas?? i??in 3")
s = input("Se??enek : ")
if s == "1":
    i = input("Hedef ip adresini girin : ")
    os.system("nmap -Pn --open "+i)
if s == "2":
    b = input("Hedef ip adresini girin : ")
    os.system("nmap -Pn -sV "+b)
if s == "3":
    d = input("Hedef ip adresini girin : ")
    os.system("nmap -Pn -sC "+d)

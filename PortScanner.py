
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
print("Normal port taraması için 1")
print("Servis Taraması için 2")
print("Açık taraması için 3")
s = input("Seçenek : ")
if s == "1":
    i = input("Hedef ip adresini girin : ")
    os.system("nmap --open "+i)
if s == "2":
    b = input("Hedef ip adresini girin : ")
    os.system("nmap -sV "+b)
if s == "3":
    d = input("Hedef ip adresini girin : ")
    os.system("nmap -sC "+d)

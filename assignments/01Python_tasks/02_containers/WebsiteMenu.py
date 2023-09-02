##########################################################################################
#                                                                                        #
# File: WebsiteMenu.py                                                                   #
# Author: Mohamed Samy Ahmed                                                             #
# Date: August 8, 2023                                                                   #
#                                                                                        #
# Description:                                                                           #
#    Provide a brief description of the purpose and functionality of the Python file.    #
#                                                                                        #
##########################################################################################

import webbrowser

Websites ={
    "Facebook":'https://www.facebook.com/',
    "Netflix":'https://Netflix.com/',
    "Youtube":'https://www.youtube.com/'
}
print(Websites.keys())
x=input("Choose a website :  ")
if x in Websites.keys() :
    webbrowser.get('windows-default').open_new_tab(Websites[x])
else :
    print(" not in the list of favourites")
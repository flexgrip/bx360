#!/usr/bin/python

########################################################
#|                xbmc import stuff                   |#
#| I was told to put this here from the               |#
#| "how-to: xbmc scripts" wiki page and I don't       |#
#| really know why. Maybe I should read more about    |#
#| python and default xbmc functions.                 |#
########################################################

import xbmc, xbmcgui
import os, sys, thread, stat, time, string

########################################################

ver = "0.1a"
created_on = '10-17-2009'
scriptname = "bx360"
xbmc.output('--- ' + scriptname + "v" + ver + " Date: " + created_on + ' ---\n')

language = xbmc.getLanguage()
print 'Language chosen by xbmc: ' + language 

xbmc.Language.__init__(os.getcwd(), xbmc.getLanguage())

#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!                                                   !#
#!                CONFIGURE THESE                    !#


ws_port = '9999'              #xbmc web server port. !#
ws_host = 'localhost'         #xbmc web server host  !#


#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!        Comine the two      #!#!#!#!#!#!#!#!#

webserver = ws_host + ':' + ws_port

#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#

########################################################
#|           GLOBAL VARIABLES CAN GO HERE             |#
#|                                                    |#
#| This one isn't being used because it errors and I  |#
#| suck at python so I don't know why. It said        |#
#| something about it not being defined but it was so |#
#| fuck that. Anyway it just set a default which I    |#
#| did manually. Oh well, you will know where to set  |#
#| your default if you search for it below.           |#
#|                                                    |#
#| wdrive = '/dev/dvd'                                |#
#|                                                    |#
########################################################
game_iso = 'will get changed'
is_linux = False
is_windows = False
burning = False

### I read that I need this to import other python libs
### so I will leave it here.
###
### BASE_RESOURCE_PATH = os.path.join( os.getcwd().replace( ";", "" ), "resources" )
### sys.path.append( os.path.join( BASE_RESOURCE_PATH, "lib" ) )
### subclassing getLocalizedString

words = xbmc.Language(os.getcwd()).getLocalizedString


#######################################################





########################################################
#|                      burnit()                      |#
#| This builds the burn command. The only reason this |#
#| is here is so that later I can add different ways  |#
#| to burn the images on different operating systems  |#
#|                                                    |#
########################################################

def burnit():

# Choose drive to write to

    kb = xbmc.Keyboard('default', 'heading', True)
    kb.setDefault("/dev/dvd")
    kb.setHeading(words(00002))
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        drive = kb.getText().replace(' ', '\ ')
    else:
        return(1)

# Choose your image

    dialog = xbmcgui.Dialog()   
    the_iso = dialog.browse(1,words(00003), 'files', '.iso|.bin|.img|.000', True, False,)
    if (the_iso != ''):  
        game_iso = the_iso.replace(' ', '\ ')
    else: 
        return(1)
    print 'Image chosen: ' + game_iso

# Choose your speed

    kb = xbmc.Keyboard('default', 'heading', True)
    kb.setDefault("2")
    kb.setHeading(words(00004))
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        speed = kb.getText().replace(' ', '\ ')
    else:
        return(1)

#makes the command from
#growisofs -use-the-force-luke=dao -use-the-force-luke=break:1913760
#-dvd-compat -speed=2 -Z /dev/hda=IMAGE.000

    if (is_linux):
       #command = 'cat /dev/urandom > ~/out.file'
       #command = 'growisofs -dry-run -use-the-force-luke=dao -use-the-force-luke=break:1913760  -dvd-compat -speed=' + speed + ' -Z ' + drive + '=' + game_iso
        command = 'sh ' + os.getcwd().replace(' ', '\ ') + '/bx360.sh ' + drive + ' ' + game_iso + ' ' + speed + ' ' + os.getcwd().replace(' ', '\ ') + '/resources/icons/xboxlogo.png ' + webserver                        
    if (is_windows):
        command = 'some windows cmd'


# Are you sure?

    if are_you_sure(command):
       print 'burn approved'
       run_it(command);
    else: 
        print 'burn cancelled'
        cancel()
        return (1) 
    return (0)

########################################################





########################################################
#|                     opening_act()                    |#
#| Gateway to the west.                               |#
#|                                                    |#
#|                                                    |#
########################################################
class opening_act(xbmcgui.Window):
      def __init__(self):

       exit_script = True 
       while (exit_script): 
             dialog = xbmcgui.Dialog()
             choice  = dialog.select(words(00001) , [ words(00005), words(00006)])

             if (choice == 0):
                 print 'User chose to burn a backup'
                 burnit()

             if (choice == 1):
                 print 'Goodbye bx360'
                 exit_script = False

       self.close()
#######################################################



########################################################
#|                      run_it()                      |#
#| Runs the command passed to it.                     |#
#|                                                    |#
#|                                                    |#
########################################################
def run_it(command):

    if (is_linux): 
        command = command + ''
        sys.platform.startswith('linux')
        status = os.system("%s" % (command))
        print 'Here is what actually ran:' + command    
        time.sleep(1)
        it_worked()


#    if (is_windows):

              
    return 0
#######################################################



########################################################
#|                   it_worked()                      |#
#| Should report from bash that the burn completed.   |#
#|                                                    |#
#|                                                    |#
########################################################
def it_worked():
    dialog = xbmcgui.Dialog()
    title = words(10008)
    selected = dialog.ok(title,words(10009))
    burning = True
    return 0
#######################################################



########################################################
#|                      failed()                      |#
#| Not implemented yet but will report if something   |#
#| fails in the script.                               |#
#|                                                    |#
########################################################
def failure():
    dialog = xbmcgui.Dialog()
    title = words(10010)
    selected = dialog.ok(title,'some variable showing the problem should go here\n')
    return 0
#######################################################



########################################################
#|                      cancel()                      |#
#| Cancels the current action.                        |#
#|                                                    |#
#|                                                    |#
########################################################
def cancel():
    dialog = xbmcgui.Dialog()
    title = words(00007)
    selected = dialog.ok(title,words(10011))
    return 0
#######################################################



########################################################
#|                  are_you_sure()                    |#
#| Asks the user if they are sure about something.    |#
#|                                                    |#
#|                                                    |#
########################################################
def are_you_sure(command):
    dialog = xbmcgui.Dialog()
    title = words(10012)
    message = "\n\n\n" + words(10014) + "\n" + words(10013) + "\n"  + command + "\n"
    selected = dialog.yesno(title, message)
    return selected
#######################################################



########################################################
#|                   wrong_os()                       |#
#| Notifies the user if he/she are not in linux.      |#
#|                                                    |#
#|                                                    |#
#############|   WILL END THE SCRIPT   |################
def wrong_os():
    dialog = xbmcgui.Dialog()
    title = words(10019)
    selected = dialog.ok(title, words(10020))
    return 0
#######################################################


################|Not in use for v0.1a|##################
#| this is the start of daves idea to check if a burn |#
#| process has been started and if it has, show the   |#
#| progress bar for it. i guess people that want to   |#
#| burn multiple games at once are S.O.L :)           |#
#############|   WILL END THE SCRIPT   |################


def check_for_process():
    dialog = xbmcgui.Dialog()
    title = words(10021)
    selected = dialog.ok(title,'')
    return 0
#######################################################



 ######################################################
#|                   -= MAIN =-                       |#
#| This is the standard main with an OS if statement. |#
#|                                                    |#
#|                                                    |#
 ######################################################
if __name__ == '__main__':

# checks the operating system -- (pulled from another script)
   operating_system = os.name

   if  (operating_system == 'nt'):
        is_windows = True
        drive = 'Would need to change \n'

   else: 
        system = os.uname()
        if system[0] == 'Linux': 
           is_linux = True 
           print 'Discovered a white operating system \n'

   if (is_linux or is_windows):

        mydisplay = opening_act() 
        del mydisplay

# tell them to get a real os
   else:
        print 'This script only runs on linux and needs growisofs \n'
        print 'Support for your OS might be available. Check some \nlink to find out more.'
        wrong_os()
 
#######################################################

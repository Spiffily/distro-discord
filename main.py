#!/bin/env python3
from pypresence import Presence # The simple rich presence client in pypresence
import os
from os.path import expanduser
home = expanduser("~")
path = os.getcwd()
import subprocess
from subprocess import *
from io import StringIO
import sys
import time

# icons=home+"/.local/share/distro-discord/icons"
icons="icons"
# run("mkdir "+icons, shell=True)

distroicon = "tux"
distro=run("neofetch distro", shell=True, stdout=PIPE)
distro=str(distro.stdout).lower()
if distro.count("pop!_os") > 0:
    distro="POP!_os"
    distroicon = "pop_os"
    client_id = "763929857649410070"
elif distro.count("xubuntu") > 0:
    distro="Xubuntu"
    distroicon = "xubuntu"
    client_id = "763930869911257129"
elif distro.count("ubuntu-mate") > 0:
    distro="Ubuntu Mate"
    distroicon = "ubuntu-mate"
    client_id = "763930983288275035"
elif distro.count("ubuntu-cinnamon") > 0:
    distro="Ubuntu Cinnamon"
    distroicon = "ubuntu-cinnamon"
    client_id = "763931239353942027"
elif distro.count("kubuntu") > 0:
    distro="Kubuntu"
    distroicon = "kubuntu"
    client_id = "763931360787955713"
elif distro.count("ubuntu") > 0:
    distro="Ubuntu"
    distroicon = "ubuntu"
    client_id = "763930415454486568"
elif distro.count("gallium") > 0:
    distro="Gallium OS"
    distroicon = "gallium"
    client_id = "763931542371827722"
elif distro.count("arch") > 0:
    distro="Arch Linux"
    distroicon = "arch"
    client_id = "763930319686205460"
elif distro.count("gentoo") > 0:
    distro="Gentoo"
    distroicon = "gentoo"
    client_id = "763805674240081960" #
elif distro.count("mint") > 0:
    distro="Linux Mint"
    distroicon = "linux-mint"
    client_id = "763931771233370133"
elif distro.count("fedora") > 0:
    distro="Fedora"
    distroicon = "fedora"
    client_id = "763931948040060958"
elif distro.count("neon") > 0:
    distro="KDE Neon"
    distroicon = "neon"
    client_id = "763805674240081960" #
elif distro.count("parrot") > 0:
    distro="Parrot OS"
    distroicon = "parrot"
    client_id = "763805674240081960" #
elif distro.count("red") > 0:
    distro="Red Hat"
    distroicon = "redhat"
    client_id = "763805674240081960" #
else:
    distro="Linux"
    distroicon = "tux"
    client_id = "763805674240081960"

deicon = "sh"
de=run("neofetch de", shell=True, stdout=PIPE)
de=str(de.stdout).lower()
if de.count("gnome") > 0:
    de="GNOME"
    deicon = "gnome"
elif de.count("xfce") > 0:
    de="XFCE"
    deicon = "xfce"
elif de.count("cinnamon") > 0:
    de="Cinnamon"
    deicon = "cinnamon"
elif de.count("mate") > 0:
    de="MATE"
    deicon = "mate"
elif de.count("budgie") > 0:
    de="Budgie"
    deicon = "budgie"
elif (de.count("kde") > 0) or (de.count("plasma") > 0):
    de="KDE Plasma"
    deicon = "plasma"
elif de.count("lxde") > 0:
    de="LxDE"
    deicon = "lxde"
elif de.count("lxqt") > 0:
    de="LxQt"
    deicon = "lxde"
elif de.count("i3") > 0:
    de="i3"
    deicon = "bash"
elif de.count("unity") > 0:
    de="Unity"
    deicon = "unity"
else:
    de="bash"
    deicon = "bash"

uptime = ":)"
uptime = run("neofetch uptime", shell=True, stdout=PIPE)
uptime = str(uptime.stdout)
uptime = uptime.split(": ", 1)[1]
uptime = uptime.split(" \\", 1)[0]

display_session = "xorg"
display_session = run("echo $XDG_SESSION_TYPE", shell=True, stdout=PIPE)
display_session = str(display_session.stdout)
display_session = display_session.split("'", 1)[1]
display_session = display_session.split("\\", 1)[0]
print("Display session: "+display_session)

window_manager = "lightdm"
window_manager = run("neofetch wm", shell=True, stdout=PIPE)
window_manager = str(window_manager.stdout)
window_manager = window_manager.split(": ", 1)[1]
window_manager = window_manager.split(" ", 1)[0]
print("Window Manager: "+window_manager)

gtk = "Adwaita"
gtk = run("neofetch theme", shell=True, stdout=PIPE)
gtk = str(gtk.stdout)
gtk = gtk.split(": ", 1)[1]
gtk = gtk.split(" [", 1)[0]
print("Gtk theme: "+gtk)

if de == "GNOME":
    try:
        shelltheme = "Default"
        shelltheme = run("gsettings get org.gnome.shell.extensions.user-theme name", shell=True, stdout=PIPE)
        shelltheme = str(shelltheme.stdout)
        shelltheme = shelltheme.split("'", 1)[1]
        shelltheme = shelltheme.split("'", 1)[0]
        print("Shell theme: "+shelltheme)
    except:
        shelltheme = "Default"

icons = "Adwaita"
icons = run("neofetch icons", shell=True, stdout=PIPE)
icons = str(icons.stdout)
icons = icons.split(": ", 1)[1]
icons = icons.split(" [", 1)[0]
print("Icon theme: "+icons)

bigicon = distroicon
smallicon = deicon
# print("Big icon: "+bigicon)
# print("Small icon: "+smallicon)
if(de == "GNOME"):
    themetooltip = "Theme: "+gtk+"    Shell: "+shelltheme+"      Icons: "+icons
else:
    themetooltip = "Theme: "+gtk+"      Icons: "+icons
disptooltip = "Display server: "+display_session+"   Window Manager: "+window_manager #Display tooltip

# INIT
# client_id = "763805674240081960"  # Put your Client ID in here
print("Distro: "+distro)
print("DE: "+de)

RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop

while True:  # The presence will stay on as long as the program is running
    uptime = run("neofetch uptime", shell=True, stdout=PIPE)
    uptime = str(uptime.stdout)
    range_start = uptime.find("uptime: ") + 8
    uptime = uptime.split(": ", 1)[1]
    uptime = uptime.split(" \\", 1)[0]

    print("Uptime: "+str(uptime))

    RPC.update(details="Desktop: "+str(de), state="Uptime:   "+str(uptime), large_image=bigicon, large_text=themetooltip, small_image=smallicon, small_text=disptooltip) # Updates our presence
    time.sleep(5) # Can only update rich presence every 15 seconds

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

distroicon = "tux.png"
distro=run("neofetch distro", shell=True, stdout=PIPE)
distro=str(distro.stdout).lower()
if distro.count("pop!_os") > 0:
    distro="POP!_os"
    distroicon = "pop_os.png"
elif distro.count("xubuntu") > 0:
    distro="Xubuntu"
    distroicon = "xubuntu.png"
elif distro.count("ubuntu-mate") > 0:
    distro="Ubuntu Mate"
    distroicon = "ubuntu-mate.png"
elif distro.count("ubuntu-cinnamon") > 0:
    distro="Ubuntu Cinnamon"
    distroicon = "ubuntu-cinnamon.png"
elif distro.count("kubuntu") > 0:
    distro="Kubuntu"
    distroicon = "kubuntu.png"
elif distro.count("ubuntu") > 0:
    distro="Ubuntu"
    distroicon = "ubuntu.png"
elif distro.count("gallium") > 0:
    distro="Gallium OS"
    distroicon = "gallium.png"
elif distro.count("arch") > 0:
    distro="Arch"
    distro = "arch.png"
elif distro.count("gentoo") > 0:
    distro="Gentoo"
    distroicon = "gentoo.png"
elif distro.count("mint") > 0:
    distro="Linux Mint"
    distroicon = "linux-mint.png"
elif distro.count("fedora") > 0:
    distro="Fedora"
    distroicon = "fedora.png"
elif distro.count("neon") > 0:
    distro="KDE Neon"
    distroicon = "neon.png"
elif distro.count("parrot") > 0:
    distro="Parrot OS"
    distroicon = "parrot.png"
elif distro.count("red") > 0:
    distro="Red Hat"
    distroicon = "redhat.png"
else:
    distro="Linux"
    distroicon = "tux.png"

deicon = "sh.png"
de=run("neofetch de", shell=True, stdout=PIPE)
de=str(de.stdout).lower()
if de.count("gnome") > 0:
    de="GNOME"
    deicon = "gnome.png"
elif de.count("xfce") > 0:
    de="XFCE"
    deicon = "xfce.png"
elif de.count("cinnamon") > 0:
    de="Cinnamon"
    deicon = "cinnamon.png"
elif de.count("mate") > 0:
    de="MATE"
    deicon = "mate.png"
elif de.count("budgie") > 0:
    de="Budgie"
    deicon = "budgie.png"
elif (de.count("kde") > 0) or (de.count("plasma") > 0):
    de="KDE Plasma"
    deicon = "plasma.png"
elif de.count("lxde") > 0:
    de="LxDE"
    deicon = "lxde.png"
elif de.count("lxqt") > 0:
    de="LxQt"
    deicon = "lxde.png"
elif de.count("i3") > 0:
    de="i3"
    deicon = "bash.png"
elif de.count("unity") > 0:
    de="Unity"
    deicon = "unity.png"
else:
    de="bash"
    deicon = "bash.png"

uptime = ":)"
uptime = run("neofetch uptime", shell=True, stdout=PIPE)
uptime = str(uptime.stdout)
range_start = uptime.find("uptime: ") + 8
uptime = uptime.split(": ", 1)[1]
uptime = uptime.split(" \\", 1)[0]

print(icons)
bigicon = icons+"/"+distroicon
smallicon = icons+"/"+deicon
print("Big icon: "+bigicon)
print("Small icon: "+smallicon)

# INIT
client_id = "763805674240081960"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop

while True:  # The presence will stay on as long as the program is running
    print("Distro: "+distro)
    print("DE: "+de)
    print("Uptime: "+str(uptime))

    RPC.update(details="Desktop: "+str(de), state="Uptime:   "+str(uptime), large_image=bigicon, small_image=smallicon) # Updates our presence
    time.sleep(15) # Can only update rich presence every 15 seconds

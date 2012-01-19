#!/usr/bin/env python

def plist (file):
    listt = set([line.strip() for line in open(file)])
    return listt

def to_plist (plist1, file1):
    file = open (file1, 'w')
    plist1 = list (plist1)
    plist1.sort()
    for item in plist1:
        file.write (item+'\n')
    file.close()
        

lmde_gnome = plist('input/lmde-gnome.txt')
lmde_xfce = plist('input/lmde-xfce.txt')

only_lmde_gnome = lmde_gnome - lmde_xfce
to_plist (only_lmde_gnome, 'only_lmde_gnome.txt')

only_lmde_xfce = lmde_xfce - lmde_gnome
to_plist (only_lmde_xfce, 'only_lmde_xfce.txt')

mint9_gnome = plist('input/mint9-gnome.txt')
mint9_lxde = plist('input/mint9-lxde.txt')
mint9_fluxbox = plist('input/mint9-fluxbox.txt')

only_mint9_gnome = mint9_gnome - mint9_lxde - mint9_fluxbox
to_plist (only_mint9_gnome, 'only_mint9_gnome.txt')

mint9_gnome_not_lxde = mint9_gnome - mint9_lxde
to_plist (mint9_gnome_not_lxde, 'mint9_gnome_not_lxde.txt') 

mint9_gnome_not_fluxbox = mint9_gnome - mint9_fluxbox
to_plist (mint9_gnome_not_fluxbox, 'mint9_gnome_not_fluxbox.txt')

lmde_not_lxde = lmde_gnome.intersection(mint9_gnome_not_lxde)
to_plist (lmde_not_lxde, 'lmde_not_lxde.txt')

lmde_not_fluxbox = lmde_gnome.intersection(mint9_gnome_not_fluxbox)
to_plist (lmde_not_fluxbox, 'lmde_not_fluxbox.txt')

antix11 = plist('input/antix11.txt')
mepis11 = plist('input/mepis11.txt')

mepis_not_antix = mepis11 - antix11
to_plist (mepis_not_antix, 'mepis_not_antix.txt')

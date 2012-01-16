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

mint9_gnome = plist('input/mint9-gnome.txt')
mint9_lxde = plist('input/mint9-lxde.txt')
mint9_fluxbox = plist('input/mint9-fluxbox.txt')
only_mint9_gnome = mint9_gnome - mint9_lxde - mint9_fluxbox
to_plist (only_mint9_gnome, 'only_mint9_gnome.txt')



# -*- coding: utf-8 -*-

import os
import sys
from colorama import Fore, Style

print(f"{Fore.LIGHTRED_EX} O programa so vai funcionar se vc tiver privilegios administrativos. "
      f"Por favor, execute sudo"
      f" AutoSettingApkI"
      f"con.py [PATH ABSOLUTE] {Style.RESET_ALL}")
print("Caso tenha executado com sudo, desconsidere esse mensagem")
print('\n')

try:
    pwd = str(sys.argv[1])
    if pwd == '--help':
        print(f'{Fore.GREEN} use - sudo AutoSettingApkIcon.py [PATH ABSOLUTE] {Style.RESET_ALL}')
    else:
        if not os.path.isabs(pwd):
            print("Por favor, insira um caminho [PATH] absoluto.")
            sys.exit()
        nome = pwd.split('/')
        os.system(f'ln -sf {pwd} /usr/bin/{nome[-1]}')
        icon = str(input(f"{Fore.CYAN} Digite o caminho do icone: {Style.RESET_ALL}"))
        terminal = str(input(f"{Fore.CYAN} Terminal: {Style.RESET_ALL}"))
        os.chdir('/usr/share/applications/')
        with open(f"{nome[-1]}.desktop", 'w') as arquivo:
            arquivo.write(f"""
[Desktop Entry]
Version = 1.0
Type = Application
Terminal = {terminal}
Name = {nome[-1]}
Exec = /usr/bin/{nome[-1]}
Icon = {icon}
Categories = Application;
            """)
except IndexError:
    print(f' {Fore.RED} use - sudo AutoSettingApkIcon.py [PATH ABSOLUTE] {Style.RESET_ALL}')





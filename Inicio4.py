from Lonely.utilies import *
#
# entrada = ''
#
# while entrada != 99:
#     try:
#
#         print("""
#             [0] > Somar
#             [1] > Subtracao
#             [3] > Ajuda
#             [99] > Sair
#
#         """)
#         entrada = int(input("  >: "))
#     except ValueError:
#         print('\n')
#         print("Digite um valor valido !")
#
#     if entrada == 0:
#         soma(2, 2)
#     if entrada == 3:
#         # arquivo = open('texto.txt')
#         # print(arquivo.read())
#         # arquivo.seek(0)
#         # arquivo.close()
#         # with open('texto.txt') as arquivo:
#         #     print(arquivo.read())
#         with open('novo.txt', 'w') as arquivo:
#             arquivo.write('Sou gay e amo homem macho \n')
#             arquivo.write('Sou safado e dou pra negao')
#
#

#
#
# with open('numeros.txt', 'w') as arquivo:
#     while True:
#         try:
#             entrada = int(input("Digite os numeros, ou digite '99' para sair: "))
#             if entrada != 99:
#                 arquivo.write(f'{entrada}\n')
#             else:
#                 break
#         except ValueError:
#             print("Use numeros !")




import os

# print(os.getcwd())
# os.chdir('/usr/share/applications/')
# print(os.getcwd())
# with open('teste.desktop', 'w') as arquivo:
#     arquivo.write("""
#         [Desktop Entry]
# Version = 1.0
# Type = Application
# Terminal = false
# Name = teste
# Exec = /usr/bin/pycharm
# Icon = /root/Downloads/pycharm-community-2019.2/bin/pycharm.png
# Categories = Application;Development
#
#     """)
#
# with open('teste.desktop', 'r') as arq:
#     print(arq.read())

#
# print(os.getcwd())
#
# ret = os.path.join(os.getcwd(), 'Lonely')
# os.chdir(ret)
# print(os.getcwd())
#
# print(len(os.listdir()))




scan = list(os.scandir())
print(scan)
print(len(scan))

# print(scan[0].name)
# index = list()
# print(index)
nome = 'nomes.txt'
arr = [arq for arq in scan if arq.name == nome]
index = scan.index(arr[0])
print(scan[index].stat())


# i = 0
# index = []
# while i < len(scan):
#     index.append(list(scan[i].name for arq in scan if scan[i].name == nome))
#     i += 1
# print(index)

# print(scan[2].name)
# print(dir(scan[2]))
# print(scan[2].__sizeof__())
# print(scan[2].name)
# print(scan[2].stat())
# size = list(scan[2].stat())[6]
# print(size)














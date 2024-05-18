from commands import *
import time

clear()

def acessar_notas():
    while True:
        clear()
        try:
            opção = int(input('- ACESSO DE NOTAS -\n1 - Por materia\n2 - Por bimestre\n3 - Voltar\n- Opção: '))
        except ValueError:
            print('Opção invalida')
            time.sleep(0.7)
            continue
        else:
            if opção >= 1 and opção <= 3:
                if opção == 1:
                    clear()
                    while True:
                        print('- MATERIAS -')
                        for n in range(0, len(list_all_names())):
                            print(n, '-', list_all_names()[n].capitalize())
                        print('12 - SAIR')
                        try:
                            opc = int(input('- Opção: '))
                        except ValueError:
                            print('Opção invalida')
                            time.sleep(0.7)
                            clear()
                            continue
                        else:
                            clear()
                            if opc >= 0 and opc <= 12:
                                if opc == 12:
                                    acessar_notas()
                                else:
                                    print('{}'.format(list_all_names()[opc].capitalize()))
                                    print('1° Bimestre: {}'.format(get(list_all_names()[opc], 1)))
                                    print('2° Bimestre: {}'.format(get(list_all_names()[opc], 2)))
                                    print('3° Bimestre: {}'.format(get(list_all_names()[opc], 3)))
                                    print('4° Bimestre: {}'.format(get(list_all_names()[opc], 4)))
                                    input()
                            else:
                                print('Opção invalida')
                                time.sleep(0.7)
                                clear()
                                continue
                            clear()
                if opção == 3:
                    clear()
                    main_screen()
def main_screen():
    while True:
        clear()
        try:
            opção = int(input('- SISTEMA DE NOTAS -\n1 - Acessar notas\n2 - Atualizar nota\n3 - Média\n4 - Estatísticas\n5 - SAIR\n- Opção: '))
        except ValueError:
            print('Opção invalida')
            time.sleep(0.7)
            continue
        else:
            if opção >= 1 and opção <= 5:
                if opção == 1:
                    acessar_notas()
            else:
                print('Opção invalida')
                time.sleep(0.7)
                continue

main_screen()

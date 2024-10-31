def monta_computador(cpu,memoria,hd,monitor=17, **outros_atributos):
    print('O computador montado foi: ')
    print(f'\tCPU {cpu}')
    print(f'\tMonitor {memoria}')
    print(f'\tHD {hd}')
    print(f'\tMonitor {monitor}')
    print(f'\tOutros atributos {outros_atributos}')

    for chave, valor in outros_atributos.items():
        print(f'\t\t {chave} : {valor}')

monta_computador(cpu='Core i9', memoria=32, hd=500, webcan="Aacan", teclado="Multlaser")

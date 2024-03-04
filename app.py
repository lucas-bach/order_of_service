order_list = ['2013420','2384265','00488488','3178984','102384','31018998',
               '0121876','2025436','3215466']

for orders in order_list:
    if orders[0] == '2':
        print(f'Ordem {orders} - Manutenção Preventiva')
    elif orders[0] == '3':
        print(f'Ordem {orders} - Manutenção Corretiva')
    else:
        print(f'Ordem {orders} - Manutenção Preditiva')        

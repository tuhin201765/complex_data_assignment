mobile_data = {
    'status': True,
    'data':[
        {'name': 'Xiaomi Note 5', 'price': '300 USD ', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}


data = mobile_data.get('data')
name_1 = data[0]
name_2 = data[1]
name_3 = data[2]
name_4 = data[3]
name_5 = data[4]
name_6 = data[5]
spilit_1 = name_1.get('price').replace('300 USD','300')
spilit_2 = name_2.get('price').replace('200 USD','200')
spilit_3 = name_3.get('price').replace('180.5 USD','180.5')
spilit_4 = name_4.get('price').replace('89.60 USD','89.60')
spilit_5 = name_5.get('price').replace('110 USD','110')
spilit_6 = name_6.get('price').replace('350 USD','350')

exchange = mobile_data.get('exchange_rate')
BDT = exchange or '103.25'
equation_1 = float(BDT) * float(spilit_1)
equation_2 = float(BDT) * float(spilit_2)
equation_3 = float(BDT) * float(spilit_3)
equation_4 = float(BDT) * float(spilit_4)
equation_5 = float(BDT) * float(spilit_5)
equation_6 = float(BDT) * float(spilit_6)

print(f"{name_1.get('name')} is made in {name_1.get('made')}. The price is {spilit_1} USD which is almost equal to {equation_1} BDT")
print(f"{name_2.get('name')} is made in {name_2.get('made')}. The price is {spilit_2} USD which is almost equal to {equation_2} BDT")
print(f"{name_3.get('name')} is made in {name_3.get('made')}. The price is {spilit_3} USD which is almost equal to {equation_3}BDT")
print(f"{name_4.get('name')} is made in {name_4.get('made')}. The price is {spilit_4} USD which is almost equal to {equation_4} BDT")
print(f"{name_5.get('name')} is made in {name_5.get('made')}. The price is {spilit_5} USD which is almost equal to {equation_5} BDT")
print(f"{name_6.get('name')} is made in {name_6.get('made')}. The price is {spilit_6} USD which is almost equal to {equation_6} BDT")



currency = input('Vilken valuta som ska omvandlaskronor (euro eller kronor)? ')

amount = float(input('Vilken mängd av valutan? '))

if currency == "euro":
    answer = f"{amount * 11.22} kronor"
elif currency == "kronor":
    answer = f"{amount / 11.22} euro"
else :
    print('Felaktig inmatning')

print(f'Den omvandlade mängden är: {answer}')
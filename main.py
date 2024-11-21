from flask import Flask
from flask import redirect, url_for
from random import choice, randint

money_count = 10000
money_plus = 1

count = [0,1000000,50,100000,1000,10000000]
not_count = 0

def change_money(money_vid):
    global money_type, money_plus, not_count
    money_type = money_vid
    if money_vid == 0 and money_count >= count[money_vid]:
        money_plus = 1
        return True
    
    elif money_vid == 1 and money_count >= count[money_vid]:
        money_plus = 10000
        return True

    elif money_vid == 2 and money_count >= count[money_vid]:
        money_plus = 5
        return True

    elif money_vid == 3 and money_count >= count[money_vid]:
        money_plus = 1000
        return True

    elif money_vid == 4 and money_count >= count[money_vid]:
        money_plus = 100
        return True

    elif money_vid == 5 and money_count >= count[money_vid]:
        money_plus = 100000
        return True

    else:
        not_count = count[money_vid] - money_count
        return False
    



def change_random_facts(now_fact):
    global ran_fact
    while True:
        ran_fact = choice(facts)
        if ran_fact != now_fact:
            break


def upd_money():
    global money_count
    money_count += money_plus
    


heads_tails_img = [['https://cdn.monetnik.ru/storage/market-lot/61/87/164961/545469_big.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgdrP3o1C2PYIJ-bka_v7Xs1g7cfNHx7Flsg&s'],
['https://неразменныйрубль.рф/assets/images/products/43/big/10-rubley-1901-fz-revers-3251-1.png',
'https://неразменныйрубль.рф/assets/images/products/43/big/10-rubley-1901-fz-avers-3252-kopiya.png'],
['https://coins-mos.ru/wa-data/public/shop/products/97/40/34097/images/50600/50600.970.png',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_jhZo7xZmFjZFNMcPuMGsZoTl6ndm0WQ5Mw&s'],
['https://cdn.monetnik.ru/storage/market-lot/47/69/71247/197830_big.jpg',
'https://cdn.monetnik.ru/storage/market-lot/46/23/71246/197827_big.jpg'],
['https://filtorg.ru/images/thumbnails/189/189/detailed/58/100-rubley-1993-mmd-1.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFHkbLRnCQ8pX-f7dSbYOm3sG8Ko0I8ySFRg&s'],
['https://zoloto-md.ru/assets/images/products/9130/big/gp-1-75-800.jpg',
'https://cdn.monetnik.ru/storage/market-lot/63/94/599463/2142610_mainViewLot_2x.jpg']]




facts = ['Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.',
'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',
'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.',
'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.',
'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.']



ran_fact = choice(facts)
app = Flask(__name__)
money_type = 0



@app.route("/technologies")
def random_facts():
    return f"""<h1>{ran_fact}</h1>
    <a href='/change_facts'><button><h2>Сгенерировать новый факт</h2></button></a>
    <br><br>
    <a href='/'><button><h2><- Вернуться назад</h2></button></a>"""



@app.route("/change_facts")
def facts_change():
    change_random_facts(ran_fact)
    return redirect(url_for('random_facts'))


@app.route("/heads_and_tails")
def heads_tails():
    money = choice(heads_tails_img[money_type])
    if money == 'https://cdn.monetnik.ru/storage/market-lot/61/87/164961/545469_big.jpg' or money == 'https://неразменныйрубль.рф/assets/images/products/43/big/10-rubley-1901-fz-revers-3251-1.png' or money == 'https://coins-mos.ru/wa-data/public/shop/products/97/40/34097/images/50600/50600.970.png' or money == 'https://cdn.monetnik.ru/storage/market-lot/46/23/71246/197827_big.jpg' or money == 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFHkbLRnCQ8pX-f7dSbYOm3sG8Ko0I8ySFRg&s' or money == 'https://cdn.monetnik.ru/storage/market-lot/63/94/599463/2142610_mainViewLot_2x.jpg':
        return f"""<img src='{money}' width = 300px><h3>Орёл</h3><br>
        <h3>Количество монет:{money_count}</h3>
        <a href='/app_money_change'><button><h2>Изменить монетку</h2></button></a>
        <br><br>
        <a href='/heads_and_tails'><button><h2>Подкинуть монетку</h2></button></a>
        <br><br>
        <a href='/'><button><h2><- Вернуться назад</h2></button></a>"""

    else:
        return f"""<img src='{money}' width = 300px><h3>Решка</h3><br>
        <h3>Количество монет:{money_count}</h3>
        <a href='/app_money_change'><button><h2>Изменить монетку</h2></button></a>
        <br><br>
        <a href='/money_update'><button><h2>Подкинуть монетку</h2></button></a>
        <br><br>
        <a href='/'><button><h2><- Вернуться назад</h2></button></a>"""


@app.route("/app_money_change")
def change():
    return f"""<a href='/money_five'><button><img src = {heads_tails_img[0][1]} width=200px><h2>Пять рублей 2016 года</h2>
    <br><h3>Доход за клик: 1 монета</h3><br><h3>Цена: 0 монет</h3></button></a>
    <a href='/money_cent'><button><img src = {heads_tails_img[2][1]} width = 200px><h2>Один цент 2021 года</h2>    
    <br><h3>Доход за клик: 5 монет</h3><br><h3>Цена: 50 монет</h3></button></a>
    <a href='/money_100'><button><img src = {heads_tails_img[4][0]} width = 200px><h2>Сто рублей 1995 года</h2>    
    <br><h3>Доход за клик: 100 монет</h3><br><h3>Цена: 1000 монет</h3></button></a>
    <a href='/money_1000'><button><img src = {heads_tails_img[3][0]} width = 200px><h2>Тысяча рублей 1995 года</h2>    
    <br><h3>Доход за клик: 1000 монет</h3><br><h3>Цена: 100000 монет</h3></button></a>
    <a href='/money_10'><button><img src = {heads_tails_img[1][1]} width = 200px><h2>Десять рублей 1901 года</h2>    
    <br><h3>Доход за клик: 10000 монет</h3><br><h3>Цена: 1000000 монет</h3></button></a>
    <a href='/money_3'><button><img src = {heads_tails_img[5][0]} width = 200px><h2>Три рубля 2024 года</h2>    
    <br><h3>Доход за клик: 100000 монет</h3><br><h3>Цена: 10000000 монет</h3></button></a><br><br>
    <a href='/heads_and_tails'><button><h2>Назад</h2></button></a>"""



@app.route("/money_not")
def money_not():
    return f"<h1>Вам не хватает {not_count} монет</h1><a href='/app_money_change'><button><h2>Назад</h2></button></a>"



@app.route("/money_five")
def money_five():
    change_money(0)
    return redirect(url_for('heads_tails'))



@app.route("/money_cent")
def money_cent():
    if change_money(2) == True:
        return redirect(url_for('heads_tails'))

    else:
        return redirect(url_for('money_not'))



@app.route("/money_100")
def money_one_hung():
    if change_money(4) == True:
        return redirect(url_for('heads_tails'))

    else:
        return redirect(url_for('money_not'))



@app.route("/money_1000")
def money_one_t():
    if change_money(3) == True:
        return redirect(url_for('heads_tails'))

    else:
        return redirect(url_for('money_not'))



@app.route("/money_10")
def money_ten():
    if change_money(1) == True:
        return redirect(url_for('heads_tails'))

    else:
        return redirect(url_for('money_not'))



@app.route("/money_3")
def money_three():
    if change_money(5) == True:
        return redirect(url_for('heads_tails'))

    else:
        return redirect(url_for('money_not'))



@app.route("/money_update")
def money_update():
    upd_money()
    return redirect(url_for('heads_tails'))



@app.route("/random_num")
def random_num():
    return f"""<h1>Ваше число: {randint(0,1000)}</h1>
    <a href='/random_num'><button><h2>Сгенерировать новое число</h2></button></a>
    <br><br>
    <a href='/'><button><h2><- Вернуться назад</h2></button></a>"""



@app.route("/")
def main():
    return f'''<a href="/technologies"><button><h2>Посмотреть случайный факт о технологических зависимостых!</h2></button></a><br><br>
    <a href="/heads_and_tails"><button><h2>Орёл или Решка!</h2></button></a><br><br>
    <a href="/random_num"><button><h2>Генератор случайных чисел!</h2></button></a>'''

app.run(debug=True)
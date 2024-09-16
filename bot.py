import os

# Достаём из неё longpoll

from vk_api.longpoll import VkLongPoll, VkEventType

from fuzzywuzzy import fuzz

# Создаём переменную для удобства в которой хранится наш токен от группы

token="vk1.a.0JFUXFXywwWm8VSwOSEw9mqh6qJ27qAuCr-xbUBQkN9Pm9rfF6DpbtGpm1NmgiXIQ7eSJTTRpn6veo8rLo3pYmrnzbN-C_GmwFY8EdMxV6BjRt26MU4CtwNZKxh4RESZHahUSLOxzq4p4Kp5m9ctlvi1RpmRbU9BE0llrl8cyIzJgWtrTahqpfmf7gmwlX86isuOywI0CQGzCT54Vp3WgA" # В ковычки вставляем аккуратно наш ранее взятый из группы токен.

# Подключаем токен и longpoll

bh = vk_api.VkApi(token = token)

give = bh.get_api()

longpoll = VkLongPoll(bh)

# Создадим функцию для ответа на сообщения в лс группы

def blasthack(id, text):

bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

# Загружаем список фраз и ответов в массив

mas=[]

if os.path.exists('slovar.txt'):

f=open('slovar.txt', 'r', encoding='UTF-8')

for x in f:

if(len(x.strip()) > 2):

mas.append(x.strip().lower())

f.close()

# Слушаем longpoll(Сообщения)

for event in longpoll.listen():

if event.type == VkEventType.MESSAGE_NEW:

# Чтобы наш бот не слышал и не отвечал на самого себя

if event.to_me:

# Для того чтобы бот читал все с маленьких букв

message = event.text.lower()

# Получаем id пользователя

id = event.user_id

if os.path.exists('slovar.txt'):

a = 0

n = 0

nn = 0

for q in mas:

if('u: ' in q):

# С помощью fuzzywuzzy получаем, насколько похожи две строки

aa=(fuzz.token_sort_ratio(q.replace('u: ',''), message))

if(aa > a and aa!= a):

a = aa

nn = n

n = n + 1

s = mas[nn + 1]

blasthack(id, s)

f=open('log.txt', 'a', encoding='UTF-8')

f.write('u: ' + message + '\n' + s +'\n')

f.close()

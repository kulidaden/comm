# Commentars
Це звичайний сайт де користувачі можуть залишати свої коменарі.

#Інсталяція.
1. Клонуйте репозиторій: `git clone https://github.com/kulidaden/comm.git`
2. Потім ці команди: `cd comm` -> `cd commentars`
3. Виконайте ці дві команди для налаштування: `pip install -r requirements.txt` -> `python manage.py migrate`
   
## Використання
У консолі(терміналі), будучи в папці `commentars`, напишіть команду: `python manage.py runserver` або `python manage.py runserver 8001`.
Перейдіть за посиланням, далі зареєструйтесь або залогіньтесь. Після чого у Вас буде можливість писати коментарі і використовувати програму.
##Docker
pull: docker pull denyskulida/commentars-django
run: docker run -d -p 8000:8000 --name commentars-django denyskulida/commentars-django:latest

## Контакт
Якщо Вам потрібна консультація або допомога по використанні програми: Telegram: @Kosmos_qwerty

## Відомі проблеми
На жаль, програма не розвернута на сайті, тому ви не бачитимете коментарі які пишуть у реальму часі інші користувачі.

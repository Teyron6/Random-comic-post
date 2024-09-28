# Публикация комиксов
Данный скрипт постит в телеграм случайные комиксы автора xkcd
## Как установить
Для работы скрипта нужно иметь python3 и установить библиотеки из `requirements.txt` с помощью этой команды:
```
py -m pip install -r requirements.txt
```
## Переменные окружения
Нужно создать и заполнить файл `.env` таким образом:
```
TG_TOKEN = 'токен'
GROUP_ID = 'id группы/канала'
```
Получить эти переменные можно с помощью @BotFather и @groupinfobot в телеграме
## Запуск
Запустить скрипт можно этой командой:
```shell
python main.py
```
Итогом работы скрипта будет комикс с комментарием автора в телеграм канале/группе
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
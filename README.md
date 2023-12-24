# Программирование интернет-приложений

## Состав группы
### КС-20-1б
1. Камянецький Сергей `Kam-Sergei`
2. Матяж Владимир `MatyazhV`

## Описание программы
Охранная система с камерой. Если перед камерой происходит движение, то делается фотография и отправляется в директорию uploads. Интернет приложение выводит список фотографий из директории uploads. Через интернет приложение можно сделать фотографию в любой момент, нажав на кнопку "Сделать скриншот". Нажав на любую фотографию из списка, она скачается на устройство. Чтобы удалить фотографию, нужно нажать на кнопку " Удалить".

------

# Установка
1. Установите менеджер пакетов `apt-get install python3-pip`
2. Установите дополнительные инструменты `sudo apt install -y build-essential libssl-dev libffi-dev python3-dev`
3. Установите venv `sudo apt install -y python3-venv`
4. Создайте виртуальное окружение `python3 -m venv env`
5. Активируйте виртуальную среду `source env/bin/activate`
6. Выполните установку пакетов из файла requirements.txt `pip install -r requirements.txt`

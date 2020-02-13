import bs4 as bs4
import requests


class VkBot:

    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["Привет", "Запись", "Цена", "Банкротство", "Сайт", "Клиент", "Инфо", "Сергей", "Погода", "Время", "Пока"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):

        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!"

        # Запись
        if message.upper() == self._COMMANDS[1]:
            txt44 = 'Несмотря на то, что время нашей работы с 12 до 18 часов по будням (пн-чт), мы готовы принять Вас в удобные для Вас время и день.'
            txt45 = 'Для соглосования даты и времени приема, напишите мне в WhatsApp https://wa.me/79059791076 или Telegram https://t.me/sergekretov или позвоните по телефону 89059791076'
            txt46 = 'Обращаю Ваше внимание на то, что ответ может поступить не сразу, так как общаться вы будете с реальным человеком, а не с ботом, соответственно Сергей Сергеевич может быть занят в судебном процессе, в работе с клиентом или отдыхать, но в любом случае он выйдет на связь в кратчайшее время.'

            reply_text = f'Уважаемый {self._USERNAME}, мы ведем прием исключительно по предварительной записи! {txt44}\n\n{txt45}\n{txt46}'
    
            return reply_text

        # Цена
        elif message.upper() == self._COMMANDS[2]:
            txt72 = 'Консультация от 500 до 1000 руб.'
            txt73 = 'Подготовка искового заявления от 2500 до 5000 руб.'
            txt74 = 'Подготовка жалоб от 2500 до 4000 руб.'
            txt75 = 'Участие представителя в суде от 5000 до 10000 руб.'
            txt76 = 'Подготовка заявлений от 1500 до 3000 руб.'

            reply_text = f'Уважаемый {self._USERNAME}, представляем Вам краткий прайс-лист.\n\n{txt72}\n{txt73}\n{txt74}\n{txt75}\n{txt76}\n\nБолее точную и подробную стоимость Вы можете узнать на консультации, так как цена зависит от конкретной ситуации и объема необходимых действий.'
    
            return reply_text

        # Банкротство
        elif message.upper() == self._COMMANDS[3]:
            txt19 = 'Списать долги и кредитные обязательства - законный способ через процедуру Банкротства.'
            txt20 = 'Процедура Банкротства осуществляется через Арбитражные суды. С нашей помощью сотни граждан уже освободились от своих долгов и начали жизнь с чистого листа. Начать процедуру банкротства может любой гражданин, сумма долгов у которого (суммарно) превышает 500 000 рублей. При этом не важно имеются или нет судебные решения, ведётся или нет исполнительное производство у судебных приставов, продан или нет ваш долг коллекторам.'
            txt21 = 'Какие долги списываются:'
            txt22 = '🏦 Любые кредиты'
            txt23 = '🏢 Коммунальные долги'
            txt24 = '💵 Любые займы по распискам и договорам как у физлиц, так и у микро финансовых организаций'
            txt25 = '⚖️ Прочие обязательства присуждённые судом'
            txt26 = '💼 Обязательства по ранее осуществляющей предпринимательской деятельности'
            txt27 = 'Какие долги НЕ СПИСЫВАЮТСЯ:'
            txt28 = '👶 Алиментные обязательства'
            txt29 = '🏥 Присуждённые суммы по возмещению вреда здоровью'
            txt30 = 'Основные вопросы связанные с Банкротством:'
            txt31 = '🏡 Единственное жильё не заберут'
            txt32 = '📺 Предметы обычного домашнего обихода не заберут'
            txt33 = '🛠 С работы не уволят'
            txt34 = '🏖 За пределы РФ выпускают'
            txt35 = '💶 Новые кредиты можно брать через 5 лет'
            txt36 = '👶 Родительских прав не лишают'
            txt37 = 'Зачем мы нужны Вам в этой процедуре:'
            txt38 = '⚖️ У нас большой опыт с 99% положительным результатом'
            txt39 = '🏛 Мы сотрудничаем с финансовыми управляющими без которых эта процедура не возможна'
            txt40 = '💻 Всю бумажную волокиту наши юристы берут на себя'
            txt41 = '⏱ Имея глубокие познания в юриспруденции, мы максимально грамотно и законно подготовим вас к данной процедуре, дабы сохранить ваше имущество и решить иные «тонкие» вопросы'
            txt42 = 'Остались вопросы или желаете записаться на личную консультацию? Или же сразу заключить договор и начать работу? Пишите в личку на WhatsApp 89059791076 или перейдите по этой ссылке: https://wa.me/79059791076 а так же на Telegram 89059791076 или перейдите по ссылке https://t.me/sergekretov'

            reply_text = f'{txt19}\n{txt20}\n\n{txt21}\n{txt22}\n{txt23}\n{txt24}\n{txt25}\n{txt26}\n\n{txt27}\n{txt28}\n{txt29}\n\n{txt30}\n{txt31}\n{txt32}\n{txt33}\n{txt34}\n{txt35}\n{txt36}\n\n{txt37}\n{txt38}\n{txt39}\n{txt40}\n{txt41}\n\n{txt42}'
    
            return reply_text


        # Погода
        elif message.upper() == self._COMMANDS[8]:
            return self._get_weather()

        # Время
        elif message.upper() == self._COMMANDS[9]:
            return self._get_time()

        # Пока
        elif message.upper() == self._COMMANDS[10]:
            return f"Пока-пока, {self._USERNAME}!"

        else:
            txt1 = 'Я виртуальный помощник Сергея Сергеевича из Юридического агентства ПРИОРИТЕТ (г.Норильск).'
            txt2 = 'Наше агентство оказывает следующие услуги:'
            txt3 = '👨🏻‍🎓Консультации по любым правовым вопросам'
            txt4 = '💼Подготовка исков, жалоб, претензий'
            txt5 = '⚖️Участие представителя в Суде'
            txt6 = '💶Банкротство граждан (списание долгов)'
            txt7 = '🏛Арбитражные споры'
            txt8 = '💻Прочие сопутствующие услуги'
            txt9 = 'Введите соответствующую команду для получения интересующей Вас информации:'
            txt10 = '📆Записаться на прием - <Запись>'
            txt11 = '📚Узнать цены - <Цена>'
            txt12 = '💸Подробнее о банкротстве - <Банкротство>'
            txt13 = '📖Посетить сайт агентства - <Сайт>'
            txt14 = '🖥Войти в кабинет клиента - <Клиент>'
            txt15 = '📰Получить краткую информацию о нас - <Инфо>'
            txt16 = '📲Написать в личку Сергею Сергеевичу - <Сергей>'
            reply_text = f'Привет, {self._USERNAME}!\n\n{txt1}\n{txt2}\n\n{txt3}\n{txt4}\n{txt5}\n{txt6}\n{txt7}\n{txt8}\n\n{txt9}\n{txt10}\n{txt11}\n{txt12}\n{txt13}\n{txt14}\n{txt15}\n{txt16}'
    
            return reply_text

    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    @staticmethod
    def _clean_all_tag_from_str(string_line):

        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

    @staticmethod
    def _get_weather(city: str = "норильск") -> list:

        request = requests.get("https://sinoptik.com.ru/погода-" + city)
        b = bs4.BeautifulSoup(request.text, "html.parser")

        p3 = b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = b.select('.temperature .p6')
        weather4 = p6[0].getText()

        result = ''
        result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result

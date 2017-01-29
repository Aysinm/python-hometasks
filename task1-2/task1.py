from Prepods_1 import Prepod
from modern_prepods import ModernPrepod
import lxml.etree as et
import urllib.request


def teachers_with_etree():
    opener = urllib.request.build_opener()
    parser = et.HTMLParser()
    tree = et.parse(opener.open('https://www.hse.ru/org/persons/'), parser)
    # Проходим по всем людям
    prepods = []
    for tag in tree.findall(".//div[@class='post__content post__content_person']"):
        # div с контактами
        contacts_tags = tag.findall(".//div[@class='l-extra small']")
        # Если есть информация о контактах
        # может быть несколько телефонов и почт, а может не быть вообще
        phones = []
        emails = []
        if contacts_tags:
            contacts_tag = contacts_tags[0]
            for contact_tag in contacts_tag:
                # телефоны лежат в тэгах спан
                if contact_tag.tag == 'span':
                    phones.append(contact_tag.text)
                # почты лежат в тэгах a
                if contact_tag.tag == 'a':
                    # Никак не хочет доставаться текст из почты только так получилось
                    email = contact_tag.values()[1]
                    email = email.replace('[', '').replace(']', '').replace(',', '').replace('"', '').replace('-at-',
                                                                                                              '@')
                    emails.append(email)
                    # print(phones)
                    # print(emails)
        # div с основной информацией
        info_tags = tag.findall(".//div[@class='main content small']")
        name = ''
        dolj = ''
        if info_tags:
            info_tag = info_tags[0]
            for tag in info_tag:
                # имя
                name = tag[0][0].get('title')
                # print(name)
                # должность
                ptag = tag[1]
                dolj_tag = ptag[0]
                dolj = dolj_tag.text
                dolj = dolj.strip().replace(':', '')
                # print(dolj)
        # собираем преподавателя в класс
        # разбиваем имя на 3 части
        # О! у кого то 2 или аж 5 имен)))
        last_name = ""
        subname = ""
        fio = name.split(' ')
        if len(fio) == 1:
            name = fio[0]
        elif len(fio) == 2:
            name = fio[0]
            last_name = fio[1]
        else:
            name = fio[0]
            last_name = fio[1]
            subname = fio[2]

        new_prepod = Prepod(name, subname, last_name, phones, "", dolj, emails)
        prepods.append(new_prepod)

        # модернизированный класс преподаватеся, генерится на лету (можно не использовать)
        # new_prepod = ModernPrepod(name=name, subname=subname, last_name=last_name, phones=phones, dolj=dolj, emails=emails)
        # prepods.append(new_prepod)
    return prepods


def teachers_with_xpath():
    opener = urllib.request.build_opener()
    parser = et.HTMLParser()
    tree = et.parse(opener.open('https://www.hse.ru/org/persons/'), parser)
    # Проходим по всем людям
    prepods = []
    for tag in tree.xpath(".//div[@class='post__content post__content_person']"):
        # div с контактами
        contacts_tags = tag.xpath(".//div[@class='l-extra small']")
        # Если есть информация о контактах
        # может быть несколько телефонов и почт, а может не быть вообще
        phones = []
        emails = []
        if contacts_tags:
            contacts_tag = contacts_tags[0]
            for contact_tag in contacts_tag:
                # телефоны лежат в тэгах спан
                if contact_tag.tag == 'span':
                    phones.append(contact_tag.text)
                # почты лежат в тэгах a
                if contact_tag.tag == 'a':
                    # Никак не хочет доставаться текст из почты только так получилось
                    email = contact_tag.values()[1]
                    email = email.replace('[', '').replace(']', '').replace(',', '').replace('"', '').replace('-at-',
                                                                                                              '@')
                    emails.append(email)
                    # print(phones)
                    # print(emails)
        # div с основной информацией
        info_tags = tag.xpath(".//div[@class='main content small']")
        name = ''
        dolj = ''
        if info_tags:
            info_tag = info_tags[0]
            for tag in info_tag:
                # имя
                name = tag[0][0].get('title')
                # print(name)
                # должность
                ptag = tag[1]
                dolj_tag = ptag[0]
                dolj = dolj_tag.text
                dolj = dolj.strip().replace(':', '')
                # print(dolj)
        # собираем преподавателя в класс
        # разбиваем имя на 3 части
        # О! у кого то 2 или аж 5 имен)))
        last_name = ""
        subname = ""
        fio = name.split(' ')
        if len(fio) == 1:
            name = fio[0]
        elif len(fio) == 2:
            name = fio[0]
            last_name = fio[1]
        else:
            name = fio[0]
            last_name = fio[1]
            subname = fio[2]

        new_prepod = Prepod(name, subname, last_name, phones, "", dolj, emails)
        prepods.append(new_prepod)

        # модернизированный класс преподаватеся, генерится на лету (можно не использовать)
        # new_prepod = ModernPrepod(name=name, subname=subname, last_name=last_name, phones=phones, dolj=dolj, emails=emails)
        # prepods.append(new_prepod)
    return prepods


if __name__ == '__main__':
    # проверяем что всё правильно
    print('_________________________________________etree__________________________________________________')
    teachers = teachers_with_etree()
    [print(t) for t in teachers]
    print('_________________________________________xpath__________________________________________________')
    teachers = teachers_with_xpath()
    [print(t) for t in teachers]

from selene.support.shared import browser
from selene import browser, be, have
import os


def test_forms_demoga_praktika():

    # Заполнение формы
    browser.element('#firstName').type("Dinara")
    browser.element('#lastName').type("Kokhanovskaya")
    browser.element('#userEmail').type("dinkokh@example.com")
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type("9090909090")

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1984"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="6"]').click()
    browser.element('.react-datepicker__day--027').click()

    # Выбор предметов
    browser.element('#subjectsInput').type('Computer Science').press_enter()

    # Выбор хобби
    browser.element('label[for="hobbies-checkbox-3"]').click()

    # Загрузка файла
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/image.png'))

    # Ввод адреса
    browser.element('#currentAddress').type('460000,Russia, Orenburg, Solynoy')
    browser.element('#react-select-3-input').type('Uttar Pradesh').click().press_enter()
    browser.element('#react-select-4-input').type('Agra').click().press_enter()

    # Отправка формы
    #browser.element('#submit').click()
    browser.element("#submit").execute_script("element.click()")

    # Проверка
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
    (
    'Dinara Kokhanovskaya',
    'dinkokh@example.com',
    'Female',
    '9090909090',
    '27 July,1984',
    'Computer Science',
    'Music',
    'image.png',
    '460000,Russia, Orenburg, Solynoy',
    'Uttar Pradesh Agra'
    ))

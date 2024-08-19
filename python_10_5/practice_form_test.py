import os
import time

from selene import browser, have, be, command

"""
Разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form

1. Find the field;
2. Fill the field;
3. Fill the form;
4. Submit the form;
5. Eat cookie (no sugar, low fat)

Requirements:
Name - First name/ Last name - input text id: firstName; input id: lastName
Gender (battle helicopter) - input radiobuttons id:gender-radio-1; gender-radio-2; gender-radio-3
Mobile (10 digits) - input text id="userNumber" minlength="10"/ maxlength="10"

Optional:
Email - text id: userEmail pattern="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
Date of Birth - id="dateOfBirthInput" value="03 Apr 2022"
Subjects - id="subjectsInput"
choose Hobbies - input checkbox id:hobbies-checkbox-1; hobbies-checkbox-2; hobbies-checkbox-3
select and upload a Picture - id: uploadPicture
Current Address - id="currentAddress"
State and city - dropdowns - id="react-select-3-input"; id="react-select-4-input"

Submit - id="submit"
"""


def test_full_form_fill():

    browser.open('/')

    browser.element('#firstName').type('Abc1')
    browser.element('#lastName').type('EFG2')
    browser.element('#userEmail').type('name@example.com')
    browser.element('#gender-radio-2').perform(command.js.click)
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').perform(command.js.click)
    browser.element("//div[@aria-label='Choose Tuesday, April 16th, 2024']").perform(command.js.click)
    browser.element('#subjectsInput').send_keys('English').press_tab()
    browser.element('#hobbies-checkbox-1').perform(command.js.click)
    browser.element('#uploadPicture').send_keys("/Users/evgeniy.l/Documents/Projects/My/guru_in_py/python_10_5/img-1.png")
    browser.element('#currentAddress').type('Lenins street')
    browser.element('#react-select-3-input').send_keys('NCR').press_tab()
    browser.element('#react-select-4-input').send_keys('Delhi').press_tab()

    browser.element('#submit').perform(command.js.click)

    browser.element('(//td)[2]').should(have.exact_text('Abc1 EFG2'))
    browser.element('(//td)[4]').should(have.exact_text('name@example.com'))
    browser.element('(//td)[6]').should(have.exact_text('Female'))
    browser.element('(//td)[8]').should(have.exact_text('1234567890'))
    browser.element('(//td)[10]').should(have.exact_text('16 April,2024'))
    browser.element('(//td)[12]').should(have.exact_text('English'))
    browser.element('(//td)[14]').should(have.exact_text('Sports'))
    browser.element('(//td)[16]').should(have.exact_text('img-1.png'))
    browser.element('(//td)[18]').should(have.exact_text('Lenins street'))
    browser.element('(//td)[20]').should(have.exact_text('NCR Delhi'))


def test_requirements_form_fill():
    browser.open('/')

    browser.element('#firstName').type('abc')
    browser.element('#lastName').type('abc')
    browser.element('#gender-radio-1').perform(command.js.click)
    browser.element('#userNumber').type('1234567890').press_enter()

    browser.element('(//td)[2]').should(have.exact_text('abc abc'))
    browser.element('(//td)[6]').should(have.exact_text('Male'))
    browser.element('(//td)[8]').should(have.exact_text('1234567890'))


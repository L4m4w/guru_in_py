python_10_5
~~~~~~~~~~
5. Selene. Яков Крамаренко. Занятие в записи
1. Лайвкодинг – тесты для GitHub
2. DOM для начинающих
3. Рассмотрим базовые возможности Selene и CSS / Xpath-селекторы
4. Продолжаем изучать библиотеку Selene (справочник-шпаргалка)
5. Практика. Работаем с тренажером demoqa.com

lesson // https://www.youtube.com/watch?v=WeNaNvAN8M0

Ссылка на репозиторий // https://github.com/yashaka/selene-in-action/tree/qaguru-lesson-selene-01-py06
Ссылка на репозиторий из предыдущих версий урока (с дополнительными примерами команд в комментариях к коду) // https://github.com/yashaka/selene-in-action

Укороченная версия урока в виде статьи – Селениды в действии (можно начать со статьи для более быстрого обзора возможностей Selene на практическом примере, и потом продолжить смотреть основную запись урока) // https://autotest.how/selenides-in-action-docs-md?lang=ru&code=py

Официальная документация // https://yashaka.github.io/selene/

Чат по Selene // https://t.me/selene_py_ru

FAQ по Selene // https://t.me/selene_py_ru/475

Краткая шпаргалка по основным командам Selene // https://t.me/selene_py_ru/7208

Примеры использования Selene для разных контекстов запуска тестов // https://github.com/yashaka/selene/tree/master/examples

Если вместо серфинга по коду хочется более лаконично увидеть список настроек драйвера для такого рода кейсов – можно просто посмотреть примеры в этой статье о конфигурациях Selene из официальной документации. // https://yashaka.github.io/selene/reference/configuration/

Примеры создания объекта драйвера вручную с автоматической установкой драйверов браузеров с помощью библиотеки webdriver_manager. https://github.com/SergeyPirogov/webdriver_manager#install-manager


Дополнительное видео от Якова по темам: // https://www.loom.com/share/8dc071f0059348bfbeaf46a6a2daffda
– Ветвления в тестах (команды matching(condition) и wait_until(condition)
– Больше симуляции шорткатов типа Command + a
– Фриз инспектора для заморозки пропадающих компонентов
– Формат проекта для тестов (tests, .gitignore, requirements, root package, project name, conftest)
– Опция config.base_url
– Базовое управление конфигурацией через переменные среды

Краткое введение в HTML и CSS-селекторы + Материалы // https://autotest.how/intro-to-css-selectors-guide-md?lang=ru
Справка по синтаксису CSS-селекторов //  https://www.w3schools.com/cssref/css_selectors.php

Шпаргалка по Селекторам: рецепты CSS, XPath и JS // https://www.red-gate.com/simple-talk/wp-content/uploads/imported/1269-Locators_table_1_0_2.pdf?file=4937

Введение в XPath на сравнении с CSS // https://www.loom.com/share/77a4b79b773b43edad09ca2514c0ed4a?sid=74d730c6-f34a-48e4-99b7-cccad11ddc25

Рецепт поиска по css-классу/class-name в XPath // https://tanzu.vmware.com/content/blog/xpath-css-class-matching
 
Статья о критериях хороших селекторов от Алексея Баранцева: «...как строить хорошие локаторы?» // https://barancev.github.io/good-locators/

Доклад о лучших практиках построения селекторов от Алексея Баранцева: «Десять правил построения хороших локаторов» // https://www.youtube.com/watch?v=_TNh2ydpoOw


Дополнительно:

На уроке я упоминал, что лучшее предусловие к тесту по открытию страницы –  вызывать в тесте явно максимум в виде функции, но не скрывать внутри фикстуры полностью. Рекомендую по этой же теме почитать статью.  // https://jamesnewkirk-typepad-com.translate.goog/posts/2007/09/why-you-should-.html?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=uk&_x_tr_pto=wapp&_x_tr_hist=true
Кому интересна вся эта философия, но также и практика – книга Владимира Хорикова будет более основательным трудом. Предпочтение явным предусловиям также коррелирует с принципом «Explicit is better than implicit» из официального кодекса The Zen of Python.// https://peps.python.org/pep-0020/
Следуя этому же принципу, я явно прописывал в уроке scope='function' для фикстур, хотя для последних это и так является значением по умолчанию. Рекомендую ознакомиться и с другими принципами из этого кодекса. Они помогут понять, почему Python такой, какой он есть и также помогут писать более идиоматичный код.


- Бонусное видео-продолжение к уроку «Фикстура для поддержки дополнительных браузеров в тесте» // https://www.loom.com/share/8bb704416ba243ed9fbca46c8b9af7ef

- С селеном или без? - отвечаем на вопрос в докладе Якова Крамаренко «Селениды против велосипедов» // https://www.youtube.com/watch?v=yv0Qpkdh-pc

- Строим свой фреймворк типа Selene на основе Selenium Webdriver на воркшопе с Яковом Крамаренко: Часть 1, Часть 2 // https://www.youtube.com/watch?v=DPV__58mcoM // https://www.youtube.com/watch?v=sYK47fF2qFo
- Что нужно ,чтобы научиться свободно программировать и создавать свои фреймворки? – Ответ в этой карте обучения. https://miro.com/app/board/uXjVOztNojY=/?share_link_id=464580841774

Общий конспект лекций курса // https://github.com/qa-guru/knowledge-base



~~~~~~~~~~


Разбор домашнего задания к уроку «Selene». Яков Крамаренко. Занятие в записи
~~~~~~~~~~
lesson // https://www.youtube.com/watch?v=r31elglwwwQ

Ссылка на репозиторий // https://github.com/yashaka/demoqa-tests/tree/py-03-lesson-05-practice-form-task-review-final

Резюме вариантов работы с таблицей и другие нюансы реализации тестов // https://www.loom.com/share/52ad196c796a49c2b619de1db0d40040

Явные прекондишены // https://www.loom.com/share/640ea006f94543169951c483919458e5

Масштабируем страницу в браузере через JS и улучшаем стабильность теста в других браузерах // https://www.loom.com/share/7b47624f8f1f42199ba06b52fd69ed4a

Ссылка на код // https://github.com/yashaka/demoqa-tests/tree/py-03-lesson-05-practice-form-task-review-final-scale-n-firefox-support

https://www.youtube.com/watch?v=Yr1RTJJihTI
https://www.youtube.com/watch?v=PffMfzpCgyw
~~~~~~~~~~

python_10_8
~~~~~~~~~~
https://www.youtube.com/watch?v=dnCooWIYbTg
https://github.com/qa-guru/qa_guru_python_7_8
https://github.com/qa-guru/knowledge-base


Тестируем классы интернет-магазина
Вам нужно реализовать и протестировать классы интернет-магазина. Все места, которые нужно дописать как в тестах, так и классах, отмечены # TODO.
При реализации обращайте внимание на типизацию аргументов методов и возвращаемых значений. Так же обратите внимание на организацию тестов в файле с тестами:
– Тесты сгруппированы по классу, который они тестируют.
– Каждый тест называется именем соответствующего ему метода.
Вы можете начать как с реализации классов, так и с тестов.
Дополнительные вопросы:
– С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?
– Почему для хранения товаров в корзине используется словарь, а не список?
– Зачем нужен hash в классе Product? Изучите этот метод и объясните, почему он нужен.
~~~~~~~~~~


python_10_9
~~~~~~~~~~

https://www.youtube.com/watch?v=wzwMwGd3weU
https://github.com/qa-guru/qa_guru_python_1_7

ИНСТРУКЦИЯ ПО УСТАНОВКЕ ALLURE


Устанавливаем Аллюр с помощью инсталлятора как в лекции.

Если по каким-то причинам аллюр не удаётся установить с помощью инсталлятора, тогда действуем так:



Как приготовить Аллюр по быстрому:

1. Если не установлена Java - установить

2. Отсюда https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

забираем последнюю версию (или какая тебе нужна)

допустим это 2.20.1:

здесь https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.20.1/

качаем архив allure-commandline-2.20.1.zip

3. Разархивируем в корень проекта, получаем папку allure-2.20.1

4. Переименовываем для удобства папку allure-2.20.1 в allure

Аллюр по быстрому готов, теперь запускать отчет можно из корня проекта командой (если папка с результатами в allure-result и она в корне проекта):

Mac: allure/bin/allure serve

Win: allure/bin/allure.bat serve


Вариант чуть сложнее, но один раз сделал, и будет работать всегда (начиная с п.3 примерно так делают установщики аллюра):


1. как п.1 в аллюр по быстрому

2. как п.2 в аллюр по быстрому

3. разархивируем куда тебе удобно

4. прописываем в переменную окружения PATH полный путь до папки allure/bin/ в которой лежат исполняемые файлы allure для Mac и allure.bat для Win

Например путь для Mac: /Users/User_name/PythonProject/tests_demoqa/allure/bin

Теперь запускать отчет можно из корня проекта командой (если папка с результатами в allure-result и она в корне проекта):

Mac: allure serve

Win: allure.bat serve


Аттеншн:

1. Если ты креативен, и папка с результатами называется не allure-results, то после serve надо указать имя этой папки

2. В случае, если папка с результатами формируется не в корне проекта, то в конфгурации запуска надо поправить working directory - указать корневую папку проекта, это исправит ситуацию

3. Параметры запуска:

--alluredir=allure-results - указывает аллюру имя папки куда записывать результаты

--clean-alluredir - указывает аллюру, что при запуске надо удалить содержимое папки alluredir (удалить результаты предыдущего запуска, обычно полезно при разработке и отладке, чтобы не было мусора)

4. В корне проекта можно создать файл pytest.ini следующего содержания:

[pytest]

addopts =

    --clean-alluredir

    --alluredir=allure-results

в таком случае, параметры запуска будут браться из этого файла, и указывать отдельно в команде запуска эти параметры будет не нужно 

5. Папку  с аллюром allure (если она лежит в проекте) и папку с результатами allure-results (или твое имя папки, если ты задавал другое) надо добавить в .gitignore, эти папки не должны попасть в репозиторий

дока https://docs.qameta.io/allure-report/#_installing_a_commandline

п 2.1.4. Manual installation

_____________

Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
Этот тест представить в трех вариантах:

1. Чистый Selene (без шагов)

2. Лямбда шаги через with allure.step

3. Шаги с декоратором @allure.step

4. Разметку тестов всеми аннотациями

В качестве ответа на задание приложите ссылку на свой репозиторий GitHub в поле ответа

~~~~~~~~~~

python_10_10

~~~~~~~~~~
Урок // https://www.youtube.com/watch?v=8iWqsZmihKk
Репо // https://github.com/yashaka/demoqa-tests/tree/py-04-lesson-po-practice-form-task-final

О синтаксисе классов в Python: «Инструментарий для работы с классами в Python» // https://www.youtube.com/watch?v=tfaFMfulY1M

Мартин Фаулер о PageObject // https://martinfowler.com/bliki/PageObject.html

Рекомендации и общепринятые договоренности в подборе имен (Python) // https://autotest.how/sdet-start-ru

Примеры тестов разного стиля с и без применения PageObject // https://github.com/yashaka/python-web-test/blob/master/tests/test_search_engines_should_search.py

Примеры более сложных PageObject-ов для контролов и тестов с ними // https://github.com/automician/snippets/tree/master/python/python-selene-for-odoo-crm-examples/framework/model/controls
https://github.com/automician/snippets/blob/master/python/python-selene-for-odoo-crm-examples/tests/test_examples.py

_________________
ровести рефакторинг своего теста на регистрацию студента по форме https://demoqa.com/automation-practice-form, используя инструменты объектно-ориентированной парадигмы для инкапсуляции деталей реализации бизнес-шагов пользователя, таким образом реализовав идеи шаблона PageObject.

Задание состоит из нескольких частей, каждую из которых следует сдавать в виде отдельной ссылки на соответствующую бренчу в репозитории с тестами на приложение demoqa (все ссылки в одном сообщении в комментариях ниже).



ЧАСТЬ I (реализовать в бренче mid-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «заполнение отдельных данных о пользователе» или «подтверждение результата проделанной работы» (как например, подтверждение что регистрация прошла успешно).

Финальный тест должен иметь структуру вида:

registration_page.open()
registration_page.fill_first_name('Yasha')
registration_page.fill_last_name('Kramarenko')
...
registration_page.submit()
registration_page.should_have_registered(yasha)
... или использовав идеи шаблона Fluent PageObject:
registration_page.open()
registration_page \
    .fill_first_name('Yasha') \
    .fill_last_name('Kramarenko') \
    .fill_email('yashaka@gmail.com') \
    ... \
    .submit()
registration_page.should_have_registered('Yasha Kramarenko', 'yashaka@gmail.com', ...)
... или использовав форматирование через круглые скобки вместо \


registration_page.open()
(  
    registration_page
    .fill_first_name('Yasha')
    .fill_last_name('Kramarenko')
    .fill_email('yashaka@gmail.com')
    ...
    .submit()
)
registration_page.should_have_registered('Yasha Kramarenko', 'yashaka@gmail.com', ...)
Другие варианты реализации проверки:

registration_page.should_have_registered(
    student_name='Yasha Kramarenko', 
    student_email='yashaka@gmail.com',
    ...
)
registration_page.should_have_registered(
    ('Student Name', 'Yasha Kramarenko'), 
    ('Student Email', 'yashaka@gmail.com'), 
    ...
)


Дополнительные условия и подсказки:

* Все элементы выносить в отдельные поля объекта класса не обязательно, но стоит это сделать с теми элементами, которые будут повторяться.

* Класс для PageObject должен лежать в выделенном модуле в выделенном пакете внутри проекта, как было показано на уроке 😉



ЧАСТЬ II (реализовать в бренче high-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «отправить форму с данными» или другими словами «провести регистрацию через форму». Также шагом считаем подтверждение результата проделанной работы (как например, подтверждение, что регистрация прошла успешно).



Также в этой части следует провести рефакторинг работы с данными пользователя, представив их в виде объекта датакласса, используя уже имеющиеся знания из предыдущих уроков.



Финальный тест должен выглядеть примерно так:

yasha = User(first_name='yasha', last_name='kramarenko', email='yashaka@gmail.com', ...)
registration_page.open()
registration_page.register(yasha)
registration_page.should_have_registered(yasha)
Допустимо реализовать шаг вида:


registration_page.fill(yasha).submit()
Допустимо предопределить пользователя для тестов в отдельном модуле users.py и в тесте либо использовать напрямую:
registration_page.open()
registration_page.register(users.student)
registration_page.should_have_registered(users.student)
... либо через переменную:

student = users.student
registration_page.open()
registration_page.register(student)
registration_page.should_have_registered(student)


Дополнительные условия и подсказки:

* Не обязательно на уровне с высокоуровневыми шагами типа .register(user) добавлять в PageObject средне-уровневые шаги типа .fill_email(user.email), но можно

  * если их добавлять – это будет сделать не сложно, просто скопировав из предыдущей версии решения из Часть I, – то возможно их стоит сделать "приватными" (добавив перед именем подчеркивание), чтобы не дать возможность в тесте – миксовать подход, а использовать только высокоуровневые шаги, но можно и не вводить такое ограничение.

  * вероятно, проще вместо добавления таких средне-уровневых шагов из Часть I – добавить в init поля объекта для всех элементов и переиспользовать их внутри реализации .register(user). Таким образом реализация будет более лаконичная и все еще достаточно гибкая, чтобы в будущем иметь доступ к элементам в контексте других "бизнес задач" на этой странице.

* Классы для PageObject и модели данных должны лежать в выделенных модулях в выделенных пакетах внутри проекта, как было показано на уроке 😉

* При реализации модели данных для реализации тех или иных полей будет неплохо использовать специальные типы данных, например, для даты использовать datetime.date, а для хобби использовать Enum 😉 





Часть III – ДОПОЛНИТЕЛЬНО/НЕ-ОБЯЗАТЕЛЬНО (реализовать в бренче application-manager)

* добавить в проект тест на упрощенную регистрацию через форму https://demoqa.com/text-box  и соответствующий PageObject. 

  * Реализовать шаблон ApplicationManager для предсоздания всех объектов для пейдж-обджектов.

  * в тесте загрузить форму не через simple_registration_form.open(), а через app.left_panel.open_simple_registration_form(), который должен быть шорткатом (методом, вызывающим под капотом другой метод этого же объекта) на app.left_panel.open('Elements', 'Text Box')

    * cоответственно добавить пейджобджект для LeftPanel и создать его объект в виде поля обьекта апликейшен-менеджера
 
~~~~~~~~~~

python_10_11

~~~~~~~~~~
Урок // https://www.youtube.com/watch?v=mjlrTdwQ_pY
Репо // https://github.com/yashaka/selene-in-action/tree/py05-lesson-configuration-management-with-pydantic

Вводный урок к этому: «Базовое управление конфигурацией через переменные среды». // https://www.loom.com/share/a3657e6a84b94fcda1a1b94e5c0a97d4
Стоит посмотреть перед началом просмотра этого урока

Кодекс Python // https://peps.python.org/pep-0020/
О консистентности в именах // https://tonsky.livejournal.com/304954.html?
Менее универсальная альтернатива для Pydantic - Pytest options (не рекомендуется к использованию для конфигурации проекта, но знать стоит) // https://docs.pytest.org/en/6.2.x/example/simple.html?highlight=pytest%20option#pass-different-values...
Пример проекта с более приближенной к реальности конфигурацией // https://github.com/yashaka/python-web-test
Примеры разных конфигураций драйвера для Selene, в том числе используемые pydantic или dotenv, или и то и то вместе // https://github.com/yashaka/selene/tree/master/examples


Пример рефакторинга с целью создания своей собственной версии Pydantic: 


Теория: 

 – Python Descriptors: An Introduction // https://realpython.com/python-descriptors/

 – Python Dataclasses from Scratch // https://xavd.id/blog/post/python-dataclasses-from-scratch/

Практика:

– шаг 1  // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_web_chrome_with_options_for_selenoid/test_todomvc.py

– шаг 2 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_android_chrome_with_options_for_browserstack/test_todomvc.py

– шаг 3 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_ios_safari_with_options_for_browserstack/test_todomvc.py

– шаг 4 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_android_app_with_options_for_browserstack/version_1__original_selene_browser_style/test_wikipedia.py

– шаг 5 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_android_app_with_options_for_browserstack/version_4__app_fixture_style/test_wikipedia.py

Библиотека для явных ожиданий (не только для веба, а например для конекшена к базе данных) // https://github.com/rockem/busypie

~~~~~~~~~~

____________
Разбор дз // https://www.youtube.com/watch?v=sGVRpOTHKtA

____________
python_10_12

~~~~~~~~~~
Урок https://www.youtube.com/watch?v=jmHvqLD0FHA

Ссылка на Jenkins  // https://jenkins.autotests.cloud/login?from=%2F

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_9_jenkins/tree/demoqa
Ссылка на Jenkins simple // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_9_jenkins_simple%2F
Ссылка на Jenkins demoqa // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_9_jenkins_demoqa

Конспект лекций // https://github.com/qa-guru/knowledge-base

______

ДЗ
1. Взять свой код для http://demoqa.com/automation-practice-form
2. Добавить аттачи для Allure – скриншот, page source, console.log и видео
3. Cделать сборку в Jenkins

В качестве ответа нужно приложить ссылку на Allure-отчет в Jenkins (с видео)
~~~~~~~~~~

__________

РАЗБОР Дз по pageobject // https://www.youtube.com/watch?v=2QGnf_WlVbE

Рекомендации и общепринятые договоренности в подборе имен (Python) // https://autotest.how/sdet-start-ru
Stop Writing Classes // https://www.youtube.com/watch?v=o9pEzgHorH0
__________

python_10_13

~~~~~~~~~~
Lesson // https://www.youtube.com/watch?v=syPeao2M8TQ

Ссылка на репозиторий // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_1_9_jenkins%2F
Ссылка на jenkins // https://github.com/qa-guru/qa_guru_python_1_9_jenkins/

___________

Home task
1. Доработать свой код на регистрационную форму с аллюровскими степами

2. Доработать код, чтобы он запускался не локально, а браузер в selenoid.autotests.cloud

3. Добавить аттачменты - скриншот, логи консоли, page source, видео

4. Сделать сборку в jenkins.autotests.cloud (регистрация открыта) с кодом

5. Передать из дженкинса адрес удаленного браузера

6. Спрятать логин/пароль к удаленному браузеру в .env файл
~~~~~~~~~~

_________

Q&A сессия к занятиям PageObjects и Configuration Management // https://www.youtube.com/watch?v=c2yaYmFlu3E

~~~~~~~~~~
– The Practical Test Pyramid // https://martinfowler.com/articles/practical-test-pyramid.html

– Раздел «Classical Inheritance is Obsolete» из книги Эрика Элиотта  https://www.oreilly.com/library/view/programming-javascript-applications/9781491950289/ch03.html
– Доклад Эрика Элиотта  // https://vimeo.com/69255635

Цитаты: «Inheritance hierarchies are trouble: inflexible, tightly coupled (child HAS TO KNOW IMPL of parent class), non-natural», «e.g. you have Tools and Weapons that you designed for war context. Maybe you can reuse them for "tactical training" but you probably can't build a "Clue board game" with them ;)»

– Статья о Why you should not use SetUp and TearDown // https://jamesnewkirk.typepad.com/posts/2007/09/why-you-should-.html

– SDET Engineer Skills Upgrade Programm // https://docs.google.com/document/d/1yf6-uhTIM2jpHa9NfoFHAJgKucuqwkH_XhSzuwjwcQQ/edit

~~~~~~~~~~
__________



python_10_14

~~~~~~~~~~
Lesson // https://www.youtube.com/watch?v=ZbpwaZJrQt8

– Репозиторий с кодом // https://github.com/qa-guru/qa_guru_python_9_jenkins
– https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_9_jenkins_notifications/2/allure/
– https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_9_jenkins_notifications_positive

Бот с уведомлениями // https://github.com/qa-guru/allure-notifications
Wiki // https://github.com/qa-guru/allure-notifications/wiki
Конспект лекций // https://github.com/qa-guru/knowledge-base
____________

Задание
1. Создайте проект с любыми автотестами, либо возьмите уже созданный.
2. Создайте задачу в Jenkins.
3. Зарегистрируйте бота в Telegram, создайте чат и добавьте бота в него. 
4. Добавьте бота к вашему проекту.
Для выполнения домашнего задания нужно приложить скриншот из телеграм-чата с нотификацией о прохождении автотестов в поле ответа.
~~~~~~~~~~

__________

Дополнительное занятие. Логирование шагов и Декораторы. Яков Крамаренко // https://www.youtube.com/watch?v=DeJYgj86Nd4
Репо // https://gist.github.com/yashaka/0cb814a5de49f4dc91a3a8528bf0d6e7

__________
python_10_15

~~~~~~~~~~
15. Учимся быстро разрабатывать готовые проекты для тестовых заданий. Васенков Станислав
Набиваем руку небольшими проектами.
1. Находим интересную нам вакансию (hh.ru / linkedin / @qa_jobs)
2. Делаем небольшой проект:
– разрабатываем 5-10 простых автотестов на сайт из вакансии,
  – создаем задачу в Jenkins,
– прячем секретные данные (должны быть вынесены в отдельный файл / конфиг сборки в Jenkis)
– настраиваем Allure-отчет, добавляем вложения:
– снимки экрана,
– логи браузера,
– видеозапись теста,
– тест-план Allure TestOps - с ручными и автоматизированными тестами
– интеграцию с Jira
– настраиваем нотификацию в Telegram / Slack.

По мере прохождения курса добавим сюда:
– автотесты на API
3. Отправляем наш проект HR c сопроводительным письмом

Lesson // https://www.youtube.com/watch?v=tF0K813nH6I

Ссылка на репозиторий // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_8_full_project%2F

Конспект лекций // https://github.com/qa-guru/knowledge-base

Доступы к сервисам

https://jira.autotests.cloud/
jira8 jira8
https://allure.autotests.cloud
allure8 allure8




Полезные ссылки: 

– https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_10_jenkins_full_project/
– https://allure.autotests.cloud/launch/36279
– https://jira.autotests.cloud/browse/HOMEWORK-1139


Оформляем README.md
Необходимо посмотреть дополнительное занятие - Дополнительное занятие. Станислав Васенков. «GitHub. Readme / Markdown»


Обязательно должны быть:
- Команды запуска тестов из терминала с пояснением ключей
- История со скриншотами - где что происходит, запускается
- Гифка с тестом (из видео в selenoid)
- Иконки используемого стека для красоты

Дополнительное занятие. Даниил Шатухин. «Оформляем README профиля на GitHub» // https://www.youtube.com/watch?v=r52XllO_3TQ

Дополнительное занятие. Даниил Шатухин. «Рисуем диаграммы с помощью Mermaid.js и Markdown» // https://www.youtube.com/watch?v=uJuskThFWW8

__________

Задание
1. Выберите вакансию 

2. Напишите на неё автотестов:

- 5-10 простых. Главное – не тратьте на это много времени!

- Тесты должны проверять основную логику приложения (регистрация, аутентификация, поиск, добавление/удаление товара из корзины, оформление заказа и др.)

- Использование параметризованных тестов не запрещается, но вся работа НЕ должна состоять из одного большого теста с параметрами (в случае, если тесты могут быть объединены в один параметризованный тест, то все подходящие тесты будут засчитываться как один).

3. Сделайте джобу в Jenkins, добавьте Allure отчёт, уведомления в чат Telegram, Selenoid.

4. Оформите всё со скриншотами в readme.md



В поле ответа на задание приложите: ссылку на джобу в Jenkins, репозиторий с тестами на github, скриншот письма рекрутёру.

Если вы не находитесь в поиске работы, просто сбросьте всё вышеуказанное на ревью. 
~~~~~~~~~~

python_10_16

~~~~~~~~~~
16. Pytest. Сергей Хомутинин. Занятие в записи
1. Аргументы запуска. Собираем фикстуры, марки и другую полезную информацию для отладки
2. Марки. Пропускаем тесты правильно
3. Параметризация. На тесте, на фикстуре. Переопределение параметров

Lesson // https://www.youtube.com/watch?v=g9y0nh2IpeM

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_5_15

How to parametrize fixtures and test functions // https://docs.pytest.org/en/7.1.x/how-to/parametrize.html

Запись с занятия. Часть II // https://www.youtube.com/watch?v=RHO9FGOxWOg

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_5_15_p2

Полезные ссылки
https://github.com/pytest-dev/pytest/issues/3261#issuecomment-369740536
https://pytest-xdist.readthedocs.io/en/latest/how-to.html

Решение проблемы с session-scope фикстурами при параллельном тестировании // https://pytest-xdist.readthedocs.io/en/latest/how-to.html#making-session-scoped-fixtures-execute-only-once

Хуки в документации  // https://docs.pytest.org/en/7.2.x/reference/reference.html#hooks

Конспект лекций // https://github.com/qa-guru/knowledge-base

________
Задание
- Реализовать автотест для github.com, который заходит на страницу, ищет кнопку Sign In, и нажимает на нее (авторизоваться не нужно);

- Параметризовать тест различным размером окна браузера;

- Обратите внимание, что для мобильной версии сайта потребуется другой автотест из-за изменения структуры локаторов;

- Сделайте два варианта пропуска неподходящих параметров и тестов.

1. Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот);

2. Переопределите параметр с помощью indirect;

3. Сделайте разные фикстуры для каждого теста.

В чем преимущества и недостатки каждого из подходов?

~~~~~~~~~~

python_10_17
~~~~~~~~~~
17. Selenoid. Роман Орлов. Занятие в записи
1. Практика. Добавляем контейнеризацию к задаче в Jenkins
2. Теория. Основы Docker. Selenoid

lesson // https://www.youtube.com/watch?v=wkKbPyF2akc

Ссылка на репозиторий // https://github.com/qa-guru/selenoid-web-mobile-starter

Конспект лекций // https://github.com/qa-guru/knowledge-base

https://github.com/fote/selenium-examples/tree/master/python

Установить Docker 

https://docs.docker.com/engine/install/

Установить Selenoid

https://aerokube.com/cm/latest/

Установить Ggr

https://aerokube.com/ggr/latest/

Готовый образ под браузер Safari

https://hub.docker.com/r/browsers/safari

Готовый образ под браузер EDGE

https://hub.docker.com/r/browsers/edge

Готовый образ под Android для тестирования .APK

https://hub.docker.com/r/selenoid/android/tags?page=1&ordering=last_updated

Готовый Android образ с предустановленным Chrome x86 

https://hub.docker.com/r/selenoid/chrome-mobile/tags?page=1&ordering=last_updated

Статья Selenium: Back to the Moon

https://blog.aerokube.com/selenium-back-to-the-moon-6ea73f1657cc

Статья Selenium on Windows: Docker Revolution

https://aandryashin.medium.com/selenium-on-windows-docker-revolution-f5a7eab205ad

Александр Андряшин билд и Dockerfile для Windows браузеров

https://github.com/aerokube/windows-images

Telegram Aerocube

https://t.me/aerokube

Selenoid QA.GURU

https://selenoid.autotests.cloud/#/

Образы

https://hub.docker.com/

Как создаются образы

https://github.com/fote/dockerfile-example/blob/main/Dockerfile

Установка

https://www.docker.com/products/docker-desktop

Презентация Docker


Презентация Selenium

~~~~~~~~~~

python_10_18

~~~~~~~~~~
18. Venv, Poetry и управление зависимостями проекта. Сергей Хомутинин. Занятие в записи
1. Поговорим подробнее о virtualenv и requirements.txt
2. Рассмотрим Poetry в качестве альтернативы, чем он лучше и какие задачи решает
3. Разберем файл pyproject.toml

lesson // https://www.youtube.com/watch?v=DvLUQp-h6Y0

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_4_17

Конспект лекций // https://github.com/qa-guru/knowledge-base

virtualenv // https://virtualenv.pypa.io/en/latest/index.html
Официальные инструменты для управления зависимостями // https://github.com/pypa

Poetry // https://python-poetry.org/

pyproject.toml // https://peps.python.org/pep-0621/

Управляем питонами // https://github.com/pyenv/pyenv

Задание
Создайте проект, используя poetry. Заполните минимальную мета-информацию в pyproject.toml

В зависимостях должны быть: pytest, selene

В dev-зависимостях должен быть pylint

~~~~~~~~~~

python_10_19

~~~~~~~~~~
19. REST API. Часть I. Александр Котляр
1. Практика. Пишем тесты на REST API при помощи библиотеки Requests
2. Теория. Основы HTTP протокола, типы запросов, коды ответов

lesson // https://www.youtube.com/watch?v=FiT8fkkQajY

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_10_19

Конспект лекций // https://github.com/qa-guru/knowledge-base

Дополнительная информация

Методы HTTP запроса  // https://developer.mozilla.org/ru/docs/Web/HTTP/Methods

Коды ответа HTTP // https://developer.mozilla.org/ru/docs/Web/HTTP/Status

Структура HTTP запроса // https://developer.mozilla.org/ru/docs/Web/HTTP/Messages

Документация по requests // https://requests.readthedocs.io/en/latest/

________
Задание
Написать API-тесты:

1. на каждый из методов GET/POST/PUT/DELETE ручек reqres.in

2. Позитивные/Негативные тесты на одну из ручек.

3. На разные статус-коды 200/201/204/404/400

4. На разные схемы (4-5 схем)

5. С ответом и без ответа
Дополнительно со * : 
6. На бизнес-логику (заметить какую-то фичу и автоматизировать, как делали на уроке)
Автотесты должны иметь говорящее название, которое будет понятно человеку не глядя в код.
~~~~~~~~~~

python_10_20
~~~~~~~~~~
20. REST API. Часть II. Александр Котляр
1. Логирование шагов API в Allure
2. Декомпозиция UI теста на API

lesson // https://www.youtube.com/watch?v=PjHaHY5jFu8

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_10_19

Конспект лекций // https://github.com/qa-guru/knowledge-base

______

Задание
1. Написать несколько тестов на demoshop на добавление товаров в корзину через API с проверкой корзины через UI.
2. Автоматизировать у себя в коде логирование в allure.
3.* Сделать,  чтобы в allure логировался request не только json, но и text, и None, если ответ пришел не в json.
4.* Реализовать логирование всех requests одним единым методом
~~~~~~~~~~

python_10_21
~~~~~~~~~~

21. Мобильная автоматизация #1. Разрабатываем автотесты с Browserstack. Станислав Васенков и Яков Крамаренко.
1. Практика. Учимся пользоваться инспектором в Browserstack, разрабатываем первые автотесты на Android / iOS с Selene
2. Практика. Browserstack-API. Забираем логи, видео
3. Теория. Основы тестирования мобильных приложений

lesson // https://www.youtube.com/watch?v=1R1lwEUsSHo
Дополнительный материал от Якова Крамаренко. «Улучшение отчета Allure и получение записи видео из Browserstack» // https://www.youtube.com/watch?v=4G-L9nBnfFQ

Исходники:

- начальный код из урока https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-1-initial

- финальный код из основной части урока (без хелперов для этача видео & Co в Allure отчет) https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-1-pre-final

- финальный код из дополнительной частью урока  (с настройкой отчета Allure и этача видео & Co) https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-1-final-with-more-allure-steps-n-attachments

- финальный код из предыдущей версии этого урока для первых потоков на курсе: https://github.com/qa-guru/mobile-tests-13-py/tree/demo-selene-appium-with-browserstack-android


Основные ссылки:

- Страничка «Get Started» на браузерстек (выбирать язык Python): https://app-automate.browserstack.com/dashboard/v2/quick-start/get-started

  - пример использовать не из нее, а с гитхаба по ссылке: https://github.com/browserstack/python-appium-app-browserstack/blob/master/android/browserstack_sample.py

- Дешбоард на браузерстек: https://app-automate.browserstack.com/dashboard/v2

- Инспектор на браузерстек: https://app-live.browserstack.com

- Как загрузить свою версию апки в браузерстек:
https://github.com/qa-guru/mobile-tests-13-py/tree/demo-selene-appium-with-browserstack-android#how-...

- Откуда скачать последнюю версию апки Wikipedia под android? - https://github.com/wikimedia/apps-android-wikipedia/releases

  - чтобы работал тот же тест с этой версией апки, вероятно, придется дописать дополнительную опцию (капабилити): 'appWaitActivity': 'org.wikipedia.*'

- Официальные примеры Selene для запуска на разных платформах: https://github.com/yashaka/selene/tree/master/examples

Конспект лекций

__________
Задание
- Зарегистрировать аккаунт в https://browserstack.com

- Запустить автотест из занятия локально

- Разработать еще один автотест на открытие любой статьи(статья не будет отображена на browserstack(отображена будет ошибка), вам нужно реализовать только клик на то что вы ищите). Если хотите чтобы статью было видно, нужно залить свою апк википедии и работать с ней

-* Разработать еще один автотест на iOS

-* Адаптировать conftest.py для работы с двумя типами платформ - Android, iOS

-* Вынести данные (логин, пароль, урл браузерстека и т.д.) в .env с pydantic

- Сделать сборку в дженкинсе
В качестве ответа на домашнее задание нужно прислать ссылку на репозиторий в гитхаб и аллюр-отчет в дженкинс
~~~~~~~~~~

python_10_22

~~~~~~~~~~
22. Мобильная автоматизация #2. Разрабатываем автотесты с эмулятором Android-устройства и на своем телефоне. Занятие в записи
1. Настраиваем рабочее место:
– Устанавливаем Android Studio
– Устанавливаем Appium Server, Appium Inspector
– Настраиваем переменные среды
2. Эмулируем Android устройство
3. Подключаем свой телефон
4. Практика. Разрабатываем автотесты с Appium
5. Теория. Основы Appium

lesson // https://www.youtube.com/watch?v=JdjL6h3NpLA

Конспект инструкций по настройке системы и устройств для локального запуска мобильных тестов на платформе Android // file:///Users/evgeniy.l/Downloads/appium-setup-for-local-android-tutorial-md.html

Исходники:


- начальный код из урока https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-2-initial

- финальный код из основной части урока https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-2-final


Дополнительно ⬇️

Пример реализации более сложной логики для этачей в Аллюр репорт, когда мы не всегда этачим скриншоты, например, а только в случае, если тест упал, чтобы сэкономить место, например: https://www.loom.com/share/d3ca893054be4566a28a2b3f8912408d

Доклад Игоря Балагурова о кросс-платформенных тестах – 

«Don’t repeat yourself: UI-тесты для веб, iOS и Android одновременно» https://www.youtube.com/watch?v=YoMt08OcxMI

Конспект лекций // https://github.com/qa-guru/knowledge-base

__________
Задание
1. Настроить систему для работы с устройствами на Android – реальными + эмуляторами (инструкция).
2. Разработать отдельный тест на getting started (onboarding screen) в приложении википедии - пройти по 4м экранам, на каждом сделать проверку
3. Добавить в config опцию context, по значению которой остальные опции конфига будут загружаться (используя библиотеку python-dotenv) из нужного файла типа .env.context. По итогу должно быть минимум три .env-файла, например: .env.local_emulator, .env.local_real, .env.bstack
4. * Если это не было сделано ранее – именно bstack_userName и bstack_accessKey считывать не из .env.bstack, а из .env.credentials или .env (соответстенно именно эти файлы должны быть в .gitignore)
5. * Если это не было сделано ранее – отрефакторить реализацию config.py на использование pydantic

~~~~~~~~~~

__________
Разбор домашних заданий по блоку REST API. Александр Котляр. Запись // https://www.youtube.com/watch?v=_83TGidrNIo
__________

python_10_23
~~~~~~~~~~
23. Allure TestOps. Артем Ерошенко. Занятие в записи
1. Знакомство с системой
2. Заведение тест-кейсов
3. Создание первого тест-плана
________________________________
1. Интеграции с Jenkins и Jira
2. Объединение ручных тестов и автотестов в единый тест-план
3. Метрики, графики, углубленное изучение платформы
4. Администрирование
5. Обзор решений и внедренных проектов

lesson // https://www.youtube.com/watch?v=uvK8ayyI_5s

Ссылка на репозиторий // https://github.com/eroshenkoam/allure-pytest-example

Доступ к сервису https://allure.autotests.cloud
allure8 allure8

Доступ к сервису https://jira.autotests.cloud/
jira8 jira8

Конспект лекций // https://github.com/qa-guru/knowledge-base

Доклад от Артема Ерошенко // https://www.youtube.com/watch?v=Q9Q-JhgogTM

__________

Задание
1. Сделать репозиторий Allure Examples

2. На основе него сгенерировать тестовую документацию

3. Настроить запуск из Allure

4*. Найти баг в Allure (ошибка в самом сервисе)

~~~~~~~~~~

python_10_25
~~~~~~~~~~
24. Дипломный проект
1. Подводим итоги по обучению 
2. Получаем задание на диплом - проект c (manual + auto) тестами - Web, Mobile, Api

lesson // https://www.youtube.com/watch?v=31o04zCrfrA

Подключение Allure TestOps и Jira

Доступы к сервисам 

https://jira.autotests.cloud jira8 jira8 

https://allure.autotests.cloud allure8 allure8



Дипломные работы выпускников прошлых потоков:

– https://github.com/tamayotas/litres-project
– https://github.com/AlexD120/Litres_shop
– https://github.com/Y3ll0wman/Ivi_UI_and_mobile_test_framework
– https://github.com/Y3ll0wman/Petstore_api_test_framework
– https://github.com/flowerfrog/litres_test_project

– https://github.com/ponomarev-iv1986
– https://github.com/A-d-am/qa_guru_diploma
– https://github.com/elakovnick24

– https://github.com/elakovnick24/demo-autotest-project-for-vivid

– https://github.com/elakovnick24/demo-spring-boot-api-test

– https://github.com/StanislavDZ

– https://github.com/StanislavDZ/DprojectAPI

Инструкция по проверке дипломов // https://rainbow-spleen-3c9.notion.site/QA-GURU-PYTHON-ff276648b76a4e6b8bb538051ddf6fb4
_____________
Задание
Дипломный проект состоит из 4-х блоков:



1. Большой проект с UI-автотестами

Обязательно должно быть:

- PageObjects



2. Красиво сделаный проект по API с Readme

Обязательно должно быть:

- Модели, как для формирования body в post-запросе, так и для десериализации ответа

- Авторизация (или подготовка данных/сущностей) по Api для UI проекта (в идеале если получится добавить API-тестов в п.1)



3. Красиво сделаный проект по Mobile с Readme;



4. В Allure Testops необходимо также добавить немного ручных тестов;



5. Обновить профиль в гитхабе, в нем можно указать ссылки на все 3-4 проекта



В идеале, если получится объединить 1-4 пункты в рамках одного продукта

Также рекомендуем аналогично доработать CV (резюме) и профили на сайтах поиска работы - linkedin.com, hh.ru и т.п.



В помощь занятие по Github Markdown #1 (шпаргалка // https://github.com/qa-guru/knowledge-base/wiki/Github-README.md) и Github Markdown #2 



Срок сдачи диплома и всех "хвостов" по домашним работам – до 15.05.2024 г. включительно


~~~~~~~~~~

python_10_26
~~~~~~~~~~
25. Переезд на собственную инфраструктуру с ресурсов школы. Егор Иванов. Занятие в записи
Настроим тестовый стенд локально. Точно также стенд настраивается на любом VPS, например в DigitalOcean.com
1. Рассмотрим базовые команды Linux, которые понадобятся
2. Доступ к удаленному серверу через ssh Ubuntu
  2.1 Доступ к Ubuntu через ssh при помощи публичного RSA ключа
3. На виртуальной машине установим:
  3.1 Python
  3.2 Docker
  3.3 Docker-compose
4. Создаем конфиг для docker-compose
5. Поднимаем Selenoid + Selenoid UI
  5.1 Проверяем, как это работает
6. Поднимаем Jenkins
  6.1 Первичные настройки Jenkins
  6.2 Проверка работоспособности
Задание не обязательное.

lesson // https://www.youtube.com/watch?v=pW0WaCsYTG4

Ссылка на репозиторий // https://github.com/cheshi-mantu/cm-jenkins-selenoid-python-testbed

Конспект лекций // https://github.com/qa-guru/knowledge-base

Тестовый стенд на WSL2 (Windows) // https://github.com/cheshi-mantu/cm-local-test-bed-wsl
Тестовый стенд внутри VirtualBox // https://github.com/cheshi-mantu/qa-local-test-bed

настройка стенда на впс // https://qaguruschool.getcourse.ru/pl/fileservice/user/file/download/h/2eabd500becdd220c87b8e26de567946.pdf

~~~~~~~~~~

python_10_27
~~~~~~~~~~
Дополнительное занятие. Стабильные тесты на чистом Selenium Webdriver c помощью явных ожиданий. Яков Крамаренко. Запись

lesson // https://www.youtube.com/watch?v=SmELu4tkw1E

reposit link // https://github.com/qa-guru/selenium-webdriver-wrapper

________

Задание
#0
Повторить код из урока, возможно коректируя селекторы (можно выбрать более удобный для себя поисковый движок, типа ecosia.org, duckduckgo.com, и т.д.). Можно подобрать свое имя для фреймворка. Потом выберем лучшее имя 😉
Сохранить проект в гит-репозитории в отдельной бренче refactoring-selenium-stage-0


#1
Отрефакторить рабочий код от версии

driver.get('https://ecosia.org')
query='[name=q]'
wait.until(type(query, value='selene' + Keys.ENTER))
driver.back()
wait.until(type(query, value=' yashaka' + Keys.ENTER))
wait.until(click('[data-test-id=mainline-result-web]:nth-of-type(1) a'))
wait.until(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))
driver.quit()
до версии

driver.get('https://ecosia.org')
query='[name=q]'
type(query, value='selene' + Keys.ENTER)
driver.back()
type(query, value=' yashaka' + Keys.ENTER)
click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4)
driver.quit()
и сохранить результат в git-репозитории в отдельной бренче c именем: refactoring-selenium-stage-1

#2
Далее отрефакторить к версии:

from seleyasha import browser
# where browser is seleyasha/browser.py
browser.open('https://ecosia.org')
query='[name=q]'
browser.type(query, value='selene' + Keys.ENTER)
browser.back()
browser.type(query, value=' yashaka' + Keys.ENTER)
browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
browser.assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4)
browser.quit()
и сохранить результат в git-репозитории в отдельной бренче c именем: refactoring-selenium-stage-2

#3
Далее отрефакторить к версии:

from seleyasha.browser import Browser
# where browser is seleyasha/browser.py
browser = Browser(driver)
browser.open('https://ecosia.org')
query='[name=q]'
browser.type(query, value='selene' + Keys.ENTER)
browser.back()
browser.type(query, value=' yashaka' + Keys.ENTER)
browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
browser.assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4)
browser.quit()
и сохранить результат в git-репозитории в отдельной бренче c именем: refactoring-selenium-stage-3


Как решение заданий – прислать 4 ссылки на соответствующие бренчи.

~~~~~~~~~~

python_10_28
~~~~~~~~~~
Дополнительное занятие. Фреймворк на Selenium Webdriver – лучшие встроенные ожидания и ленивые элементы. Яков Крамаренко. Запись
lesson // https://www.youtube.com/watch?v=WEZ3IHZ9yzI

#0 Исходный код – «Чистый вебдрайвер с явными ожиданиями до кастомных команд и условий для проверок» // https://github.com/qa-guru/selenium-webdriver-wrapper/tree/refactoring-selenium-stage-0-explicit-waits-for-custom-commands-n-conditions

#1 Рефакторинг –  «Высокоуровневые ждущие команды и проверки» // https://github.com/qa-guru/selenium-webdriver-wrapper/tree/refactoring-selenium-stage-1-built-in-waits-with-improved-errors

#2 Рефакторинг – «Высокоуровневый API для браузера с помощью инструментов Модульной Парадигмы» // https://github.com/qa-guru/selenium-webdriver-wrapper/tree/refactoring-selenium-stage-2-browser-api-modular-style

#3 Рефакторинг – «Высокоуровневый API для браузера с помощью ООП» // https://github.com/qa-guru/selenium-webdriver-wrapper/tree/refactoring-selenium-stage-3-browser-api-oop-style

#4 Рефакторинг – «Конфиг для браузера и еще больше ООП для флуэнт стиля ленивых элементов для шаблона PageObject» // https://github.com/qa-guru/selenium-webdriver-wrapper/tree/refactoring-selenium-stage-3-browser-api-oop-style

____________
Задание
Повторить код из урока.



#4.1 ... получив сначала версию (cохраненную в бренче refactoring-selenium-stage-4-1) вида:

from seleyasha.browser import Browser
# where browser is seleyasha/browser.py
browser = Browser(driver, Config(timeout=4.0, base_url='https://ecosia.org'))
browser.open('/')
query=browser.element('[name=q]')
query.type('selene').press_enter()
browser.back()
query.type(' github issues').press_enter()
browser.element('[data-test-id=mainline-result-web]:nth-of-type(1) a').click()
'''
# при этом старая версия API все еще должна работать:

browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
'''
browser.all('[id^=issue_]:not([id$=_link])').assert_amount(25)
browser.quit()


#4.2 ... потом получив версию (cохраненную в бренче refactoring-selenium-stage-4-2) вида:

from tests.model import web

web.ecosia.open()
web.ecosia.query.type('selene').press_enter()
browser.back()
web.ecosia.query.type(' github issues').press_enter()
web.ecosia.first_result_link.click()
web.github_issues.links.assert_amount(25)
browser.quit()
#4.3 Далее убери «старую» версию API вида browser.command(selector, *value)

Реализация всех команд и проверок над элементом и коллекцией элементов – должны быть перенесены в соответствующие классы Element и Collection. 

То есть, из двух стилей API:

browser.element('[data-test-id=mainline-result-web]:nth-of-type(1) a').click()
# OR
browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
– должен остаться только первый 😉

Сохрани решение в отдельной бренче с именем refactoring-selenium-stage-4-3

#4.4 Расширь набор команд для Element, Collection, Browser, Config

Написать тест на страницу https://the-internet.herokuapp.com/hovers проверяющий появление подписи по наведению мышки на аватарку и соответственно ее исчезновение при наведении на следующую. Важное условие и ключевая подсказка – полноценный тест должен проверять одновременно коллекцию всех подсказок под всеми тремя аватарками (то есть нужны проверки именно над коллекцией элементов а не одним элементом). 

Написать тест на страницу https://the-internet.herokuapp.com/context_menu проверяющий срабатывание правого клика мыши по соответствующей области.

Добавить в Config опцию quit_browser_on_exit управляющую автоматическим закрытием браузера по завершению работы python процесса. По умолчанию опция должна быть «отключена». Далее - удали из тестов browser.quit() и в настройке браузера – «включи» соответствующую опцию. Подсказка: используй функцию register из стандартного python-модуля atexit для «регистрации» во время инициализации браузера – вызова соответствующего метода для закрытия.

Сохрани решение в отдельной бренче с именем refactoring-selenium-stage-4-4
~~~~~~~~~~

Дополнительное занятие. Разбор вопросов на интервью по Selenium WebDriver. Яков Крамаренко. Запись
~~~~~~~~~~
О Selenium, его локаторах, вейтах и execute_script // https://www.loom.com/share/af46c0e8d35f4bfab0783b30a56d4ee8

is_element_present и работа с динамическими таблицами в Selenium + Python // https://www.loom.com/share/774416dc80a94b6aa4cab80a2e6287a9

Selenium Grid, варианты click и send_keys в Selenium // https://www.loom.com/share/c93fc3a8bd274ee397ad6dd51af6f419

Что такое Appium + немного о Grid // https://www.loom.com/share/562ca1289539479398db8d853a6f8a4e

~~~~~~~~~~

Дополнительное занятие. Разрабатываем автотесты с Python/Pytest/Playwright. Иван Тебеньков
~~~~~~~~~~
lesson // https://www.youtube.com/watch?v=A4bfFwbOVtU


– https://playwright.dev/python/
– Andrey Lushnikov — Playwright: Web testing without drama // https://www.youtube.com/watch?v=ttODF00XWis
~~~~~~~~~~

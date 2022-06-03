# it_company_card

Тестовые задания для кандидатов на должность 
разработчика Python\Django (Бэкенд)
Необходимо разработать сайт визитку для IT компании. Сайт должен иметь следующий контент:
    1. Сайт должен иметь верхнее меню(модель Меню), по которым можно переходить на другие страницы(Создать элементы: Главная, Услуги, Новости, Отзывы, Контакты)
    ---2. НА главной странице должны выводиться 2 баннера(В админке можно использовать галку активны/показывать на главной), 3 последних новости и 3 услуги(Галка показывать на главной)
    ---3. Страница услуг должна выводить список категорий услуг. При Переходе в категорию на странице должны выводиться подкатегории, и если есть товары то список товаров. Также должен быть реализован справочник акций. На шаблоне должен быть выведен BreadCrumbs.
    ---4. Модель категория должна иметь аттрибуты:
        a. Название
        b. Родительская категория
        c. Картинка
        d. Ссылка
        e. Удалено
    ---5. Модель Товара должна иметь аттрибуты:
        a. Название
        b. Категория
        c. Картинка
        d. Ссылка
        e. Описание
        f. Характеристики
        g. Цена
        h. Действующие акции
        i. Удалено
    ---6. На сайте должны быть кнопки авторизации и регистрации, с переходом на соответствующие страницы с соответствующими формами.
    ---7. Страница отзывов должна выводить опубликованные отзывы пользователей о компании, сортированыых по дате создания(от новых к старым). Форма оставить отзыв должны быть доступна авторизированным пользователям. При сохранении отзыва в моделе должен сохраняться тот пользователь, который его оставил. При выводе на странице выводить информацию: кто оставил отзыв, дата создания отзыва, сообщение. Также у отзыва должны быть следующие статусы: Опубликован, На модерации, Отклонен. 
    ---8. Страница новостей должна выводить новости сортированные по дате создания. Также на странице должен присутствовать фильтр по дате создания новостей(дата от, дата до, при применении фильтра должны отображаться новости в этом интервале дат. У каждой новости должна отображаться следующая информация: Дата новости, картинка, название, короткое описание(20 символов). При клике на новость должен осуществляться переход на детальную страницу новостей.
    ---9. Страница контакты должна содержать форму обратной связи, и контент отображающий контактную информацию компании. 
На бэке форма должна проходить валидацию(Правильный формат телефона, правильная запись e-mail, не пустые поля 
имени и сообщения). После отправки формы она должна сохраняться в соответствующую модель и отправляться 
уведомление с ссылкой администраторам сайта. Также форма должна иметь поле капчу(Гугл, django-captcha и т д.)
    10. Футер сайта должен состоять из элементов меню, которые пометили как «Показывать в футере»
    11. Любой объект в системе не должен удаляться. При удалении объекта из админки должна проставляться галочка «Удален»
    ---12. В админке для каждой модели должен быть осуществлен фильтр по полю удалено, а также поиск по названию.
    ---13. Модель товаров в админке не выводить, выводить товары при переходе на редактирование категории.
Требования к решению:
    • Программный код должен быть размещен в открытом Git-репозитории.
    • Оформлением (css, js) можно пренебречь. Выводить голый текст или скачать оформление с каких-нибудь сайтов визиток.
    • Рабочая версия приложения должна быть размещена в открытом доступе. Например, с использованием хостинга https://www.pythonanywhere.com/ или путем «прокидывания» доступа к локально запущенной версии с помощью сервиса https://ngrok.com/ или любым другим вариантом, который позволит посмотреть приложение в действии удаленно.
    • Серверная часть должна быть реализована на языке Python с использованием фреймворка Django
    • Взаимодействие с БД должно осуществляться с использованием Django ORM.
    • Административная часть должна быть реализована с использованием Django Admin Site.
    • Маршрутизацию запросов сделать с использованием Django URL Dispatcher.
    • Код серверной части должен соответствовать требованиям к оформлению кода: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/.
    • Код серверной части должен проходить проверки flake8 с плагинами flake8-import-order и flake8-docstrings без дополнительных параметров.

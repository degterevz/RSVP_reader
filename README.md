# RSVP_reader
Десктопный текстовый плеер по технологии [RSVP](https://ru.wikipedia.org/wiki/%D0%91%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%B5%D0%B4%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5). Реализован с использованием библиотеки Tk.

<img src="https://raw.githubusercontent.com/degterevz/RSVP_reader/master/sample.jpg">
Интерфейс адаптирован под Windows.

## Запуск

```
python main.py
```
* Загрузите текст из файла ```.txt```, либо через встроенный редактор.

## Функционал

а) Управление плеером осуществляется через соответствующие иконки, либо через клавиатуру.

1. Пробел - старт / пауза.
2. Если нажата пауза стрелки влево/вправо путешествуют вручную по кадрам.
3. Стрелки вверх/вниз увеличивают/уменьшают скорость воспроизведения с шагом step_wpm.
4. [0] - перейти в начало текста.
5. Регулировка wpm через меню. Там же оно и отображается.

в) Дополнение: 
* В рамках текущего запуска программа сохраняет ифнформацию, где завершилось чтение для каждого файла.
* Программа делает небольшую паузу в конце предложения. Задается через 'GV.pause_sentence'
* Программа дополнительно задерживает кадр в зависимости от длины слова.

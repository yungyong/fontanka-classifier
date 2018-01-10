Классификатор новостей
======================

Скачивает и классифицирует новости с [Фонтанки](https://www.fontanka.ru) с 2015 по 2017 гг.

Получение данных
------

* `fetch_news_pages.py` получает все ссылки на новости Фонтанки за указанный временной
период



* `fetch_news.py` скачивает все новости с разделением на категорию, заголовок и собственно новость


Обработка и исследование данных
------

* `clean.py` содержит очистку данных и "ручное" проставление категорий 

  - например, категории "Афиша +", "Книги", "Кино" отнесены к категории "Культура"
  -  общее количество категорий уменьшилось со 118 до 20
  - очистка = стемминг + учет стоп-слов (библиотека `nltk`)

![](https://habrastorage.org/webt/fu/ir/ic/fuiricntameavngdur6pc4uqlgi.png)

![](https://habrastorage.org/webt/d1/yh/iz/d1yhizip4jf0efxkt6mbzyjsqpe.png)

![](https://habrastorage.org/webt/pe/a8/8j/pea88j9pespu48dwtjc5hnysk0s.png)

* `tfidf.py`  транформирует новости в вектора из `10` тыс. признаков
* `PCA.py` уменьшает количество признаков до  `2048` 
    - `variance: 0,629`
    - рассмотрены и другие варианты сжатия: `[1024, 512, 256]` признаков
    
   
Нейронная сеть 
------

* `MLPClassifier (sklearn)` 
* `512` юнитов, `1` слой
* `accuracy: 0,68`

Логистическая регрессия
------

* `LogisticRegression (sklearn)` 
* проверены следующие параметры для `С`: `[0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10]`
* `accuracy: 0,70` при `C = 3`

SVM 
------

* `LinearSVC (sklearn)` 
* `max_iter = 200`
* `accuracy: 0.70` 








































 - Авто
 - Бизнес
 - Благотворительность
 - Власть
 - Выборы
 - Город
 - Деньги
 - Дороги
 - ЖКХ
 - Культура
 - Личная жизнь
 - Недвижимость
 - Общество
 - Происшествия
 - Работа
 - Спорт
 - Строительство
 - Технологии
 - Туризм
 - Финансы


![](https://habrastorage.org/webt/qv/qe/mz/qvqemzk0tcptlogr_oml5chen3y.png)

![](https://habrastorage.org/webt/4b/jk/md/4bjkmdeulayaiahej1_bew0vv3g.png)

![](https://habrastorage.org/webt/6e/bo/bw/6ebobw215gnrvfiv1dcjf0wnbpk.png)

Точность
--------


- Logistic Regression: 0.68 (+/- 0.02)
- Linear SVM: 0.66 (+/- 0.02)
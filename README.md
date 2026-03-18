# Deep Learning in Biology @ HSE FCS

Курс по применению методов **deep** learning в биологии и медицине для студентов ФКН НИУ ВШЭ. [hse](https://www.hse.ru/edu/courses/858163775)

***

## Структура репозитория

Репозиторий организован по типам материалов:

- `lectures/` — pdf‑файлы лекций, общий README по лекциям.
- `seminars/` — ноутбуки и код семинаров, для некоторых тем будут отдельные подпапки с дополнительными материалами.
- `homeworks/` — формулировки домашних заданий и вспомогательные материалы.

***

## Основная информация о курсе

- Университет: НИУ ВШЭ, ФКН. 
- Формат: очные занятия с возможностью подключения онлайн.  
- Старт курса: 27 января 
- Язык курса: русский.  

### Блоки курса

Курс состоит из трёх взаимосвязанных блоков:

1. Биоинформатика и DL в биологии (Андрей Боревский).
2. Physically Informed Neural Networks (Александр Тараканов).  
3. ИИ и новые материалы (Михаил Лазарев).  

Каждый блок имеет собственные акценты в части методов и приложений, но общая линия курса — современные DL‑подходы к анализу биологических и материаловедческих данных. 

***

### План тем (био + DL)

| № | Bio‑темы                                  | DL‑темы                                   | Материалы (Презентация / Семинар)                                                                 | Запись занятия |
|---|-------------------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------------------|----------------|
| 1 | Введение в молекулярную биологию, ДНК     | Введение в DL, мотивация в биологии       | [Лекция 1](lectures/1.DNA.pdf)                                                                    | [Ссылка]()     |
| 2 | –                                         | Основы ML                                  | [Лекция 2](lectures/2.ML.pdf)                                                                     | [Ссылка]()     |
| 3 | –                                         | Основы DL                                  | [Лекция 3](lectures/3.DL.pdf)                                                                     | [Ссылка]()     |
| 4 | Хроматин, транскрипция                    | Модели для последовательностей (обзор)    | [Лекция 4](lectures/4.Chromatine.pdf)                                                             | [Ссылка]()     |
| 5 | Пост‑транскрипция                         | CNN, LSTM для ДНК, mlflow                 | [Лекция 5](lectures/5.Post-Transcription.pdf), [Seminar DNA](seminars/Seminar_I_DNA_classification.ipynb)                                                    | [Ссылка]()     |
| 6 | -                                         | NLP, Attention, Transformers               | [Лекция 6](lectures/6.NLP.pdf)                                                     | [Ссылка]()     |
| 7 | Трансляция                                | CNN XAI, GNN, optuna                      | [Лекция 7](lectures/7.Translation.pdf), [Seminar GNN](seminars/Seminar_2_GNN_for_ZDNA.ipynb)      | [Ссылка]()     |
| 8 | Белки                                     | CV for Med, XAI, mlflow                   | [Презентация](), [Семинар]()                                                                      | [Ссылка]()     |
| 9 | Белки, протеостаз                         | Advanced approaches (contrastive, self‑supervised) | [Презентация](), [Семинар]()                                                             | [Ссылка]()     |
| 10 | Завершение молекулярного блока, med cases | Языковые модели, RL                       | [Презентация](), [Семинар]()                                                                      | [Ссылка]()     |
| 11| Анализ мозга                              | Повторение, диффузионные модели           | [Презентация](), [Семинар]()                                                                      | [Ссылка]()     |
| 12| EEG‑analysis, коллоквиум (extra)          | Дополнительные кейсы                      | [Презентация](), [Семинар]()                    | [Ссылка]()     |

***

## Preliminaries

Раздел для самостоятельной подготовки перед началом (и в процессе) курса. Он помогает выровнять базу по машинному и глубокому обучению, а также освежить ключевые факты по математике и программированию.

### Machine Learning (База)
[Учебник Яндекса по ML](https://education.yandex.ru/handbook/ml/article/linear-models)
[Курс Е.А. Соколова](https://github.com/esokolov/ml-course-hse/tree/master)

### Deep Learning (База)

| Блок | Подтемы | Ссылки на материалы |
|---|---|---|
| **Основы нейросетей** | Линейные слои, полносвязные сети, функции активации | [Лекция ФКН](https://github.com/isadrtdinov/intro-to-dl-hse/blob/2023-2024/lecture-notes/notes-01-mlp.pdf), [Учебник Яндекса](https://education.yandex.ru/handbook/ml/article/nejronnye-seti) |
| **Обучение** | Backpropagation, интуиция и визуализация градиентного спуска | [3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi), [Видео IBM](https://www.youtube.com/watch?v=S5AGN9XfPK4), [Учебник Яндекса](https://education.yandex.ru/handbook/ml/article/metod-obratnogo-rasprostraneniya-oshibki) |
| **Практика PyTorch** | Определение архитектуры модели, цикл обучения, работа с датасетами | [Туториал PyTorch](https://pytorch.org/tutorials/beginner/pytorch_with_examples.html#pytorch-custom-nn-modules) |
| **Регуляризация и слои** | BatchNorm, Dropout, функции активации | [Первый](https://towardsdatascience.com/batch-norm-explained-visually-how-it-works-and-why-neural-networks-need-it-b18919692739?gi=f49f49297ad9) и [Второй](http://vbystricky.ru/2020/05/batch_normalization.html) разбор BN, [Разбор Dropout](https://habr.com/ru/companies/wunderfund/articles/330814/), [Плейлист основ DL](https://youtube.com/playlist?list=PLTl9hO2Oobd-GaTYQWIuIs2yyNy7TYbEj&si=9I95glZquxts92Hm), [Лекция ФКН](https://github.com/isadrtdinov/intro-to-dl-hse/blob/2023-2024/lecture-notes/notes-02-dropout-batchnorm.pdf) |
| **Сверточные сети (CNN)** | Принцип работы свертки, pooling, residual connections | [3Blue1Brown](https://www.youtube.com/watch?v=KuXjwB4LzSA), [Лекция ИАД](https://www.youtube.com/watch?v=Vcz8C8Q-1og), [Лекция ФКН](https://github.com/isadrtdinov/intro-to-dl-hse/blob/2023-2024/lecture-notes/notes-04-convolution.pdf), [Учебник Яндекса](https://education.yandex.ru/handbook/ml/article/svyortochnye-nejroseti), [Residual connections](https://www.youtube.com/watch?v=o_3mboe1jYI) |
| **Работа с последовательностями**| Разбор RNN, LSTM, проблема затухающего градиента, запуск на текстах | [Топ разбор](https://sysblok.ru/knowhow/mama-myla-lstm-kak-ustroeny-rekurrentnye-nejroseti-s-dolgoj-kratkosrochnoj-pamjatju/), [Статья Habr](https://habr.com/ru/articles/567142/), [Видео LSTM](https://www.youtube.com/watch?v=Kv4NyVW9IZ4), [Учебник Яндекса](https://education.yandex.ru/handbook/ml/article/nejroseti-dlya-raboty-s-posledovatelnostyami) |

***

## Навигация по директориям

Рекомендуемая структура вспомогательных README:

- `lectures/README.md`  
  - Список лекций по датам и темам.  
  - Ссылки на соответствующие pdf (`1.DNA.pdf`, `2.ML.pdf`, `BioLecture_UFA.pdf` и т.п.).  
  - Ссылки на записи лекций и дополнительные материалы.

- `seminars/README.md`  
  - Список семинаров с кратким описанием задач.  
  - Ссылки на ноутбуки (`Seminar 0. Transformer.ipynb`, `Seminar_I_DNA_classification.ipynb`, и т.д.).  
  - Описание структуры подпапок семинаров (датасеты, утилиты, скрипты обучения).

- `homeworks/README.md`  
  - Перечень домашних заданий с кратким описанием.  
  - Ссылки на формулировки и starter‑код. 

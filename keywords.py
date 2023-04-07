import math

# создаем словари с данными
data1 = {
    "Стажер": {"Задачи":
                   "1) Подготовка и анализ отчетов\n"
                   "2) Помощь в организации мероприятий\n"
                   "3) Изучение и тестирование новых технологий\n",

               "description": "Аналитическое мышление Организационные навыки Коммуникативные навыки"
               },

    "Младший специалист": {"Задачи":
                               "1) Разработка и тестирование простых программных решений\n"
                               "2) Поддержка и оптимизация существующего программного обеспечения\n"
                               "3) Работа с базами данных и написание SQL-запросов\n",

                           "description": "Знание языков программирования Навыки тестирования Работа с базами данных"
                           },

    "Специалист": {"Задачи":
                       "1) Разработка и тестирование сложных программных решений\n"
                       "2) Развертывание и настройка приложений на серверах\n"
                       "3) Работа с системами управления версиями и автоматизация процессов разработки\n",

                   "description": "Глубокое знание языков программирования Опыт работы с системами управления версиями  Навыки работы с DevOps инструментами"
                   },

    "Старший специалист": {"Задачи":
                               "1) Руководство командой разработчиков и координация процессов разработки\n"
                               "2) Принятие решений по оптимизации и улучшению программного обеспечения\n"
                               "3) Подготовка и анализ отчетов о работе проекта\n",

                           "description": "Экспертиза в определенной области IT Развитие новых стратегий разработки Руководство и менторинг более младших сотрудников"
                           },

    "Ведущий специалист": {"Задачи":
                               "1) Разработка и реализация новых стратегий разработки программного обеспечения\n"
                               "2) Проведение исследований в области IT и выработка рекомендаций по внедрению новых технологий\n"
                               "3) Руководство и менторинг более младших сотрудников\n",

                           "description": "Экспертиза в определенной области IT Развитие новых стратегий разработки Руководство и менторинг более младших сотрудников "
                           },

    "Эксперт": {"Задачи":
                    "1) Разработка и реализация новых технологических решений\n"
                    "2) Анализ проблем и разработка стратегий их решения\n"
                    "3) Помощь остальным сотрудникам\n",

                "description": "Глубокое знание специфических технологий Умение применять новые технологии в работе Аналитические навыки"
                },

}

data2 = {
    "web-приложений": {"description": "JavaScript,Python,Ruby on Rails,React,Angular,Vue.js,Node.js,Django,Flask"},
    "desktop-приложений": {"description": "C++,Java,Python,Electron,Qt,GTK+,WinForms,WPF,Cocoa"},
    "мобильных приложений": {
        "description": "Swift,Kotlin,Java,React Native,Flutter,Xamarin Android Studio,Xcode,Appcelerator"},
    "серверных приложений": {"description": "Java,Python,Ruby,Spring Boot,Django,Ruby on Rails,Apache,Nginx,Tomcat"},
    "встраиваемых систем": {"description": "C,C++,Assembly,Arduino,ARM Cortex,Raspberry Pi,FreeRTOS, mbed, Keil"},
    "системного программирования": {"description": "C,Rust,Assembly,Linux kernel,Windows API,macOS API,GCC,LLVM,Clang"}
}

# создаем список ключевых слов
keywords1 = ["Глубокое", "технологии", "Аналитические"]
keywords2 = ["Python", "Java", "C", "Linux"]

# вычисляем TF-IDF для каждого значения в словаре 1
values1 = []
for key1, value1 in data1.items():
    tf_idf1 = 0
    for keyword in keywords1:
        tf = value1["description"].count(keyword) / len(value1["description"])
        idf = math.log(len(data1) / sum(1 for value1 in data1.values() if keyword in value1["description"]))
        tf_idf1 += tf * idf
    values1.append((key1, tf_idf1))

# вычисляем TF-IDF для каждого значения в словаре 2
values2 = []
for key2, value2 in data2.items():
    tf_idf2 = 0
    for keyword in keywords2:
        tf = value2["description"].count(keyword) / len(value2["description"])
        idf = math.log(len(data2) / sum(1 for value2 in data2.values() if keyword in value2["description"]))
        tf_idf2 += tf * idf
    values2.append((key2, tf_idf2))

# находим наиболее подходящее значение
best_value1 = max(values1, key=lambda x: x[1])[0]
best_value2 = max(values2, key=lambda x: x[1])[0]

# выводим результат
print(f"Наиболее подходящая должность: {best_value1} {best_value2}.\n Задачи:\n{data1[best_value1]['Задачи']:}")

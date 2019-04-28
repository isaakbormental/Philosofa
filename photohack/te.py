# import base64
# import spacy
# # with open("D:\\Education\\Hackathones\\photohack2\\back\\photohack\\uiuiui.jpg", "rb") as image_file:
# #     encoded_string = base64.b64encode(image_file.read())

# # print(encoded_string)




# # Загрузка английской NLP-модели
# nlp = spacy.load('D:\\Education\\Hackathones\\photohack2\\back\\photohack\\en_core_web_lg')

# # Текст для анализа
# text = """London is the capital and most populous city of England and 
# the United Kingdom.  Standing on the River Thames in the south east 
# of the island of Great Britain, London has been a major settlement 
# for two millennia. It was founded by the Romans, who named it Londinium.
# """

# text2 = 'I am stuck in a jam and hate the world'

# # Парсинг текста с помощью spaCy. Эта команда запускает целый конвейер
# doc = nlp(text)

# # в переменной 'doc' теперь содержится обработанная версия текста
# # мы можем делать с ней все что угодно!
# # например, распечатать все обнаруженные именованные сущности
# # for entity in doc.ents:
# #     print("{} {}".format(entity.text, (entity.label_)))


# statements = textacy.extract.semistructured_statements(doc, "London")
 
# # Вывод результатов
# print("Here are the things I know about London:")
 
# for statement in statements:
#     subject, verb, fact = statement
#     print(f" - {fact}")
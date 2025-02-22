class make_dict():
    # определяем класс make_dict

    def __init__(self, line):
        # при инициализации объекта необходимо ввести параметр line, содержащий текст для его дальнейшего форматирования
        self.line = line
        self.list = []
        # объекту присваивается два параметра: line и list


    def _custom_lower_(self):
        # скрытый метод, приводящий строку к нижнему регистру
        line = self.line
        upp_alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        # алфавит заглавных букв кириллицы
        done_line = []
        for let in line:
            if let in upp_alph:
                done_line.append(chr(ord(let) + 32))
                # если буква является заглавной, то она переводится в нижний регистр.
                # Все буквы кириллицы распределены так, что при получении порядкого номера символа в Unicode, заглавные
                # буквы идут на 32 символа раньше их вариантов в нижнем регистре. Этим и воспользуемся для перевода в
                # нижний регистр.
                continue # переход к новой итерации цикла
            done_line.append(let)
        self.line = ''.join(done_line)
        # собираем список всех букв (уже в нижнем регистре) и объединяем их в одну строку с помощью метода join
        return self.line


    def _get_rid_of_(self):
        # скрытый метод, убирающий все знаки пунктуации и переноса строки "\n"
        line = self.line
        punc_marks = '.,:;-()?!'
        # алфавит недопустимых символов пунктуации
        tmp = []
        flag = False
        for let in line:
            if let == "\n":
                tmp.append(' ')
                # если символ является переносом строки, заменяем его на одинарный пробел
                continue # переход к новой итерации цикла


            if let not in punc_marks:
                tmp.append(let)
            else:
                tmp.append(' ')
            # если символа нет в алфавите недопустимых символов, то добавляем этот символ в список, иначе заменяем его
            # на одинарный пробел.
        
        tmp.append(' ')
        # для корректной работы удаления двойных пробелов необходимо в самом конце строки добавить ещё один пробел


        lst = []
        flag = False
        for elem in tmp:
            if elem == ' ':
                if not flag:
                    lst.append(elem)
                flag = True
                continue
                # если символ является пробелом, то мы его добавляем в строку. Если дальше будут встречаться пробелы,
                # то они не будут добавлены, пока не встретится символ, отличный от одинарного пробела
            flag = False
            lst.append(elem)


        self.line = ''.join(lst)
        # объединяем список символов в строку
        return self.line

    def _custom_split_(self, splitter=' ', line='def'):
        # скрытый метод, разбивающий строку по заданному разделителю (по умолчанию это ' ' - одинарный пробел)
        # Метод реализован с помощью рекурсии. В общем его работа описывается так: строка делится по первому
        # встреченному разделителю на две части, первая часть остаётся неизменной (так как там уже точно нет
        # разделителя), а в правой части происходит поиск разделителя. Если разделителя нет или он просто не может
        # поместиться в строку, то возвращаем правую часть без каких-либо изменений.
        splitter = splitter.lower()
        if line == 'def':
            line = self.line
        finder = line.find(splitter)
        if finder == -1:
            return [line]
        f_h, s_h = line[:finder], line[finder + len(splitter):]
        if len(s_h) >= len(splitter):
            s_h = self._custom_split_(splitter, s_h)
        self.list = [f_h, *s_h]
        return self.list


    def _collect_dict_(self):
        # скрытый метод, считающий количество встречаемых слов
        words_dict = dict()
        for word in sorted(self.list):
            # сортируем список всех слов в алфавитном порядке
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
            # если слова ещё нет в словаре, добавляем его, иначе увеличиваем счётчик встречи слова на 1
        return words_dict # возвращаем готовый словарь


    def complete_dict(self):
        # метод, объединяющий все прочие методы класса и возвращающий готовый словарь
        self._custom_lower_()
        self._get_rid_of_()
        self._custom_split_()
        return self._collect_dict_()


if __name__ == '__main__':
    # выполнение этого кода будет производиться только тогда, когда он будет выполняться напрямую из файла, т.е.
    # не в качестве библиотеки

    text = "Я помню чудное мгновенье:\n\
    Передо мной явилась ты,\n\
    Как мимолетное виденье,\n\
    Как гений чистой красоты.\n\
    \n\
    В томленьях грусти безнадежной,\n\
    В тревогах шумной суеты,\n\
    Звучал мне долго голос нежный\n\
    И снились милые черты.\n\
    \n\
    Шли годы. Бурь порыв мятежный\n\
    Рассеял прежние мечты,\n\
    И я забыл твой голос нежный,\n\
    Твои небесные черты.\n\
    \n\
    В глуши, во мраке заточенья\n\
    Тянулись тихо дни мои\n\
    Без божества, без вдохновенья,\n\
    Без слез, без жизни, без любви.\n\
    \n\
    Душе настало пробужденье:\n\
    И вот опять явилась ты,\n\
    Как мимолетное виденье,\n\
    Как гений чистой красоты.\n\
    \n\
    И сердце бьется в упоенье,\n\
    И для него воскресли вновь\n\
    И божество, и вдохновенье,\n\
    И жизнь, и слезы, и любовь."
    # входная строка текста


    diction = make_dict(text)
    print(diction.complete_dict())
    # создаём объект make_dict с входным текстом, после выводим в консоль результат выполнения метода comlete_dict
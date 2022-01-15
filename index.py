def is_contain(sub_word):
    """
    Validate word from letter
    :param sub_word:
    :return:
    """
    # main_word = self.word
    main_word = 'инкапсуляция'
    for letter in sub_word:
        if letter not in main_word or len(main_word) < len(sub_word):
            return False
        else:
            if letter.count(sub_word) > letter.count(main_word):
                return False
            main_word = main_word.replace(letter, '', 1)
    return True


is_contain('инкапсу')
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:  #substitution
        word_pointer = 0
        abbr_pointer = 0
        while word_pointer < len(word):  # 0 < 12    # 1 < 12
            if abbr_pointer >= len(abbr) or abbr[abbr_pointer] == '0':                          # False       # false
                return False

            if abbr[abbr_pointer].isdigit():                                           # True
                number_string = ''
                while (abbr_pointer  < len(abbr) and
                            abbr[abbr_pointer].isdigit()):                 # 0, 1 # n, 2
                    number_string += abbr[abbr_pointer]
                    abbr_pointer += 1                              # 0             # 3
                word_pointer += int(number_string)
            else:
                if abbr[abbr_pointer] != word[word_pointer]:             # n , 1 + 10, n
                    return False
                else:
                    abbr_pointer += 1                                       #1,1
                    word_pointer += 1

        if (abbr_pointer == len(abbr) and
                 word_pointer == len(word)):
            return True
        else:
            return False
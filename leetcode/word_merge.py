class Solution:
    def merge(self, word1: str, word2: str):
        word_one_pointer = 0
        word_two_pointer = 0
        new_word_length = len(word1) + len(word2)
        merged = [""] * (new_word_length)
        letter = 0
        while letter < new_word_length:
            if word_one_pointer < len(word1):
                merged[letter] = word1[word_one_pointer]
            word_one_pointer += 1
            letter += 1
            if word_two_pointer < len(word2):
                merged[letter] = word2[word_two_pointer]
            word_two_pointer += 1
            letter += 1
        return "".join(merged)

        m = len(word1)
        n = len(word2)
        letter = []
        max_len = max(m, n)

        for i in range(max_len):
            if i < m:
                letter += word1[i]
            if i < n:
                letter += word2[i]
        return "".join(letter)
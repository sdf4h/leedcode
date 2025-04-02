class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_words = []
        line_length = 0
        index = 0
        
        while index < len(words):
            word = words[index]
            # Проверяем, помещается ли слово в текущую строку
            if not line_words:
                # Первое слово в строке
                line_words.append(word)
                line_length = len(word)
                index += 1
            else:
                # Учитываем пробел перед словом
                if line_length + 1 + len(word) <= maxWidth:
                    line_words.append(word)
                    line_length += 1 + len(word)
                    index += 1
                else:
                    # Форматируем текущую строку
                    formatted_line = self.formatLine(line_words, maxWidth, False)
                    result.append(formatted_line)
                    line_words = []
                    line_length = 0
        
        # Обрабатываем последнюю строку
        if line_words:
            formatted_line = self.formatLine(line_words, maxWidth, True)
            result.append(formatted_line)
            
        return result
    
    def formatLine(self, words, maxWidth, is_last_line):
        if len(words) == 1 or is_last_line:
            # Левое выравнивание для одной строки или последней строки
            line = ' '.join(words)
            return line + ' ' * (maxWidth - len(line))
        else:
            # Равномерное распределение пробелов
            total_spaces = maxWidth - sum(len(word) for word in words)
            gaps = len(words) - 1
            base_space = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            
            line_parts = []
            for i in range(gaps):
                line_parts.append(words[i])
                line_parts.append(' ' * (base_space + (1 if i < extra_spaces else 0)))
            
            line_parts.append(words[-1])
            return ''.join(line_parts)

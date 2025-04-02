class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        n = len(s)
        if n == 0:
            return False
        
        i = 0
        # Обработка знака в начале
        if s[i] in '+-':
            i += 1
            if i == n:  # Только знак
                return False
        
        has_digit = False
        has_dot = False
        has_exp = False
        
        # Проверка целой и дробной частей
        while i < n and (s[i].isdigit() or s[i] == '.'):
            if s[i].isdigit():
                has_digit = True
            elif s[i] == '.':
                if has_dot or has_exp:  # Две точки или точка после экспоненты
                    return False
                has_dot = True
            i += 1
        
        if not has_digit:  # Нет цифр перед экспонентой
            return False
        
        # Проверка экспоненты
        if i < n and s[i] in 'eE':
            has_exp = True
            i += 1
            if i == n:  # Нет цифр после экспоненты
                return False
            
            # Знак после экспоненты
            if s[i] in '+-':
                i += 1
                if i == n:  # Только знак после экспоненты
                    return False
            
            has_exp_digit = False
            while i < n and s[i].isdigit():
                has_exp_digit = True
                i += 1
            
            if not has_exp_digit:  # Нет цифр после экспоненты
                return False
        
        return i == n  # Проверяем, что дошли до конца строки

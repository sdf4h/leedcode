class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Предварительно вычисляем факториалы для всех чисел до n
        factorials = [1] * (n + 1)
        for i in range(1, n + 1):
            factorials[i] = factorials[i-1] * i
        
        # Список доступных цифр
        digits = [str(i) for i in range(1, n + 1)]
        result = []
        
        # Уменьшаем k на 1 для удобства работы с индексами (0-based)
        k -= 1
        
        for i in range(n, 0, -1):
            # Определяем индекс текущей цифры
            index = k // factorials[i-1]
            result.append(digits.pop(index))
            # Обновляем k для следующей итерации
            k %= factorials[i-1]
            
        return ''.join(result)

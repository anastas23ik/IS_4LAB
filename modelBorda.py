from tabulate import tabulate
class ModelBorda:
    def __init__(self, preference_array, vote_list):
        self.preference_array = preference_array
        self.vote_list = vote_list
        self.answer = 'Этапы решения модели Борда: \n'

    def get(self, data):
        matrix_str = (tabulate(data[0:], missingval="-"))
        self.answer += matrix_str + "\n"
    def get_result(self):
        column_names = ["Геккон", "Попугай", "Хомяк", "Рыбки"]

        #Количество столбцов (предполагаем, что все строки имеют одинаковую длину)
        num_cols = len(self.preference_array[0])

        # Умножаем каждую строку матрицы на соответствующий элемент вектора
        result_mat = [[element * self.vote_list[i] for element in row] for i, row in enumerate(self.preference_array)]
        self.answer += ('Таблица голосов: \n')
        self.get(result_mat)


        # Суммируем элементы по столбцам
        col_sums = [sum(row[i] for row in result_mat) for i in range(num_cols)]
        self.answer += "Количество голосов:\n" + ', '.join(map(str, col_sums))

        column = 0
        results_vote = {}

        for i in col_sums:
            column_name = column_names[column]
            results_vote[column_name] = i
            column += 1

        # Сортировка сумм по столбцам в порядке убывания
        sorted_items = sorted(results_vote.items(), key=lambda item: item[1], reverse=True)

        first_key, first_value = sorted_items[0]  # Извлекаем ключ и значение первого элемента = sorted_results_vote.item[0]




        self.answer += f"\n\nПобедитель: {first_key}, количество голосов: {first_value} \n\n"
        return self.answer



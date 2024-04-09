class RelativeMajority:
    def __init__(self, preference_array, vote_list):
        self.preference_array = preference_array
        self.vote_list = vote_list
        self.answer = 'Этапы решения модели относительного большинства: \n'

    def get_result(self):
        print(self.preference_array)
        print(self.vote_list)
        results = {}
        results_vote = {}
        column_names = ["Геккон", "Попугай", "Хомяк", "Рыбки"]
        # Проход по всем строкам массива
        for row_idx, row in enumerate(self.preference_array):
            for col_idx, element in enumerate(row):
                # Проверяем, равен ли текущий элемент значению '3'
                if element == 3:
                    # Используем имя столбца и номер строки (начиная с 1) как ключ и значение словаря
                    column_name = column_names[col_idx]  # Получаем имя столбца
                    # Записываем данные в словарь, где ключ - это имя столбца, а значение - список номеров строк
                    if column_name not in results:
                        results[column_name] = [row_idx + 1]  # Начинаем счёт строк с 1
                    else:
                        results[column_name].append(row_idx + 1)

                    if column_name not in results_vote:
                        results_vote[column_name] = [self.vote_list[row_idx]]
                    else:
                        results_vote[column_name].append(self.vote_list[row_idx])
                        # results_vote[column_name] = [self.vote_list[row_idx]]
                        print("тест", row_idx)
                # Суммирование значений в списках каждого ключа в results_vote

        self.answer += "\nКандидаты фавориты:\n"
        for column_name, votes in results.items():
            self.answer += (f"{column_name}\n")

        for key, value_list in results_vote.items():
            results_vote[key] = sum(value_list)  # Суммируем значения в списке и записываем обратно

        self.answer += "\nКоличество голосов для каждой категории:\n"
        for key, total_votes in results_vote.items():
            self.answer +=(f"{key}: голосов - {total_votes} \n")

        # Отсортируем в порядке от большего к меньшему
        sorted_results_vote = sorted(results_vote.items(), key=lambda item: item[1], reverse=True)

        first_key, first_value = sorted_results_vote[0]  # Извлекаем ключ и значение первого элемента = sorted_results_vote.item[0]
        max_votes = first_value
        # Определение победителя(ей)
        winners = [name for name, count in sorted_results_vote if count == max_votes]
        if len(winners) == 1:
            self.answer += f"\nПобедитель: {winners[0]} \n"
        else:
            self.answer += f"\nПобедители: {winners} \n"  # или "Ничья между: " + ", ".join(winners) для текстового вывода

        return self.answer


from tabulate import tabulate
class ModelCondorcet:

    def __init__(self, preference_array, vote_list):
        self.column_names = ["Геккон", "Попугай", "Хомяк", "Рыбки"]
        self.preference_array = preference_array #[[3, 2, 1, 0], [3, 1, 2, 0], [0, 3, 1, 2], [0, 2, 3, 1]]
        self.vote_list = vote_list #[3, 5, 7, 6]
        self.count_candidat = len(self.preference_array[0])
        self.count_groups = len(self.preference_array)
        self.matrix = []
        self.output = 'Этапы решения модели Кондорсе \n'
        self.createTable()
        self.prepareTable()


    def get(self, data):
        matrix_str = (tabulate(data[0:], missingval="-"))
        self.output += matrix_str + "\n"

    def get_matrix_string(self, matrix):
        result = ''
        for row in matrix:
            result += " | ".join(map(str, row)) + '\n'
        return result

    def createTable(self):
        for row_idx in range(self.count_groups):
            self.matrix.append([])
            for col_idx in range(self.count_candidat):
                self.matrix[row_idx].append(None)
        
    def prepareTable(self):
        values = self.preference_array

        col_range = range(self.count_candidat)
        row_range = range(self.count_groups)
        
        for col_idx in col_range:
            for col2_idx in range(col_idx + 1, self.count_candidat):
                sum1 = 0
                sum2 = 0
                for row_idx in row_range:
                    if values[row_idx][col_idx] > values[row_idx][col2_idx]:
                        sum1 += self.vote_list[row_idx]
                    else:
                        sum2 += self.vote_list[row_idx]

                self.matrix[col_idx][col2_idx] = sum1
                self.matrix[col2_idx][col_idx] = sum2

        self.output += 'Таблица предпочтений кандидатов: \n'
        self.get(self.matrix)  # Исправленный вызов


    def get_result_winner(self):
        row_range = range(self.count_groups)

        result = []

        for row_idx in row_range:
            for col_idx in range(row_idx + 1, self.count_candidat):
                winner = ''
                loser = ''
                if self.matrix[row_idx][col_idx] > self.matrix[col_idx][row_idx]:
                    winner = self.column_names[row_idx]
                    loser = self.column_names[col_idx]
                else:
                    winner = self.column_names[col_idx]
                    loser = self.column_names[row_idx]
                result.append({
                    'score': max(self.matrix[row_idx][col_idx], self.matrix[col_idx][row_idx]),
                    'winner': winner,
                    'loser': loser
                })

        self.output += "\nСписок победителей в попарном сравнении кандидатов:\n"
        for res in result:
            self.output += (f"Победитель: {res['winner']}, проигравший: {res['loser']}, счёт: {res['score']} \n")

        #self.output += result
        winners = {}

        for record in result:
            winner_name = record['winner']
            if winners.get(winner_name) == None:
                winners[winner_name] = 1
            else:
                winners[winner_name] += 1

        sorted_winners = {k: v for k, v in sorted(winners.items(), key=lambda item: item[1], reverse=True)}

        winner_name = list(sorted_winners.keys())[0]

        self.output += f'\nКандидат «{winner_name}» выигрывает у каждого из остальных кандидатов в попарном сравнении по правилу большинства\n'
        return self.output
    
    def get_result_copeland(self):
        return self.get_all_pairs()

    def get_result_simpson(self):
        return self.get_all_pairs(True)

    def get_all_pairs(self, is_simpson = False):
        self.output = ''
        row_range = range(self.count_groups)
        col_range = range(self.count_candidat)

        result = []

        for row_idx in row_range:
            for col_idx in col_range:
                main_item = self.matrix[row_idx][col_idx]
                secondary_item = self.matrix[col_idx][row_idx]
                if main_item == None or secondary_item == None:
                    continue

                num = 1 if main_item > secondary_item else -1

                result.append({
                    'main': self.column_names[row_idx],
                    'second': self. column_names[col_idx],
                    'score': main_item if is_simpson else num,
                })

        winners = {}

        for record in result:
            name = record['main']
            curr = winners.get(name)
            if curr == None:
                winners[name] = record['score']
            else:
                if is_simpson:
                    winners[name] = min(record['score'], winners[name])
                else:   # правило Копеланда
                    winners[name] += record['score']


        output_rule_str = " Симпсона" if is_simpson else " Копленда"

        self.output += "\nСписок сравнений по правилу"
        self.output += f"{output_rule_str}:\n"
        for res in result:
            self.output += (f"Сравнение '{res['main']}' с '{res['second']}', счёт: {res['score']}\n")

        sorted_winners = {k: v for k, v in sorted(winners.items(), key=lambda item: item[1], reverse=True)}

        self.output += "\nСчет кандидатов:\n"
        for key in list(sorted_winners.keys()):
            self.output += (f"Кандитат: '{key}', счёт: {sorted_winners[key]}\n")

        winner_name = list(sorted_winners.keys())[0]

        self.output += f"\nКандидат «{winner_name}» выигрывает у каждого из остальных кандидатов в попарном сравнении по правилу{output_rule_str}.\n\n"
        return self.output
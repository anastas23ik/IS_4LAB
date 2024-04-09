from modelBorda import ModelBorda
from modelCondorce import ModelCondorcet
from relativeMajority import RelativeMajority


class System:
    def __init__(self, preference_array, count_ratings):
        self.relative_majority = RelativeMajority(preference_array, count_ratings)
        self.model_borda = ModelBorda(preference_array, count_ratings)
        self.model_condorcet = ModelCondorcet(preference_array, count_ratings)


    def get_result(self):
        answer = 'Относительное большинство:' + '\n' + self.relative_majority.get_result() + '\n'
        answer += 'Модель Борда:' + '\n' + self.model_borda.get_result() + '\n'
        answer += 'Модель Кондерсе: ' + '\n' + self.model_condorcet.get_result_winner() + '\n'
        answer += 'Правило Копланда: ' + '\n' + self.model_condorcet.get_result_copeland() + '\n'
        answer += 'Правило Симпсона: ' + '\n' + self.model_condorcet.get_result_simpson() + '\n'

        return answer
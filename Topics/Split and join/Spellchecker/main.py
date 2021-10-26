dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
input_words = input().split()
incorrect_words = [word for word in input_words if word not in dictionary]
result = '\n'.join(incorrect_words) if incorrect_words else 'OK'
print(result)

class Statistics:

    def __init__(self, users_dict):
        users = []
        for user_id in users_dict:
            users.append(users_dict[user_id])

        self.users = users

    def getUsersCount(self):
        women = 0
        men = 0
        undefined = 0

        for user in self.users:
            if user.gender == 'male':
                men += 1
            elif user.gender == 'female':
                women += 1
            else:
                undefined += 1

        return {
            'male': men,
            'female': women,
            'undefined': undefined,
            'total': women + men + undefined,
        }

    def getUsersSentiment(self):
        positive = 0
        negative = 0
        neutral = 0

        # Para guardar conteos de mujeres
        female_positive = 0
        female_negative = 0
        female_neutral = 0

        # Para guardar conteos de hombres
        male_positive = 0
        male_negative = 0
        male_neutral = 0

        # Para guardar conteos de indefinidos
        undefined_positive = 0
        undefined_negative = 0
        undefined_neutral = 0

        for user in self.users:
            sentiment = user.getSentiment()

            if sentiment == 'positive':
                positive += 1

                if user.gender == 'female':
                    female_positive += 1
                elif user.gender == 'male':
                    male_positive += 1
                else:
                    undefined_positive += 1

            elif sentiment == 'negative':
                negative += 1

                if user.gender == 'female':
                    female_negative += 1
                elif user.gender == 'male':
                    male_negative += 1
                else:
                    undefined_negative += 1

            elif sentiment == 'neutral':
                neutral += 1

                if user.gender == 'female':
                    female_neutral += 1
                elif user.gender == 'male':
                    male_neutral += 1
                else:
                    undefined_neutral += 1

        return {
            'all': {
                'positive': positive,
                'negative': negative,
                'neutral': neutral,
            },
            'female': {
                'positive': female_positive,
                'negative': female_negative,
                'neutral': female_neutral,
            },
            'male': {
                'positive': male_positive,
                'negative': male_negative,
                'neutral': male_neutral,
            },
            'undefined': {
                'positive': undefined_positive,
                'negative': undefined_negative,
                'neutral': undefined_neutral,
            },
        }

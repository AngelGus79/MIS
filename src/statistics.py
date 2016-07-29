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

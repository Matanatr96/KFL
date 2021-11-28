from sleeper_wrapper import League
from sleeper_wrapper import Stats

from flask_table import Table, Col

class Sleeper:
    def __init__(self):
        self.league = League('732312711840550912')

        d_users = self.league.get_users()
        users = {}
        for r in d_users:
            users[r['user_id']] = {'user_id': r['user_id'], 'name': r['display_name']}

        p = self.league.get_rosters()
        roster = []
        for i, x in enumerate(p):
            oID = x['owner_id']
            rec = users[oID]
            rec['roster_id'] = i + 1
            rec['wins'] = x['settings']['wins']
            rec['losses'] = x['settings']['losses']
            points = int(x['settings']['fpts']) + (int(x['settings']['fpts_decimal']) / 100)
            pa = int(x['settings']['fpts_against']) + (int(x['settings']['fpts_against_decimal']) / 100)
            rec['pf'] = points
            rec['pa'] = pa
            users[oID] = rec

        self.users = users


    def getUsers(self):
        return self.users

    def getTable(self):
        class ItemTable(Table):
            name = Col('Name')
            wins = Col('Wins')
            losses = Col('Losses')
            pf = Col('Pf')
            pa = Col('Pa')

        # Populate the table
        table = ItemTable(self.users.values())

        return table
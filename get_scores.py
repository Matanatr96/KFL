import argparse

from sleeper_wrapper import League
from collections import defaultdict
import pandas as pd
league = League('918363762489450496')

roster_conversions = ['Mattapalli', 'Komee', 'Idate', 'Bada', 'Digby', 'Nethi', 'Rattan', 'Upadhyaya', 'Aireddy',
                      'Hansen', 'Le', 'Pandya']

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--week', required=True)
args = parser.parse_args()
print(args.week)

def get_matchups(week: int) -> (defaultdict, pd.DataFrame):
    all_matchups = league.get_matchups(week)
    matchups = defaultdict(list)
    ranks = []
    for matchup in all_matchups:
        matchup_id = matchup['matchup_id']
        matchups[matchup_id].append((matchup['roster_id'], matchup['points']))
        ranks.append([matchup['roster_id'], matchup['points']])

    ranks_df = pd.DataFrame(ranks, columns=['Id', 'Score']).sort_values(by='Score', ascending=False).set_index('Id')
    ranks_df['Rank'] = range(1, 13)
    return matchups, ranks_df


def get_scores(week: int) -> list:
    matchups, ranks = get_matchups(week)
    df = []
    for j in matchups.values():
        roster_id1 = j[0][0]
        roster_id2 = j[1][0]
        one_score = j[0][1]
        two_score = j[1][1]
        one_diff = round(one_score - two_score, 2)
        two_diff = round(two_score - one_score, 2)
        df.append(
            [2023, roster_conversions[roster_id1 - 1], week, 1 if one_score > two_score else 0, one_score, two_score,
             roster_conversions[roster_id2 - 1], one_diff, ranks.loc[roster_id1, 'Rank']])
        df.append(
            [2023, roster_conversions[roster_id2 - 1], week, 1 if one_score < two_score else 0, two_score, one_score,
             roster_conversions[roster_id1 - 1], two_diff, ranks.loc[roster_id2, 'Rank']])

    print(df)


get_scores(args.week)

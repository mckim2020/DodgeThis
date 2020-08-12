from riotwatcher import LolWatcher, ApiError
import pandas as pd


# global variables
api_key = 'RGAPI-86c34767-17f5-41e1-82b8-c59e5349f478'
watcher = LolWatcher(api_key)
accountId = '1tl_YlUF1FBkFOHe2hMZkrFjQItv9XaYHjjgxmV88fUjJnM'
myRegion = 'kr'

me = watcher.summoner.by_name(myRegion, 'hide on bush')
#print(me)

my_matches = watcher.match.matchlist_by_account(myRegion, me['accountId'])

# fetch last match detail
last_match = my_matches['matches'][0]
match_detail = watcher.match.by_id(myRegion, last_match['gameId'])

participants = []
for row in match_detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants.append(participants_row)

df = pd.DataFrame(participants)
print(df)

import pandas as pd
from riotwatcher import LolWatcher, ApiError
import requests
import time


#harvesting starts here
# global variables

api_key = 'RGAPI-86c34767-17f5-41e1-82b8-c59e5349f478'
#api_url='https://kr.api.riotgames.com/lol/match/v4/matches/' + str(match_info_df2['gameId'].iloc[i]) + '?api_key=' + api_key
watcher = LolWatcher(api_key)
accountId = '1tl_YlUF1FBkFOHe2hMZkrFjQItv9XaYHjjgxmV88fUjJnM'
myRegion = 'kr'

me = watcher.summoner.by_name(myRegion, 'Pensieve')
#print(me)

my_matches = watcher.match.matchlist_by_account(myRegion, me['accountId'])


# 1 to 99 data fetching
participants = []

for i in range(99):
#    req = requests.get(api_key)
    last_match = my_matches['matches'][i]
    match_detail = watcher.match.by_id(myRegion, last_match['gameId'])

    for row in match_detail['participants']:
        participants_row = {}
        participants_row['champion'] = row['championId']
        participants_row['win'] = row['stats']['win']
        participants.append(participants_row)

    print(1)
    time.sleep(10)


# Convert and save to csv file(LolData.xlsx)
df = pd.DataFrame(participants)

df.to_csv("LolData.xlsx", header=False, index=False)

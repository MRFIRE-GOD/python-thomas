from riotwatcher import LolWatcher, ApiError
import datetime as datetime
api_key = 'RGAPI-3902a756-7317-415e-9113-5b18c5a2a56d'
watcher = LolWatcher(api_key)
my_region = "na1"
me = watcher.summoner.by_name(my_region, "MRFIREGOD")
print(me)


def get_summoner_data(region, summoner_id):
    try:
        data = watcher.summoner.by_id(region, summoner_id)
        return data
    except ApiError as e:
        print(e)
        return None
        
import requests

BASE_URL = "https://{0}.api.riotgames.com/"
ACCOUNT_REGIONS = ["americas", "asia", "europe"]
GAMES_REGIONS = ["br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"]


class RiotApi(object):


	def __init__(self, key: str):
		self.key = key


	def __request(self, url: str):
		return requests.get(url, headers={"X-Riot-Token": self.key}).json()


	def __generate_region_url(self, region: str, regions: list):
		if region.lower() not in regions:
			raise ValueError("AVAILABLE REGIONS: {}".format(" ".join(regions)))
		return BASE_URL.format(region.lower())


	# ACCOUNT V1
	def get_account_by_puuid(self, region: str, puuid: str):
		url = self.__generate_region_url(region, ACCOUNT_REGIONS)
		request_url = "{}/riot/account/v1/accounts/by-puuid/{}".format(url, puuid)
		return self.__request(request_url)

	
	def get_account_by_id(self, region: str, game_name: str, tag_line: str):
		url = self.__generate_region_url(region, ACCOUNT_REGIONS)
		request_url = "{}/riot/account/v1/accounts/by-riot-id/{}/{}".format(url,game_name, tag_line)
		return self.__request(request_url)


	# SUMMONER V4
	def get_summoner_by_name(self, region: str, name: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/summoner/v4/summoners/by-name/{}".format(url, name)
		return self.__request(request_url)
	

	def get_summoner_by_account_id(self, region: str, account_id: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/summoner/v4/summoners/by-account/{}".format(url, account_id)
		return self.__request(request_url)
	

	def get_summoner_by_id(self, region: str, id: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/summoner/v4/summoners/{}".format(url, id)
		return self.__request(request_url)

	
	def get_summoner_by_puuid(self, region: str, puuid: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/summoner/v4/summoners/by-puuid/{}".format(url, puuid)
		return self.__request(request_url)

	
	# LOL STATUS V3
	def get_lol_status(self, region: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/status/v3/shard-data".format(url)
		return self.__request(request_url)
	

	# CHAMPION V3
	def get_lol_champion_rotations(self, region: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/platform/v3/champion-rotations".format(url)
		return self.__request(request_url)
	

	# CHAMPION MASTERY V4
	def get_total_mastery_score(self, region: str, id: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/champion-mastery/v4/scores/by-summoner/{}".format(url, id)
		return self.__request(request_url)
	

	def get_all_champions_mastery(self, region: str, id: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/champion-mastery/v4/champion-masteries/by-summoner/{}".format(url, id)
		return self.__request(request_url)

	
	def get_champion_mastery(self, region: str, id: str, champion_id: str):
		url = self.__generate_region_url(region, GAMES_REGIONS)
		request_url = "{}/lol/champion-mastery/v4/champion-masteries/by-summoner/{}/by-champion/{}".format(url, id, champion_id)
		return self.__request(request_url)
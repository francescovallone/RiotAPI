import requests

BASE_URL = "https://{0}.api.riotgames.com/"


class RiotApi(object):


	def __init__(self, key: str):
		self.key = key


	def __request(self, url: str):
		return requests.get(url, headers={"X-Riot-Token": self.key}).json()


	def get_account_by_puuid(self, region: str, puuid: str):
		if region.lower() not in ["americas", "asia", "europe"]:
			raise ValueError("Region must be americas or asia or europe")
		url = BASE_URL.format(region.lower())
		request_url = "{}/riot/account/v1/accounts/by-puuid/{}".format(url, puuid)
		return self.__request(request_url)

	
	def get_account_by_id(self, region: str, game_name: str, tag_line: str):
		if region.lower() not in ["americas", "asia", "europe"]:
			raise ValueError("Region must be americas or asia or europe")
		url = BASE_URL.format(region.lower())
		request_url = "{}/riot/account/v1/accounts/by-riot-id/{}/{}".format(url,game_name, tag_line)
		return self.__request(request_url)

	
	def get_summoner_by_name(self, region: str, name: str):
		if region.lower() not in ["br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"]:
			raise ValueError("Region must be americas or asia or europe")
		url = BASE_URL.format(region.lower())
		request_url = "{}/lol/summoner/v4/summoners/by-name/{}".format(url, name)
		return self.__request(request_url)
	

	def get_summoner_by_account_id(self, region: str, account_id: str):
		if region.lower() not in ["br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"]:
			raise ValueError("Region must be americas or asia or europe")
		url = BASE_URL.format(region.lower())
		request_url = "{}/lol/summoner/v4/summoners/by-account/{}".format(url, account_id)
		return self.__request(request_url)
	

	def get_summoner_by_id(self, region: str, id: str):
		if region.lower() not in ["br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"]:
			raise ValueError("Region must be americas or asia or europe")
		url = BASE_URL.format(region.lower())
		request_url = "{}/lol/summoner/v4/summoners/{}".format(url, id)
		return self.__request(request_url)

	
	def get_summoner_by_puuid(self, region: str, puuid: str):
		if region.lower() not in ["br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"]:
			raise ValueError("Region must be americas or asia or europe")
		url = BASE_URL.format(region.lower())
		request_url = "{}/lol/summoner/v4/summoners/by-puuid/{}".format(url, puuid)
		return self.__request(request_url)
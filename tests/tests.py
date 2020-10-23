import src as api
from key import RIOT_KEY
import unittest

api = api.RiotApi(RIOT_KEY)


class TestApi(unittest.TestCase):
	def test_account(self):
		self.assertEqual(api.get_account_by_id("europe", "MushiKun", "BUCKY"),\
			 api.get_account_by_puuid("europe", "Q0EWHfz9zWglKLP_TPg59q9Shkjd7YydYYHxaggkS_AiXzR-LaH91Fphv8ewteTS1pykKJFBhi7Ypw"), "Should be equal")

	def test_summoner(self):
		equal_to = api.get_summoner_by_name("euw1", "MushiKun")
		requests = [api.get_summoner_by_puuid("euw1", "Q0EWHfz9zWglKLP_TPg59q9Shkjd7YydYYHxaggkS_AiXzR-LaH91Fphv8ewteTS1pykKJFBhi7Ypw"),\
			api.get_summoner_by_id("euw1", "U_rxSsAS4GAvTPndiBZ5QQ9dvyyWQJaDvcD4a5Yx9ytXXYU"),\
			api.get_summoner_by_account_id("euw1", "j-fmQt_cOYwuFEu9tASkbVjP5H9Be6JxOW_MrDc7UblqSg")]
		for r in requests:
			self.assertDictEqual(equal_to, r)
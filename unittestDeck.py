''' this program performs unittests to make sure the program is working correctly. 
It selects an Ace of Hearts as a test'''
from Deck import Deck, Card
import unittest


class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts","A")

	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")

	def test_repr(self):
		"""repr should return a string stating value then suit"""
		self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		""""init should show a list of 52 cards"""
		self.assertEqual(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards), 52)	
	def test_repr(self):
		"""should return deck of cards"""
		self.assertEqual(repr(self.deck),"Deck of 52 cards")

	def test_count(self):
		"""shows count of cards in deck"""
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)
	def test_deal_sufficient_cards(self):
		"""should deal cards specified"""
		cards = self.deck_deal(10)
		self.assertEqual(len(cards), 10)
		self.assertEqual(self.deck.count(), 42)
	def test_deal_insufficient_cards(self):
		cards = self.deck._deal(100)
		self.assertEqual(len(cards),52)
		self.assertEqual(self.deck.count(), 0)
	def test_deal_no_cards(self):
		self.deck._deal(self.deck.count())
		with self.assertRaises(ValueError):
			self.deck._deal(1)
	def test_deal_card(self):
		"""deal card should deal a single card"""
		card = self.deck.card[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(self.deck.count(), 51)
	def test_deal_hand(self):
		"""deal hand should deal number of cards passed"""
		cards = self.deck.deal_hand(20)
		self.assertEqual(len(cards), 20)
		self.assertEqual(self.deck.count(), 32)
	def test_shuffle_full_deck(self):
		"""shuffle should shuffle the deck"""
		cards = self.deck.cards[:]
		self.deck.shuffle()
		self.assertNotEqual(cards,self.deck.cards)
		self.assertEqual(self.deck.count(), 52)

	def test_shuffle_not_full_deck(self):
		"""shuffle should not work if cards in deck not 52"""
		self.deck._deal(1)
		with self.assertRaises(ValueError):
			self.deck.shuffle()
if __name__ == "__main__":
	unittest.main()
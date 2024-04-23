# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_other_prior(self):
        items = [Item("other", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_other_after(self):
        items = [Item("other", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_other_under(self):
        items = [Item("other", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_brie_prior(self):
        items = [Item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_after(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_brie_over(self):
        items = [Item("Aged Brie",1 , 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_passes_prior_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",11 , 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_passes_prior_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",6 , 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_passes_prior_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",1 , 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_passes_after_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",-1 , 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_prior(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5 , 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_after(self):
        items = [Item("Sulfuras, Hand of Ragnaros",-1 , 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_conjured_prior(self):
            items = [Item("Conjured", 0, 2)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            self.assertEqual(-1, items[0].sell_in)
            self.assertEqual(0, items[0].quality)

    def test_conjured_after(self):
        items = [Item("Conjured", -1, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_other_under(self):
        items = [Item("Conjured", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
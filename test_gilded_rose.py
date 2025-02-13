# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(("Sulfuras", 80), (all_items[0].name, all_items[0].quality))
        
    def test_quality_never_negative(self):
        
        items = [Item("Elixir of the Mongoose", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0, "Quality should never be negative")

    def test_backstage_passes_drop_to_zero_after_concert(self):
    
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0, "Backstage passes should have quality 0 after sell_in is 0")
    
    def test_aged_brie_increases_quality_correctly(self):
        
        items = [Item("Aged Brie", 2, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50, "Aged Brie should not exceed quality of 50")
    
    def test_sulfuras_sell_in_decreases(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 5, "Sulfuras should not change sell_in") 

    
    def test_syntax_error(self):
        # self.assertEqual(Item("foo", 0, 0).quality,, 0)  # SyntaxError: invalid syntax (extra comma)
        pass



if __name__ == '__main__':
    unittest.main()

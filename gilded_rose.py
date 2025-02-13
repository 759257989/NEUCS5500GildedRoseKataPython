# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        
        # update on the items
    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update(item)
            
    def get_strategy(self, item):
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassStrategy()
        elif item.name == "Sulfuras":
            return SulfurasStrategy()
        elif "Conjured" in item.name:
            return ConjuredStrategy()
        else:
            return NormalStrategy()
        
    def get_items(self):
        return self.items
    
class UpdateStrategy:
    def update(self, item):
        raise NotImplementedError("must implement the update method")

# normal goods
class NormalStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        degradation = 1 if item.sell_in >= 0 else 2
        item.quality = max(item.quality - degradation, 0)

# Aged Brie update
class AgedBrieStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        # increase quality
        increment = 1 if item.sell_in >= 0 else 2
        item.quality = min(item.quality + increment, 50)  
   
# backstagepass update
class BackstagePassStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            # if the sell in day pass, 0 quality
            item.quality = 0
        else: #still not pass sell in day
            if item.sell_in < 5:
                increment = 3
            elif item.sell_in < 10:
                increment = 2
            else:
                increment = 1
            item.quality = min(item.quality + increment, 50)

# sulfura update
class SulfurasStrategy(UpdateStrategy):
    def update(self, item):
        #quality doesnt change
        item.quality = 80
#conjured update
class ConjuredStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        # twice as fast as normal 
        degradation = 2 if item.sell_in >= 0 else 4
        item.quality = max(item.quality - degradation, 0)


    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1

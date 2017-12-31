#inventory.py
def display_inventory(inventory):
    print("持ち物リスト：")
    item_total = 0
    for k, v in inventory.items():
        #ソースコード
        print(v, k)
        item_total += v
    print("アイテム総数: " + str(item_total))

def add_to_inventory(inventory, added_items):
    #ソースコード
    for i in range(len(added_items)):
        if added_items[i] not in inventory.keys():
            inventory[added_items[i]] = 1
        else:
            inventory[added_items[i]] += 1
    return inventory

#stuff = {'ロープ':1, 'たいまつ':6, '金貨':42, '手裏剣':1, '矢':12}
#display_inventory(stuff)

inv = {'金貨':42, 'ロープ':1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

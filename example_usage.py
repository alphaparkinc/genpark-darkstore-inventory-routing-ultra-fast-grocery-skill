from client import DarkstoreInventoryRoutingUltraFastGroceryClient

def main():
    client = DarkstoreInventoryRoutingUltraFastGroceryClient()
    res = client.dispatch_ultra_fast_order((24.7500, 46.6500), ['fresh_dates', 'goat_milk'])
    print('Dispatch: ' + res['dispatch_id'] + ' from ' + res['assigned_darkstore'])
    print('Pick & Pack: ' + str(res['picker_pick_and_pack_time_seconds']) + 's | Delivery ETA: ' + str(res['estimated_delivery_time_mins']) + ' mins')
    print('Distance: ' + str(res['distance_to_door_km']) + 'km (Guaranteed <15m: ' + str(res['on_time_guarantee_met']) + ')')

if __name__ == '__main__':
    main()

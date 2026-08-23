class DarkstoreInventoryRoutingUltraFastGroceryClient:
    def dispatch_ultra_fast_order(self, customer_lat_lng=(24.7136, 46.6753), order_sku_list=None):
        order_sku_list = order_sku_list or ['SKU_MILK_FRESH', 'SKU_ARABIC_BREAD', 'SKU_WATER_6PACK']
        return {
            'dispatch_id': 'nnj_dsp_8841',
            'assigned_darkstore': 'RIYADH_AL_MALQA_HUB_03',
            'picker_pick_and_pack_time_seconds': 114,
            'courier_motorcycle_speed_kmh': 38.0,
            'distance_to_door_km': 1.8,
            'estimated_delivery_time_mins': 12.5,
            'on_time_guarantee_met': True
        }

CATEGORIES = {
    'Mazzza narx!': 'mazza-narx/',
    'Pas-narxlar': 'low_prices/',
    'ҲАВО СОВУТГИЧЛАР': 'kondicionery/',
    'СМАРТФОНЛАР': 'telefony/',
    'МУЗЛАТГИЧЛАР': 'holodilniki/',
    'ЧАНГЮТГИЧЛАР': 'pylesosy/',
    'НОУТБУКЛАР': 'noutbuki/',
    'ТЕЛЕВИЗОРЛАР': 'televizory/'
}


def get_value(category):
    for k, v in CATEGORIES.items():
        if k == category:
            return v

# mock_data.py

from typing import List, Dict

# -------------------
# Sales History
# -------------------
SALES_HISTORY: List[Dict] = [
    {"product_id":"Camry","date":"2025-11-01","units":5},
    {"product_id":"Camry","date":"2025-11-02","units":3},
    {"product_id":"Camry","date":"2025-11-03","units":4},
    {"product_id":"Camry","date":"2025-11-04","units":6},
    {"product_id":"Camry","date":"2025-11-05","units":7},
    {"product_id":"Camry","date":"2025-11-06","units":8},
    {"product_id":"Camry","date":"2025-11-07","units":6},
    {"product_id":"Camry","date":"2025-11-08","units":5},
    {"product_id":"Camry","date":"2025-11-09","units":9},
    {"product_id":"Camry","date":"2025-11-10","units":4}
]

# -------------------
# Inventory Levels
# -------------------
INVENTORY_LEVELS: List[Dict] = [
    {"product_id":"Camry","location_id":"STORE-A","on_hand":20,"reserved":2,"available":18},
    {"product_id":"Camry","location_id":"STORE-B","on_hand":15,"reserved":1,"available":14},
    {"product_id":"Camry","location_id":"STORE-C","on_hand":18,"reserved":0,"available":18},
    {"product_id":"Camry","location_id":"STORE-D","on_hand":10,"reserved":3,"available":7},
    {"product_id":"Camry","location_id":"STORE-E","on_hand":8,"reserved":0,"available":8},
    {"product_id":"Camry","location_id":"STORE-F","on_hand":7,"reserved":1,"available":6},
    {"product_id":"Camry","location_id":"STORE-G","on_hand":12,"reserved":2,"available":10},
    {"product_id":"Camry","location_id":"STORE-H","on_hand":9,"reserved":0,"available":9},
    {"product_id":"Camry","location_id":"STORE-I","on_hand":17,"reserved":1,"available":16},
    {"product_id":"Camry","location_id":"STORE-J","on_hand":14,"reserved":2,"available":12}
]

# -------------------
# Supplier List
# -------------------
SUPPLIERS: List[Dict] = [
    {"supplier_id":"SUP-YAMAHA","name":"Yamaha Imports","region":"Japan","rating":88.5},
    {"supplier_id":"SUP-FORD","name":"Ford Distributors","region":"USA","rating":82.3},
    {"supplier_id":"SUP-GMC","name":"GMC Auto Parts","region":"USA","rating":74.2},
    {"supplier_id":"SUP-TOYOTA","name":"Toyota Motors","region":"Japan","rating":91.4},
    {"supplier_id":"SUP-HONDA","name":"Honda Global","region":"Japan","rating":85.1},
    {"supplier_id":"SUP-ACURA","name":"Acura Auto Supply","region":"Japan","rating":77.3},
    {"supplier_id":"SUP-KIA","name":"Kia Korea Parts","region":"Korea","rating":69.9},
    {"supplier_id":"SUP-HYUNDAI","name":"Hyundai Motors Co","region":"Korea","rating":72.5},
    {"supplier_id":"SUP-CHEVY","name":"Chevy Auto Distributors","region":"USA","rating":80.2},
    {"supplier_id":"SUP-BMW","name":"BMW International","region":"Germany","rating":89.7}
]

# -------------------
# Supplier Pricing
# -------------------
PRICING: List[Dict] = [
    {"supplier_id":"SUP-YAMAHA","product_id":"Camry","unit_price":22800,"currency":"USD","min_order_qty":2},
    {"supplier_id":"SUP-FORD","product_id":"Camry","unit_price":23500,"currency":"USD","min_order_qty":3},
    {"supplier_id":"SUP-GMC","product_id":"Camry","unit_price":22500,"currency":"USD","min_order_qty":4},
    {"supplier_id":"SUP-TOYOTA","product_id":"Camry","unit_price":23200,"currency":"USD","min_order_qty":1},
    {"supplier_id":"SUP-HONDA","product_id":"Camry","unit_price":23050,"currency":"USD","min_order_qty":2},
    {"supplier_id":"SUP-ACURA","product_id":"Camry","unit_price":24000,"currency":"USD","min_order_qty":1},
    {"supplier_id":"SUP-KIA","product_id":"Camry","unit_price":22000,"currency":"USD","min_order_qty":5},
    {"supplier_id":"SUP-HYUNDAI","product_id":"Camry","unit_price":22350,"currency":"USD","min_order_qty":4},
    {"supplier_id":"SUP-CHEVY","product_id":"Camry","unit_price":23700,"currency":"USD","min_order_qty":3},
    {"supplier_id":"SUP-BMW","product_id":"Camry","unit_price":25000,"currency":"USD","min_order_qty":2}
]

# -------------------
# Supplier Lead Times
# -------------------
LEAD_TIMES: List[Dict] = [
    {"supplier_id":"SUP-YAMAHA","product_id":"Camry","lead_time_days":15,"on_time_delivery_pct":0.92},
    {"supplier_id":"SUP-FORD","product_id":"Camry","lead_time_days":12,"on_time_delivery_pct":0.88},
    {"supplier_id":"SUP-GMC","product_id":"Camry","lead_time_days":18,"on_time_delivery_pct":0.81},
    {"supplier_id":"SUP-TOYOTA","product_id":"Camry","lead_time_days":10,"on_time_delivery_pct":0.95},
    {"supplier_id":"SUP-HONDA","product_id":"Camry","lead_time_days":14,"on_time_delivery_pct":0.90},
    {"supplier_id":"SUP-ACURA","product_id":"Camry","lead_time_days":16,"on_time_delivery_pct":0.85},
    {"supplier_id":"SUP-KIA","product_id":"Camry","lead_time_days":20,"on_time_delivery_pct":0.78},
    {"supplier_id":"SUP-HYUNDAI","product_id":"Camry","lead_time_days":19,"on_time_delivery_pct":0.80},
    {"supplier_id":"SUP-CHEVY","product_id":"Camry","lead_time_days":13,"on_time_delivery_pct":0.87},
    {"supplier_id":"SUP-BMW","product_id":"Camry","lead_time_days":11,"on_time_delivery_pct":0.94}
]

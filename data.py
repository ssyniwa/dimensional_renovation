"""
異次元インテリア・リノベーション - ゲームデータモジュール (画像パス対応版)
"""

CLIENT_TYPES = {
    "magma_dragon": {
        "name": "灼熱の溶岩竜族",
        "title": "深紅の灼熱領域からの訪問者",
        "description": "超高温かつ超乾燥の過酷な環境を好む古代竜族。重厚で金属的なインテリアを好みます。",
        "min_temp": 800,
        "max_humidity": 10,
        "target_gravity": 1.5,
        "budget": 60000,
        "preferred_style": "industrial_magma",
        "avatar_image": "images/clients/magma_dragon.jpg"
    },
    "cyber_ai": {
        "name": "電脳空間のAI精神体",
        "title": "第9サーバー階層の統一意識",
        "description": "サーバーのオーバーヒートを防ぐ極低温と完璧な冷却効率を要求する情報生命体。",
        "min_temp": -100,
        "max_humidity": 0,
        "target_gravity": 0.0,
        "budget": 85000,
        "preferred_style": "cyberpunk_neon",
        "avatar_image": "images/clients/cyber_ai.jpg"
    },
    "deepsea_crystal": {
        "name": "深海の結晶生命体",
        "title": "海溝第10区のクリスタルアーキテクト",
        "description": "高水圧と神秘的な静寂を愛する結晶体。水温管理と高い審美性を備えた空間を求めています。",
        "min_temp": -10,
        "max_humidity": 100,
        "target_gravity": 1.0,
        "budget": 75000,
        "preferred_style": "crystal_ocean",
        "avatar_image": "images/clients/deepsea_crystal.jpg"
    },
    "astral_spirit": {
        "name": "次元回廊の風使い",
        "title": "銀河を漂う精霊旅団",
        "description": "重力ゼロの流体空間で暮らす種族。気流の流れと幻想的な装飾を好みます。",
        "min_temp": 15,
        "max_humidity": 40,
        "target_gravity": 0.0,
        "budget": 50000,
        "preferred_style": "astral_ether",
        "avatar_image": "images/clients/astral_spirit.jpg"
    }
}

FURNITURE_CATALOG = {
    "f_magma_floor": {
        "name": "耐熱マグマタイル",
        "category": "床・壁",
        "cost": 8000,
        "temp_delta": 30,
        "humidity_delta": -20,
        "gravity_delta": 0.0,
        "aesthetic": 15,
        "style": "industrial_magma",
        "image_path": "images/furniture/magma_floor.jpg"
    },
    "f_cool_panel": {
        "name": "超伝導冷却パネル",
        "category": "床・壁",
        "cost": 12000,
        "temp_delta": -45,
        "humidity_delta": -30,
        "gravity_delta": 0.0,
        "aesthetic": 20,
        "style": "cyberpunk_neon",
        "image_path": "images/furniture/cool_panel.jpg"
    },
    "f_crystal_pool": {
        "name": "深海高圧ウォータープール",
        "category": "水質・環境",
        "cost": 15000,
        "temp_delta": -5,
        "humidity_delta": 60,
        "gravity_delta": 0.3,
        "aesthetic": 30,
        "style": "crystal_ocean",
        "image_path": "images/furniture/crystal_pool.jpg"
    },
    "f_zerog_field": {
        "name": "ゼロG発生ジェネレーター",
        "category": "環境装置",
        "cost": 18000,
        "temp_delta": 0,
        "humidity_delta": 0,
        "gravity_delta": -1.0,
        "aesthetic": 25,
        "style": "astral_ether",
        "image_path": "images/furniture/zerog_field.jpg"
    },
    "f_dark_fireplace": {
        "name": "反物質暖炉",
        "category": "大型家具",
        "cost": 22000,
        "temp_delta": 60,
        "humidity_delta": -40,
        "gravity_delta": 0.1,
        "aesthetic": 45,
        "style": "industrial_magma",
        "image_path": "images/furniture/dark_fireplace.jpg"
    },
    "f_data_sofa": {
        "name": "量子データ同期ソファ",
        "category": "家具",
        "cost": 14000,
        "temp_delta": -2,
        "humidity_delta": 0,
        "gravity_delta": 0.0,
        "aesthetic": 35,
        "style": "cyberpunk_neon",
        "image_path": "images/furniture/data_sofa.jpg"
    },
    "f_biolum_plant": {
        "name": "発光水晶樹のインテリア",
        "category": "装飾品",
        "cost": 9000,
        "temp_delta": 0,
        "humidity_delta": 10,
        "gravity_delta": 0.0,
        "aesthetic": 40,
        "style": "crystal_ocean",
        "image_path": "images/furniture/biolum_plant.jpg"
    },
    "f_ether_chandelier": {
        "name": "エーテル気流シャンデリア",
        "category": "照明",
        "cost": 11000,
        "temp_delta": 10,
        "humidity_delta": 0,
        "gravity_delta": -0.2,
        "aesthetic": 50,
        "style": "astral_ether",
        "image_path": "images/furniture/ether_chandelier.jpg"
    },

    # --- 新規追加の家具 (8種類) ---
    "f_plasma_forge": {
        "name": "超高圧プラズマ溶鉱炉",
        "category": "大型家具",
        "cost": 28000,
        "temp_delta": 80,
        "humidity_delta": -50,
        "gravity_delta": 0.1,
        "aesthetic": 55,
        "style": "industrial_magma",
        "image_path": "images/furniture/plasma_forge.jpg"
    },
    "f_liquid_metal_wall": {
        "name": "液体金属防壁パネル",
        "category": "床・壁",
        "cost": 16000,
        "temp_delta": 15,
        "humidity_delta": -10,
        "gravity_delta": 0.0,
        "aesthetic": 30,
        "style": "industrial_magma",
        "image_path": "images/furniture/liquid_metal_wall.jpg"
    },
    "f_neon_matrix_display": {
        "name": "ネオン・マトリクス・ウォール",
        "category": "装飾・壁",
        "cost": 13000,
        "temp_delta": -10,
        "humidity_delta": -10,
        "gravity_delta": 0.0,
        "aesthetic": 45,
        "style": "cyberpunk_neon",
        "image_path": "images/furniture/neon_matrix_display.jpg"
    },
    "f_cryo_sleep_pod": {
        "name": "極低温コールドスリープポッド",
        "category": "大型家具",
        "cost": 25000,
        "temp_delta": -60,
        "humidity_delta": -20,
        "gravity_delta": 0.0,
        "aesthetic": 60,
        "style": "cyberpunk_neon",
        "image_path": "images/furniture/cryo_sleep_pod.jpg"
    },
    "f_abyssal_hydro_pillar": {
        "name": "深海圧搾ハイドロピラー",
        "category": "環境装置",
        "cost": 19000,
        "temp_delta": -8,
        "humidity_delta": 80,
        "gravity_delta": 0.6,
        "aesthetic": 40,
        "style": "crystal_ocean",
        "image_path": "images/furniture/abyssal_hydro_pillar.jpg"
    },
    "f_coral_prism": {
        "name": "虹彩発光コーラルプリズム",
        "category": "照明",
        "cost": 10500,
        "temp_delta": 0,
        "humidity_delta": 30,
        "gravity_delta": 0.1,
        "aesthetic": 50,
        "style": "crystal_ocean",
        "image_path": "images/furniture/coral_prism.jpg"
    },
    "f_antigrav_floating_ring": {
        "name": "反重力フローティングリング",
        "category": "大型家具",
        "cost": 21000,
        "temp_delta": 0,
        "humidity_delta": 0,
        "gravity_delta": -0.8,
        "aesthetic": 55,
        "style": "astral_ether",
        "image_path": "images/furniture/antigrav_floating_ring.jpg"
    },
    "f_stellar_wind_harp": {
        "name": "星間微風のエーテルハープ",
        "category": "装飾品",
        "cost": 12500,
        "temp_delta": 5,
        "humidity_delta": 10,
        "gravity_delta": -0.3,
        "aesthetic": 65,
        "style": "astral_ether",
        "image_path": "images/furniture/stellar_wind_harp.jpg"
    }
}

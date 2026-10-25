"""
異次元インテリア・リノベーション - ゲームデータモジュール (審美度強化調整版)
"""

CLIENT_TYPES = {
    "magma_dragon": {
        "name": "灼熱の溶岩竜族",
        "title": "深紅の灼熱領域からの訪問者",
        "description": "超高温かつ超乾燥の過酷な環境を好む古代竜族。重厚で金属的なインテリアを好みます。",
        "min_temp": 800,
        "max_humidity": 10,
        "target_gravity": 1.5,
        "budget": 750000,
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
        "budget": 850000,
        "preferred_style": "cyberpunk_neon",
        "avatar_image": "images/clients/cyber_ai.jpg"
    },
    "deepsea_crystal": {
        "name": "深海の結晶生命体",
        "title": "海溝第10区のクリスタルアーキテクト",
        "description": "高水圧と神秘的な静寂を愛する結晶体。水温管理と高い審美性を備えた空間を求めています。",
        "min_temp": -10,
        "max_humidity": 100,
        "target_gravity": 3.0,
        "budget": 750000,
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
        "budget": 750000,
        "preferred_style": "astral_ether",
        "avatar_image": "images/clients/astral_spirit.jpg"
    }
}

FURNITURE_CATALOG = {
    # ==========================================
    # 既存の基本家具・装置（審美度強化）
    # ==========================================
    "f_magma_floor": {
        "name": "耐熱マグマタイル",
        "category": "床・壁",
        "cost": 8000,
        "temp_delta": 250,
        "humidity_delta": -15,
        "gravity_delta": 0.2,
        "aesthetic": 40,  # 20 -> 40
        "style": "industrial_magma",
        "image_path": "images/furniture/magma_floor.jpg"
    },
    "f_cool_panel": {
        "name": "超伝導冷却パネル",
        "category": "床・壁",
        "cost": 12000,
        "temp_delta": -150,
        "humidity_delta": -20,
        "gravity_delta": 0.0,
        "aesthetic": 45,  # 25 -> 45
        "style": "cyberpunk_neon",
        "image_path": "images/furniture/cool_panel.jpg"
    },
    "f_crystal_pool": {
        "name": "深海高圧ウォータープール",
        "category": "水質・環境",
        "cost": 15000,
        "temp_delta": -40,
        "humidity_delta": 40,
        "gravity_delta": 0.2,
        "aesthetic": 60,  # 35 -> 60
        "style": "crystal_ocean",
        "image_path": "images/furniture/crystal_pool.jpg"
    },
    "f_zerog_field": {
        "name": "ゼロG発生ジェネレーター",
        "category": "環境装置",
        "cost": 18000,
        "temp_delta": 0,
        "humidity_delta": 0,
        "gravity_delta": -0.5,
        "aesthetic": 55,  # 30 -> 55
        "style": "astral_ether",
        "image_path": "images/furniture/zerog_field.jpg"
    },
    "f_dark_fireplace": {
        "name": "反物質暖炉",
        "category": "大型家具",
        "cost": 22000,
        "temp_delta": 400,
        "humidity_delta": -30,
        "gravity_delta": 0.1,
        "aesthetic": 75,  # 50 -> 75
        "style": "industrial_magma",
        "image_path": "images/furniture/dark_fireplace.jpg"
    },
    "f_data_sofa": {
        "name": "量子データ同期ソファ",
        "category": "家具",
        "cost": 14000,
        "temp_delta": -20,
        "humidity_delta": 0,
        "gravity_delta": 0.0,
        "aesthetic": 65,  # 40 -> 65
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
        "aesthetic": 70,  # 45 -> 70
        "style": "crystal_ocean",
        "image_path": "images/furniture/biolum_plant.jpg"
    },
    "f_ether_chandelier": {
        "name": "エーテル気流シャンデリア",
        "category": "照明",
        "cost": 11000,
        "temp_delta": 0,
        "humidity_delta": 0,
        "gravity_delta": -0.2,
        "aesthetic": 80,  # 55 -> 80
        "style": "astral_ether",
        "image_path": "images/furniture/ether_chandelier.jpg"
    },
    
    # --- 追加特化家具 (審美度強化) ---
    "f_plasma_forge": {
        "name": "超高圧プラズマ溶鉱炉",
        "category": "大型家具",
        "cost": 28000,
        "temp_delta": 500,
        "humidity_delta": -40,
        "gravity_delta": 0.2,
        "aesthetic": 85,  # 65 -> 85
        "style": "industrial_magma",
        "image_path": "images/furniture/plasma_forge.jpg"
    },
    "f_liquid_metal_wall": {
        "name": "液体金属防壁パネル",
        "category": "床・壁",
        "cost": 16000,
        "temp_delta": 150,
        "humidity_delta": -10,
        "gravity_delta": 0.0,
        "aesthetic": 55,  # 35 -> 55
        "style": "industrial_magma",
        "image_path": "images/furniture/liquid_metal_wall.jpg"
    },
    "f_neon_matrix_display": {
        "name": "ネオン・マトリクス・ウォール",
        "category": "装飾・壁",
        "cost": 13000,
        "temp_delta": -50,
        "humidity_delta": -10,
        "gravity_delta": 0.0,
        "aesthetic": 70,  # 50 -> 70
        "style": "cyberpunk_neon",
        "image_path": "images/furniture/neon_matrix_display.jpg"
    },
    "f_cryo_sleep_pod": {
        "name": "極低温コールドスリープポッド",
        "category": "大型家具",
        "cost": 25000,
        "temp_delta": -250,
        "humidity_delta": -20,
        "gravity_delta": 0.0,
        "aesthetic": 90,  # 70 -> 90
        "style": "cyberpunk_neon",
        "image_path": "images/furniture/cryo_sleep_pod.jpg"
    },
    "f_abyssal_hydro_pillar": {
        "name": "深海圧搾ハイドロピラー",
        "category": "環境装置",
        "cost": 19000,
        "temp_delta": -30,
        "humidity_delta": 50,
        "gravity_delta": 0.4,
        "aesthetic": 65,  # 45 -> 65
        "style": "crystal_ocean",
        "image_path": "images/furniture/abyssal_hydro_pillar.jpg"
    },
    "f_coral_prism": {
        "name": "虹彩発光コーラルプリズム",
        "category": "照明",
        "cost": 10500,
        "temp_delta": 0,
        "humidity_delta": 25,
        "gravity_delta": 0.0,
        "aesthetic": 75,  # 55 -> 75
        "style": "crystal_ocean",
        "image_path": "images/furniture/coral_prism.jpg"
    },
    "f_antigrav_floating_ring": {
        "name": "反重力フローティングリング",
        "category": "大型家具",
        "cost": 21000,
        "temp_delta": 0,
        "humidity_delta": 0,
        "gravity_delta": -0.6,
        "aesthetic": 80,  # 60 -> 80
        "style": "astral_ether",
        "image_path": "images/furniture/antigrav_floating_ring.jpg"
    },
    "f_stellar_wind_harp": {
        "name": "星間微風のエーテルハープ",
        "category": "装飾品",
        "cost": 12500,
        "temp_delta": 0,
        "humidity_delta": 10,
        "gravity_delta": -0.2,
        "aesthetic": 95,  # 75 -> 95
        "style": "astral_ether",
        "image_path": "images/furniture/stellar_wind_harp.jpg"
    },

    # ==========================================
    # 1. 工業・マグマ風スタイル [8種類] (審美度強化)
    # ==========================================
    "f_magma_desk": {
        "name": "重金属製マグマデスク", "category": "机", "cost": 10000,
        "temp_delta": 150, "humidity_delta": -10, "gravity_delta": 0.0, "aesthetic": 50,  # 25 -> 50
        "style": "industrial_magma", "image_path": "images/furniture/magma_desk.jpg"
    },
    "f_magma_chair": {
        "name": "耐熱ハードアロイチェア", "category": "椅子", "cost": 7000,
        "temp_delta": 100, "humidity_delta": -5, "gravity_delta": 0.0, "aesthetic": 45,  # 20 -> 45
        "style": "industrial_magma", "image_path": "images/furniture/magma_chair.jpg"
    },
    "f_magma_heater": {
        "name": "マグマ熱交換ボイラー", "category": "湯沸かし器", "cost": 18000,
        "temp_delta": 300, "humidity_delta": -20, "gravity_delta": 0.0, "aesthetic": 60,  # 30 -> 60
        "style": "industrial_magma", "image_path": "images/furniture/magma_heater.jpg"
    },
    "f_magma_bed": {
        "name": "溶岩床カプセルベッド", "category": "ベッド", "cost": 20000,
        "temp_delta": 250, "humidity_delta": -15, "gravity_delta": 0.0, "aesthetic": 75,  # 40 -> 75
        "style": "industrial_magma", "image_path": "images/furniture/magma_bed.jpg"
    },
    "f_magma_rack": {
        "name": "アーマー収納ラック", "category": "ラック", "cost": 12000,
        "temp_delta": 120, "humidity_delta": -10, "gravity_delta": 0.0, "aesthetic": 65,  # 35 -> 65
        "style": "industrial_magma", "image_path": "images/furniture/magma_rack.jpg"
    },
    "f_magma_clock": {
        "name": "マグマ溶融クロック", "category": "時計", "cost": 8000,
        "temp_delta": 80, "humidity_delta": -5, "gravity_delta": 0.0, "aesthetic": 80,  # 45 -> 80
        "style": "industrial_magma", "image_path": "images/furniture/magma_clock.jpg"
    },
    "f_magma_bath": {
        "name": "溶岩流スパ・バス", "category": "風呂", "cost": 25000,
        "temp_delta": 500, "humidity_delta": -25, "gravity_delta": 0.0, "aesthetic": 95,  # 60 -> 95
        "style": "industrial_magma", "image_path": "images/furniture/magma_bath.jpg"
    },
    "f_magma_kitchen": {
        "name": "プラズマ溶鉱キッチン", "category": "キッチン", "cost": 22000,
        "temp_delta": 350, "humidity_delta": -20, "gravity_delta": 0.0, "aesthetic": 85,  # 50 -> 85
        "style": "industrial_magma", "image_path": "images/furniture/magma_kitchen.jpg"
    },

    # ==========================================
    # 2. サイバー・ネオン風スタイル [8種類] (審美度強化)
    # ==========================================
    "f_cyber_desk": {
        "name": "ホログラフィック・ターミナルデスク", "category": "机", "cost": 12000,
        "temp_delta": -30, "humidity_delta": -10, "gravity_delta": 0.0, "aesthetic": 55,  # 30 -> 55
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_desk.jpg"
    },
    "f_cyber_chair": {
        "name": "ゼログラビティ・コクピットチェア", "category": "椅子", "cost": 9000,
        "temp_delta": -20, "humidity_delta": -5, "gravity_delta": 0.0, "aesthetic": 50,  # 25 -> 50
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_chair.jpg"
    },
    "f_cyber_heater": {
        "name": "クライオ・ウォータークーラー", "category": "湯沸かし器", "cost": 15000,
        "temp_delta": -100, "humidity_delta": -15, "gravity_delta": 0.0, "aesthetic": 65,  # 35 -> 65
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_heater.jpg"
    },
    "f_cyber_bed": {
        "name": "データ同期型スリーピングポッド", "category": "ベッド", "cost": 22000,
        "temp_delta": -80, "humidity_delta": -20, "gravity_delta": 0.0, "aesthetic": 80,  # 50 -> 80
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_bed.jpg"
    },
    "f_cyber_rack": {
        "name": "量子サーバーラック", "category": "ラック", "cost": 16000,
        "temp_delta": -90, "humidity_delta": -20, "gravity_delta": 0.0, "aesthetic": 70,  # 40 -> 70
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_rack.jpg"
    },
    "f_cyber_clock": {
        "name": "アトミック・デジタルクロック", "category": "時計", "cost": 9000,
        "temp_delta": -10, "humidity_delta": -5, "gravity_delta": 0.0, "aesthetic": 85,  # 45 -> 85
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_clock.jpg"
    },
    "f_cyber_bath": {
        "name": "データトランス・バス", "category": "風呂", "cost": 24000,
        "temp_delta": -120, "humidity_delta": 0, "gravity_delta": 0.0, "aesthetic": 100, # 65 -> 100
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_bath.jpg"
    },
    "f_cyber_kitchen": {
        "name": "合成栄養素ディスペンサー", "category": "キッチン", "cost": 20000,
        "temp_delta": -50, "humidity_delta": -10, "gravity_delta": 0.0, "aesthetic": 90,  # 55 -> 90
        "style": "cyberpunk_neon", "image_path": "images/furniture/cyber_kitchen.jpg"
    },

    # ==========================================
    # 3. 深海・クリスタル風スタイル [8種類] (審美度強化)
    # ==========================================
    "f_crystal_desk": {
        "name": "深海石灰岩のクリアデスク", "category": "机", "cost": 11000,
        "temp_delta": -10, "humidity_delta": 20, "gravity_delta": 0.0, "aesthetic": 55,  # 30 -> 55
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_desk.jpg"
    },
    "f_crystal_chair": {
        "name": "流体モールドシェルチェア", "category": "椅子", "cost": 8000,
        "temp_delta": -10, "humidity_delta": 15, "gravity_delta": 0.0, "aesthetic": 50,  # 25 -> 50
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_chair.jpg"
    },
    "f_crystal_heater": {
        "name": "高圧スチーム・ウォーターヒーター", "category": "湯沸かし器", "cost": 16000,
        "temp_delta": 20, "humidity_delta": 30, "gravity_delta": 0.0, "aesthetic": 65,  # 35 -> 65
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_heater.jpg"
    },
    "f_crystal_bed": {
        "name": "クリスタル・ウォーターベッド", "category": "ベッド", "cost": 21000,
        "temp_delta": -20, "humidity_delta": 40, "gravity_delta": 0.0, "aesthetic": 80,  # 55 -> 80
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_bed.jpg"
    },
    "f_crystal_rack": {
        "name": "鉱石・シェル収納ラック", "category": "ラック", "cost": 13000,
        "temp_delta": -15, "humidity_delta": 25, "gravity_delta": 0.0, "aesthetic": 70,  # 40 -> 70
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_rack.jpg"
    },
    "f_crystal_clock": {
        "name": "潮汐連動ウォータークロック", "category": "時計", "cost": 9500,
        "temp_delta": -5, "humidity_delta": 15, "gravity_delta": 0.0, "aesthetic": 85,  # 50 -> 85
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_clock.jpg"
    },
    "f_crystal_bath": {
        "name": "アビス・高圧ハイドロバス", "category": "風呂", "cost": 26000,
        "temp_delta": -30, "humidity_delta": 70, "gravity_delta": 0.0, "aesthetic": 100, # 70 -> 100
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_bath.jpg"
    },
    "f_crystal_kitchen": {
        "name": "ディープシー・アクアキッチン", "category": "キッチン", "cost": 21000,
        "temp_delta": -15, "humidity_delta": 35, "gravity_delta": 0.0, "aesthetic": 90,  # 55 -> 90
        "style": "crystal_ocean", "image_path": "images/furniture/crystal_kitchen.jpg"
    },

    # ==========================================
    # 4. 次元・エーテル風スタイル [8種類] (審美度強化)
    # ==========================================
    "f_ether_desk": {
        "name": "レヴィテーション・エーテルデスク", "category": "机", "cost": 13000,
        "temp_delta": 0, "humidity_delta": 0, "gravity_delta": 0.0, "aesthetic": 65,  # 40 -> 65
        "style": "astral_ether", "image_path": "images/furniture/ether_desk.jpg"
    },
    "f_ether_chair": {
        "name": "フローティング・エーテルチェア", "category": "椅子", "cost": 10000,
        "temp_delta": 0, "humidity_delta": 0, "gravity_delta": 0.0, "aesthetic": 60,  # 35 -> 60
        "style": "astral_ether", "image_path": "images/furniture/ether_chair.jpg"
    },
    "f_ether_heater": {
        "name": "星間エーテル・サーモヒーター", "category": "湯沸かし器", "cost": 17000,
        "temp_delta": 30, "humidity_delta": 5, "gravity_delta": 0.0, "aesthetic": 75,  # 40 -> 75
        "style": "astral_ether", "image_path": "images/furniture/ether_heater.jpg"
    },
    "f_ether_bed": {
        "name": "ゼロG・フローティングベッド", "category": "ベッド", "cost": 23000,
        "temp_delta": 5, "humidity_delta": 0, "gravity_delta": 0.0, "aesthetic": 90,  # 60 -> 90
        "style": "astral_ether", "image_path": "images/furniture/ether_bed.jpg"
    },
    "f_ether_rack": {
        "name": "次元回廊サスペンドラック", "category": "ラック", "cost": 14000,
        "temp_delta": 0, "humidity_delta": 0, "gravity_delta": 0.0, "aesthetic": 80,  # 45 -> 80
        "style": "astral_ether", "image_path": "images/furniture/ether_rack.jpg"
    },
    "f_ether_clock": {
        "name": "アストラル・クロノメーター", "category": "時計", "cost": 11000,
        "temp_delta": 0, "humidity_delta": 0, "gravity_delta": 0.0, "aesthetic": 95,  # 60 -> 95
        "style": "astral_ether", "image_path": "images/furniture/ether_clock.jpg"
    },
    "f_ether_bath": {
        "name": "ゼロG・エーテルミストバス", "category": "風呂", "cost": 27000,
        "temp_delta": 10, "humidity_delta": 15, "gravity_delta": 0.0, "aesthetic": 110, # 75 -> 110
        "style": "astral_ether", "image_path": "images/furniture/ether_bath.jpg"
    },
    "f_ether_kitchen": {
        "name": "エーテル気流モレキュラーキッチン", "category": "キッチン", "cost": 22000,
        "temp_delta": 10, "humidity_delta": 10, "gravity_delta": 0.0, "aesthetic": 95,  # 60 -> 95
        "style": "astral_ether", "image_path": "images/furniture/ether_kitchen.jpg"
    }
}

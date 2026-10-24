"""
異次元インテリア・リノベーション - ゲームロジックモジュール (種族別環境適応カスタム版)
"""
import os
from data import CLIENT_TYPES, FURNITURE_CATALOG

# デフォルトの基本環境（標準室温等）
BASE_TEMP = 20
BASE_HUMIDITY = 50
BASE_GRAVITY = 1.0

def calculate_room_stats(placed_furniture_ids):
    """配置された家具から現在の部屋のステータスを計算"""
    temp = BASE_TEMP
    humidity = BASE_HUMIDITY
    gravity = BASE_GRAVITY
    total_cost = 0
    total_aesthetic = 0
    style_counts = {}

    for fid in placed_furniture_ids:
        item = FURNITURE_CATALOG.get(fid)
        if not item:
            continue
        temp += item["temp_delta"]
        humidity += item["humidity_delta"]
        gravity += item["gravity_delta"]
        total_cost += item["cost"]
        total_aesthetic += item["aesthetic"]
        
        style = item["style"]
        style_counts[style] = style_counts.get(style, 0) + 1

    # 限界値の調整
    humidity = max(0, min(100, humidity))
    gravity = max(0.0, round(gravity, 2))

    return {
        "temp": temp,
        "humidity": humidity,
        "gravity": gravity,
        "cost": total_cost,
        "aesthetic": total_aesthetic,
        "style_counts": style_counts
    }

def evaluate_renovation(client_key, placed_furniture_ids):
    """顧客の要求と現在の部屋構造から採点・レビューを判定 (種族別ロジック)"""
    client = CLIENT_TYPES[client_key]
    stats = calculate_room_stats(placed_furniture_ids)

    # 1. 予算チェック
    budget_ok = stats["cost"] <= client["budget"]
    
    # 2. 種族別の環境適応度計算カスタム分岐
    if client_key == "magma_dragon":
        # 溶岩竜族: 高温であるほど良い（最低800°C）、湿度は低いほど良い、重力は重い方が落ち着く
        temp_score = 100 if stats["temp"] >= 800 else max(0, 100 - (800 - stats["temp"]) // 2)
        hum_score = 100 if stats["humidity"] <= 10 else max(0, 100 - (stats["humidity"] - 10) * 3)
        grav_diff = abs(stats["gravity"] - 1.5)
        grav_score = max(0, int(grav_diff * 40))

    elif client_key == "cyber_ai":
        # 電脳AI: 極低温を好む（-100°C以下が理想）、湿度は完全ゼロ必須、重力は完全無重力(0G)が理想
        temp_score = 100 if stats["temp"] <= -100 else max(0, 100 - (stats["temp"] - (-100)) // 2)
        hum_score = 100 if stats["humidity"] == 0 else max(0, 100 - stats["humidity"] * 5)
        grav_score = 100 if stats["gravity"] == 0.0 else max(0, 100 - int(stats["gravity"] * 100))

    elif client_key == "deepsea_crystal":
        # 深海結晶生命体: 水温は冷たい方が良い（-10°C以下）、湿度は超高湿度（80%以上）、高水圧（重力高め）を好む
        temp_score = 100 if stats["temp"] <= -10 else max(0, 100 - (stats["temp"] - (-10)) // 2)
        hum_score = 100 if stats["humidity"] >= 80 else max(0, 100 - (80 - stats["humidity"]) * 2)
        grav_diff = abs(stats["gravity"] - 1.6)
        grav_score = max(0, int(grav_diff * 30))

    elif client_key == "astral_spirit":
        # 風使い: 常温（15〜30°C）、湿度は中程度、完全に無重力（0G）であること
        temp_score = 100 if 15 <= stats["temp"] <= 30 else max(0, 100 - abs(stats["temp"] - 22) * 2)
        hum_score = 100 if 30 <= stats["humidity"] <= 50 else max(0, 100 - abs(stats["humidity"] - 40) * 2)
        grav_score = 100 if stats["gravity"] <= 0.1 else max(0, 100 - int(stats["gravity"] * 80))

    else:
        # フォールバック（汎用計算）
        temp_score = 100 if stats["temp"] >= client["min_temp"] else max(0, 100 - (client["min_temp"] - stats["temp"]) // 10)
        hum_score = 100 if stats["humidity"] <= client["max_humidity"] else max(0, 100 - (stats["humidity"] - client["max_humidity"]) * 2)
        grav_diff = abs(stats["gravity"] - client["target_gravity"])
        grav_score = max(0, 100 - int(grav_diff * 50))

    env_score = (temp_score * 0.4) + (hum_score * 0.3) + (grav_score * 0.3)

    # 3. 好みスタイルボーナス
    pref_style = client["preferred_style"]
    style_match_count = stats["style_counts"].get(pref_style, 0)
    style_bonus = style_match_count * 12

    # 総合得点 (0 - 100)
    final_score = int((env_score * 0.5) + (min(100, stats["aesthetic"] + style_bonus) * 0.5))
    if not budget_ok:
        final_score = max(0, final_score - 35)  # 予算オーバーペナルティ

    # ランク判定
    if final_score >= 90:
        rank = "S"
        reward = int(client["budget"] * 1.6)
        comment = "「驚異的だ！我が種の遺伝子レベルで安らぐ、完璧な次元空間を構築してくれた！」"
    elif final_score >= 75:
        rank = "A"
        reward = client["budget"]
        comment = "「素晴らしい仕事だ。非常に快適で、同胞たちにもぜひ薦めたい設計だよ。」"
    elif final_score >= 50:
        rank = "B"
        reward = int(client["budget"] * 0.7)
        comment = "「なんとか過ごせそうだが、いくつか環境の微調整が必要だな。次も頼む。」"
    else:
        rank = "D"
        reward = 0
        comment = "「不快極まりない！我が種の生理条件を全く理解していない致命的な欠陥建築だ！」"

    return {
        "rank": rank,
        "score": final_score,
        "reward": reward,
        "comment": comment,
        "stats": stats,
        "budget_ok": budget_ok
    }


"""
異次元インテリア・リノベーション - ゲームロジックモジュール (高得点調整・バグ修正版)
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
    """顧客の要求と現在のお部屋構造から採点・レビューを判定 (修正版)"""
    client = CLIENT_TYPES[client_key]
    stats = calculate_room_stats(placed_furniture_ids)

    # 1. 予算チェック
    budget_ok = stats["cost"] <= client["budget"]
    
    # 2. 種族別の環境適応度計算
    if client_key == "magma_dragon":
        temp_score = 100 if stats["temp"] >= 750 else max(0, 100 - (750 - stats["temp"]) // 4)
        hum_score = 100 if stats["humidity"] <= 20 else max(0, 100 - (stats["humidity"] - 20) * 2)
        grav_diff = abs(stats["gravity"] - 1.5)
        grav_score = max(0, 100 - int(grav_diff * 20)) # 減点を少しマイルドに

    elif client_key == "cyber_ai":
        temp_score = 100 if stats["temp"] <= -80 else max(0, 100 - (stats["temp"] - (-80)) // 3)
        hum_score = 100 if stats["humidity"] <= 5 else max(0, 100 - stats["humidity"] * 3)
        grav_score = 100 if stats["gravity"] <= 0.2 else max(0, 100 - int(stats["gravity"] * 40))

    elif client_key == "deepsea_crystal":
        temp_score = 100 if stats["temp"] <= 0 else max(0, 100 - stats["temp"] // 3)
        hum_score = 100 if stats["humidity"] >= 70 else max(0, 100 - (70 - stats["humidity"]) * 2)
        grav_diff = abs(stats["gravity"] - 3.0)
        grav_score = max(0, 100 - int(grav_diff * 20))

    elif client_key == "astral_spirit":
        temp_score = 100 if 10 <= stats["temp"] <= 35 else max(0, 100 - abs(stats["temp"] - 22) * 3)
        hum_score = 100 if 20 <= stats["humidity"] <= 60 else max(0, 100 - abs(stats["humidity"] - 40) * 2)
        grav_score = 100 if stats["gravity"] <= 0.2 else max(0, 100 - int(stats["gravity"] * 40))

    else:
        temp_score = 100 if stats["temp"] >= client["min_temp"] else max(0, 100 - (client["min_temp"] - stats["temp"]) // 10)
        hum_score = 100 if stats["humidity"] <= client["max_humidity"] else max(0, 100 - (stats["humidity"] - client["max_humidity"]) * 2)
        grav_diff = abs(stats["gravity"] - client["target_gravity"])
        grav_score = max(0, 100 - int(grav_diff * 40))

    env_score = (temp_score * 0.4) + (hum_score * 0.3) + (grav_score * 0.3)

    # 3. 好みスタイルボーナス
    pref_style = client["preferred_style"]
    style_match_count = stats["style_counts"].get(pref_style, 0)
    style_bonus = style_match_count * 15

    # ★【修正ポイント】総合得点の計算：審美度・スタイルがしっかり点数に反映されるように調整
    # 総合得点 (0 - 100)
    # 環境スコアのウェイトを30%に下げ、インテリア（審美度・スタイル）のウェイトを70%に引き上げます
    aesthetic_total = min(100, (stats["aesthetic"] * 0.8) + style_bonus)
    final_score = int((env_score * 0.3) + (aesthetic_total * 0.7))
    
    if not budget_ok:
        final_score = max(0, final_score - 20)  # ペナルティを少し軽減

    # ランク判定（85点以上でSランクに届くように）
    if final_score >= 85:
        rank = "S"
        reward = int(client["budget"] * 1.8)
        comment = "「驚異的だ！我が種の遺伝子レベルで安らぐ、完璧な次元空間を構築してくれた！」"
    elif final_score >= 70:
        rank = "A"
        reward = int(client["budget"] * 1.2)
        comment = "「素晴らしい仕事だ。非常に快適で、同胞たちにもぜひ薦めたい設計だよ。」"
    elif final_score >= 45:
        rank = "B"
        reward = int(client["budget"] * 0.8)
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

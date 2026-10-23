"""
異次元インテリア・リノベーション - ゲームロジックモジュール
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
    """顧客の要求と現在の部屋構造から採点・レビューを判定"""
    client = CLIENT_TYPES[client_key]
    stats = calculate_room_stats(placed_furniture_ids)

    # 1. 予算チェック
    budget_ok = stats["cost"] <= client["budget"]
    
    # 2. 環境適応度計算 (温度・湿度・重力)
    temp_score = 100 if stats["temp"] >= client["min_temp"] else max(0, 100 - (client["min_temp"] - stats["temp"]) // 10)
    hum_score = 100 if stats["humidity"] <= client["max_humidity"] else max(0, 100 - (stats["humidity"] - client["max_humidity"]) * 2)
    grav_diff = abs(stats["gravity"] - client["target_gravity"])
    grav_score = max(0, 100 - int(grav_diff * 50))

    env_score = (temp_score + hum_score + grav_score) / 3.0

    # 3. 好みスタイルボーナス
    pref_style = client["preferred_style"]
    style_match_count = stats["style_counts"].get(pref_style, 0)
    style_bonus = style_match_count * 15

    # 総合得点 (0 - 100)
    final_score = int((env_score * 0.6) + (min(100, stats["aesthetic"] + style_bonus) * 0.4))
    if not budget_ok:
        final_score = max(0, final_score - 40)  # 予算オーバー大減点

    # ランク判定
    if final_score >= 90:
        rank = "S"
        reward = int(client["budget"] * 1.5)
        comment = "「素晴らしい！我が種の生理条件を満たす完璧な空間だ。異次元建築大賞に推薦しよう！」"
    elif final_score >= 75:
        rank = "A"
        reward = client["budget"]
        comment = "「素晴らしい仕事だ。非常に快適で、同胞たちにもぜひ薦めたい設計だよ。」"
    elif final_score >= 50:
        rank = "B"
        reward = int(client["budget"] * 0.7)
        comment = "「なんとか過ごせそうだが、いくつか気になる点があるな。今後に期待する。」"
    else:
        rank = "D"
        reward = 0
        comment = "「不快だ！環境条件が壊滅的で到底住めたものではない！やり直しを求める！」"

    return {
        "rank": rank,
        "score": final_score,
        "reward": reward,
        "comment": comment,
        "stats": stats,
        "budget_ok": budget_ok
    }

def generate_room_prompt(client_key, placed_furniture_ids):
    """Gemini API用の画像生成プロンプトを作成"""
    client = CLIENT_TYPES[client_key]
    items = [FURNITURE_CATALOG[fid]["name"] for fid in placed_furniture_ids if fid in FURNITURE_CATALOG]
    items_str = ", ".join(items) if items else "Minimalist empty futuristic shell"

    prompt = (
        f"A ultra-detailed, cinematic interior architecture photo of a room designed for {client['name']}. "
        f"Style: {client['preferred_style']}, Sci-Fi fantasy interior design. "
        f"Key furniture and elements included: {items_str}. "
        f"Atmosphere: Highly immersive, futuristic lighting, high resolution, 8k, Unreal Engine 5 render style."
    )
    return prompt

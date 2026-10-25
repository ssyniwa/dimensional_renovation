"""
『異次元インテリア・リノベーション』 Main Streamlit Application (グリッド画像配置対応版)
"""
import os
import streamlit as st
from data import CLIENT_TYPES, FURNITURE_CATALOG
from models import calculate_room_stats, evaluate_renovation
# スタイルの日本語名マッピング
STYLE_NAMES = {
    "industrial_magma": "🔥 工業・マグマ風 (溶岩竜族向け)",
    "cyberpunk_neon": "🤖 サイバー・ネオン風 (電脳AI向け)",
    "crystal_ocean": "💎 深海・クリスタル風 (深海生命体向け)",
    "astral_ether": "🌌 次元・エーテル風 (風使い向け)"
}
# ページ基本設定
st.set_page_config(
    page_title="異次元インテリア・リノベーション",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS
st.markdown("""
<style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 4px; font-size: 12px; padding: 2px; }
    .client-card {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
    }
    .grid-cell {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 5px;
        text-align: center;
        min-height: 90px;
    }
</style>
""", unsafe_allow_html=True)

# セッション状態の初期化
if "funds" not in st.session_state:
    st.session_state.funds = 100000
if "reputation" not in st.session_state:
    st.session_state.reputation = 0
if "current_client" not in st.session_state:
    st.session_state.current_client = "magma_dragon"
if "grid_furniture" not in st.session_state:
    st.session_state.grid_furniture = [["" for _ in range(6)] for _ in range(6)]

# サイドバー：事務所パラメータ & 顧客選択
st.sidebar.title("🌌 次元建築事務所")
st.sidebar.metric("所持金", f"{st.session_state.funds:,} Cr")
st.sidebar.metric("事務所の評判", f"Rank {st.session_state.reputation // 100 + 1} ({st.session_state.reputation} pt)")

st.sidebar.divider()
st.sidebar.subheader("📋 依頼者を選択")

for key, client_data in CLIENT_TYPES.items():
    col_ico, col_btn = st.sidebar.columns([1, 3])
    with col_ico:
        if os.path.exists(client_data["avatar_image"]):
            st.image(client_data["avatar_image"], width=35)
    with col_btn:
        if st.button(client_data["name"], key=f"btn_{key}"):
            st.session_state.current_client = key

# メイン表示エリア
client = CLIENT_TYPES[st.session_state.current_client]

st.title("異次元インテリア・リノベーション")
st.caption("マルチバースの異世界顧客に向けた、理想の次元空間設計シミュレーション")

col_client, col_grid, col_stats = st.columns([0.7, 2.0, 0.7])

# --- カラム1: クライアント情報 & 家具カタログ ---
with col_client:
    st.subheader("👤 クライアント要件")
    if os.path.exists(client["avatar_image"]):
        st.image(client["avatar_image"], use_container_width=True)
    st.markdown(f"""
    <div class="client-card">
        <h3>{client['name']}</h3>
        <p><b>{client['title']}</b></p>
        <p>{client['description']}</p>
        <hr style="border-color:#30363d;">
        <p>💰 <b>予算:</b> {client['budget']:,} Cr</p>
        <p>🔥 <b>必須最低温度:</b> {client['min_temp']}°C 以上</p>
        <p>💧 <b>許容最大湿度:</b> {client['max_humidity']}% 以下</p>
        <p>🌌 <b>目標重力:</b> {client['target_gravity']} G</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧰 家具カタログ")
    selected_furniture = st.selectbox(
        "配置するアイテムを選択",
        options=list(FURNITURE_CATALOG.keys()),
        format_func=lambda x: FURNITURE_CATALOG[x]['name']
    )
    
    item_info = FURNITURE_CATALOG[selected_furniture]
    if os.path.exists(item_info["image_path"]):
        st.image(item_info["image_path"], use_container_width=True)
    
    # ★スタイルの表示を追加
    style_display = STYLE_NAMES.get(item_info["style"], item_info["style"])
    st.markdown(f"**所属スタイル**: {style_display}")

    st.info(f"**{item_info['name']}**\n\nコスト: {item_info['cost']:,} Cr\n温度 {item_info['temp_delta']:+}°C | 湿度 {item_info['humidity_delta']:+}% | 重力 {item_info['gravity_delta']:+}G | 審美度 +{item_info['aesthetic']}")
# --- カラム2: 6x6 グリッド設計室 (画像配置対応) ---
with col_grid:
    st.subheader("📐 6×6 空間デザイン設計")
    click_mode = st.radio("アクション", ["選択マスに配置", "マスを撤去"], horizontal=True)

    st.markdown("<p style='font-size: 12px; color: #8b949e;'>下のグリッドから操作したいマスをクリックしてください。</p>", unsafe_allow_html=True)

    # 6x6 グリッドの描画
    for r in range(6):
        cols = st.columns(6)
        for c in range(6):
            cell_item = st.session_state.grid_furniture[r][c]
            
            with cols[c]:
                # セル内の表示コンテナ
                if cell_item and cell_item in FURNITURE_CATALOG:
                    img_path = FURNITURE_CATALOG[cell_item]["image_path"]
                    if os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.markdown(f"<div style='text-align:center; font-size:10px;'>[配置済]</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='grid-cell' style='height:90px; display:flex; align-items:center; justify-content:center; color:#30363d;'>+</div>", unsafe_allow_html=True)
                
                # 各セルのクリックボタン
                btn_label = "❌" if cell_item else "📍"
                if st.button(btn_label, key=f"grid_btn_{r}_{c}"):
                    if click_mode == "選択マスに配置":
                        st.session_state.grid_furniture[r][c] = selected_furniture
                    else:
                        st.session_state.grid_furniture[r][c] = ""
                    st.rerun()

    if st.button("🗑️ 空間を全クリア"):
        st.session_state.grid_furniture = [["" for _ in range(6)] for _ in range(6)]
        st.rerun()

placed_ids = [cell for row in st.session_state.grid_furniture for cell in row if cell]
current_stats = calculate_room_stats(placed_ids)

# --- カラム3: リアルタイム環境モニター & 施工 ---
with col_stats:
    st.subheader("📊 リアルタイム環境状態")

    c1, c2 = st.columns(2)
    c1.metric("現在温度", f"{current_stats['temp']}°C", 
              delta=current_stats['temp'] - client['min_temp'],
              delta_color="normal" if current_stats['temp'] >= client['min_temp'] else "inverse")
    
    c2.metric("現在湿度", f"{current_stats['humidity']}%",
              delta=client['max_humidity'] - current_stats['humidity'],
              delta_color="normal" if current_stats['humidity'] <= client['max_humidity'] else "inverse")

    c3, c4 = st.columns(2)
    c3.metric("重力レベル", f"{current_stats['gravity']} G", delta=round(current_stats['gravity'] - client['target_gravity'], 2))
    c4.metric("審美スコア", f"{current_stats['aesthetic']} pt")

    cost_percentage = min(1.0, current_stats['cost'] / client['budget'])
    st.write(f"**使用予算**: {current_stats['cost']:,} / {client['budget']:,} Cr")
    st.progress(cost_percentage)

    st.divider()

    if st.button("🔨 リノベーション施工・レビュー実行", type="primary"):
        result = evaluate_renovation(st.session_state.current_client, placed_ids)
        
        st.subheader("📝 施工評価結果")
        st.markdown(f"### 評価ランク: **{result['rank']}** (スコア: {result['score']}/100)")
        st.write(result['comment'])

        if result['rank'] in ["S", "A", "B"]:
            st.success(f"報酬 {result['reward']:,} Cr を獲得しました！")
            st.session_state.funds += result['reward']
            st.session_state.reputation += result['score'] // 10
        else:
            st.error("評価が不十分なため、報酬は支払われませんでした。")

       

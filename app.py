"""
『異次元インテリア・リノベーション』 Main Streamlit Application (画像対応版)
"""
import streamlit as st
from data import CLIENT_TYPES, FURNITURE_CATALOG
from models import calculate_room_stats, evaluate_renovation, generate_room_prompt

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
    .stButton>button { width: 100%; border-radius: 6px; }
    .client-card {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
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
        st.image(client_data["avatar_image"], width=40)
    with col_btn:
        if st.button(client_data["name"], key=f"btn_{key}"):
            st.session_state.current_client = key

# メイン表示エリア
client = CLIENT_TYPES[st.session_state.current_client]

st.title("異次元インテリア・リノベーション")
st.caption("マルチバースの異世界顧客に向けた、理想の次元空間設計シミュレーション")

col_client, col_grid, col_stats = st.columns([1, 1.3, 1])

# --- カラム1: クライアント情報 ---
with col_client:
    st.subheader("👤 クライアント要件")
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
    st.image(item_info["image_path"], use_container_width=True)
    st.info(f"**{item_info['name']}**\n\nコスト: {item_info['cost']:,} Cr\n温度 {item_info['temp_delta']:+}°C | 湿度 {item_info['humidity_delta']:+}% | 重力 {item_info['gravity_delta']:+}G | 審美度 +{item_info['aesthetic']}")

# --- カラム2: 6x6 グリッド設計室 ---
with col_grid:
    st.subheader("📐 6×6 空間デザイン設計")
    
    click_mode = st.radio("マス操作モード", ["設置", "撤去"], horizontal=True)

    grid_container = st.container()
    for r in range(6):
        cols = grid_container.columns(6)
        for c in range(6):
            cell_item = st.session_state.grid_furniture[r][c]
            # グリッドボタンには家具の名前略称やアイコンを表示（画像は入りませんが、設置されていると名前を表示）
            label = FURNITURE_CATALOG[cell_item]["name"][:2] if cell_item else "・"
            
            if cols[c].button(label, key=f"cell_{r}_{c}"):
                if click_mode == "設置":
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

        prompt = generate_room_prompt(st.session_state.current_client, placed_ids)
        with st.expander("🎨 生成ビジュアルプロンプト (Gemini API用)"):
            st.code(prompt, language="text")

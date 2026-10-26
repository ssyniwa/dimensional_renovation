"""
『異次元インテリア・リノベーション』 Main Streamlit Application (家具配置修正版)
"""
import os
import streamlit as st
from data import CLIENT_TYPES, FURNITURE_CATALOG
from models import calculate_room_stats, evaluate_renovation

# スタイルの日本語名マッピング
STYLE_NAMES = {
    "industrial_magma": "🔥 工業・マグマ風",
    "cyberpunk_neon": "🤖 サイバー・ネオン風",
    "crystal_ocean": "💎 深海・クリスタル風",
    "astral_ether": "🌌 次元・エーテル風 "
}

# ページ基本設定
st.set_page_config(
    page_title="異次元インテリア・リノベーション",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSSによるデザインの洗練
st.markdown("""
<style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 6px; font-size: 13px; font-weight: bold; padding: 6px; }
    .client-card {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
    }
    .panel-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 15px;
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

# セッション状態の初期izing
if "funds" not in st.session_state:
    st.session_state.funds = 100000
if "reputation" not in st.session_state:
    st.session_state.reputation = 0
if "current_client" not in st.session_state:
    st.session_state.current_client = list(CLIENT_TYPES.keys())[0]

# 依頼ごとのグリッド状態管理用（クライアント別グリッド辞書）
if "client_grids" not in st.session_state:
    st.session_state.client_grids = {key: [["" for _ in range(6)] for _ in range(6)] for key in CLIENT_TYPES.keys()}

# 現在編集中のグリッドをアクティブなクライアントに同期
if "grid_furniture" not in st.session_state:
    st.session_state.grid_furniture = st.session_state.client_grids[st.session_state.current_client]

# 完了した依頼の記録
if "completed_clients" not in st.session_state:
    st.session_state.completed_clients = {key: False for key in CLIENT_TYPES.keys()}

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
        label = f"{client_data['name']} ✅" if st.session_state.completed_clients[key] else client_data["name"]
        if st.button(label, key=f"btn_{key}"):
            st.session_state.client_grids[st.session_state.current_client] = st.session_state.grid_furniture
            st.session_state.current_client = key
            st.session_state.grid_furniture = st.session_state.client_grids[key]
            st.rerun()

# --- 全ての依頼が完了したかのチェック ---
all_completed = all(st.session_state.completed_clients.values())

if all_completed:
    st.title("🎉 全ての依頼が完了しました！")
    st.markdown("### 🏆 結果発表：各クライアントの設計ルーム一覧")
    st.write("マルチバースの全顧客が大満足する素晴らしい建築実績を残しました。以下は各依頼で保存された空間デザインです。")

    for key, client_data in CLIENT_TYPES.items():
        st.divider()
        st.subheader(f"👤 依頼者: {client_data['name']}")
        saved_grid = st.session_state.client_grids[key]
        
        for r in range(6):
            cols = st.columns(6)
            for c in range(6):
                cell_item = saved_grid[r][c]
                with cols[c]:
                    if cell_item and cell_item in FURNITURE_CATALOG:
                        img_path = FURNITURE_CATALOG[cell_item]["image_path"]
                        if os.path.exists(img_path):
                            st.image(img_path, use_container_width=True)
                        else:
                            st.markdown(f"<div style='text-align:center; font-size:8px;'>[配置済]</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='grid-cell' style='height:40px; display:flex; align-items:center; justify-content:center; color:#30363d; font-size:10px;'>-</div>", unsafe_allow_html=True)
    
    st.stop()

# --- 通常のメイン表示エリア ---
client = CLIENT_TYPES[st.session_state.current_client]

st.title("異次元インテリア・リノベーション")
st.caption("マルチバースの異世界顧客に向けた、理想の次元空間設計シミュレーション")

# 3カラムの配分 (左: クライアント要件 | 中央: グリッド設計 | 右: カタログ & モニター)
col_client, col_grid, col_right = st.columns([0.8, 2.0, 0.8])

# --- カラム3 (右側) の家具カタログを先に処理し、選択中の家具を確定させる ---
with col_right:
    st.subheader("🧰 家具カタログ")
    with st.container():
        style_filter_options = ["すべて"] + list(STYLE_NAMES.keys())
        selected_style = st.selectbox(
            "スタイルで絞り込み",
            options=style_filter_options,
            format_func=lambda x: "すべて表示" if x == "すべて" else STYLE_NAMES[x],
            key="selected_style_filter"
        )
        
        if selected_style == "すべて":
            filtered_furniture_keys = list(FURNITURE_CATALOG.keys())
        else:
            filtered_furniture_keys = [
                fid for fid, info in FURNITURE_CATALOG.items() 
                if info["style"] == selected_style
            ]
        
        if filtered_furniture_keys:
            # key="selected_furniture" を指定してセッションステートに保存
            selected_furniture = st.selectbox(
                "配置するアイテムを選択",
                options=filtered_furniture_keys,
                format_func=lambda x: FURNITURE_CATALOG[x]['name'],
                key="selected_furniture"
            )
            
            item_info = FURNITURE_CATALOG[selected_furniture]
            
            col_img, col_desc = st.columns([1, 1.2])
            with col_img:
                if os.path.exists(item_info["image_path"]):
                    st.image(item_info["image_path"], use_container_width=True)
            with col_desc:
                style_display = STYLE_NAMES.get(item_info["style"], item_info["style"])
                st.markdown(f"<p style='font-size:11px; margin:0;'><b>スタイル</b>: {style_display}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size:11px; margin:0;'><b>コスト</b>: {item_info['cost']:,} Cr</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size:11px; margin:0;'><b>効果</b>: 温{item_info['temp_delta']:+d} / 湿{item_info['humidity_delta']:+d}% / 重力{item_info['gravity_delta']:+.2f}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size:11px; margin:0;'><b>審美度</b>: +{item_info['aesthetic']} pt</p>", unsafe_allow_html=True)
        else:
            st.warning("このスタイルに該当する家具はありません。")
            selected_furniture = None

# --- カラム1: クライアント要件 ---
with col_client:
    st.subheader("👤 クライアント要件")
    if os.path.exists(client["avatar_image"]):
        st.image(client["avatar_image"], use_container_width=True)
    
    status_badge = "<p style='color: #3fb950; font-weight: bold;'>【 依頼達成済み (Rank A以上) 】</p>" if st.session_state.completed_clients[st.session_state.current_client] else ""
    
    st.markdown(f"""<div class="client-card">
<h3>{client['name']}</h3>
{status_badge}
<p><b>{client['title']}</b></p>
<p>{client['description']}</p>
<hr style="border-color:#30363d;">
<p>💰 <b>予算:</b> {client['budget']:,} Cr</p>
<p>🔥 <b>必須最低温度:</b> {client['min_temp']}°C 以上</p>
<p>💧 <b>許容最大湿度:</b> {client['max_humidity']}% 以下</p>
<p>🌌 <b>目標重力:</b> {client['target_gravity']} G</p>
</div>""", unsafe_allow_html=True)

# --- カラム2: 6x6 グリッド設計室（右側のカタログ処理後に描画するため、選択家具が確実に取得できる） ---
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
                if cell_item and cell_item in FURNITURE_CATALOG:
                    img_path = FURNITURE_CATALOG[cell_item]["image_path"]
                    if os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.markdown(f"<div style='text-align:center; font-size:10px;'>[配置済]</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='grid-cell' style='height:75px; display:flex; align-items:center; justify-content:center; color:#30363d;'>+</div>", unsafe_allow_html=True)
                
                btn_label = "❌" if cell_item else "📍"
                if st.button(btn_label, key=f"grid_btn_{r}_{c}"):
                    if click_mode == "選択マスに配置":
                        # st.session_state.get("selected_furniture") を使って確実に現在選ばれている家具を取得
                        chosen_item = st.session_state.get("selected_furniture")
                        if chosen_item:
                            st.session_state.grid_furniture[r][c] = chosen_item
                    else:
                        st.session_state.grid_furniture[r][c] = ""
                    
                    st.session_state.client_grids[st.session_state.current_client] = st.session_state.grid_furniture
                    st.rerun()

    if st.button("🗑️ 空間を全クリア"):
        st.session_state.grid_furniture = [["" for _ in range(6)] for _ in range(6)]
        st.session_state.client_grids[st.session_state.current_client] = st.session_state.grid_furniture
        st.rerun()

placed_ids = [cell for row in st.session_state.grid_furniture for cell in row if cell]
current_stats = calculate_room_stats(placed_ids)

# --- カラム3 (続き): 環境モニター & 施工 ---
with col_right:
    st.divider()

    st.subheader("📊 環境モニター & 施工")

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

    if st.button("🔨 リノベーション施工・レビュー実行", type="primary"):
        result = evaluate_renovation(st.session_state.current_client, placed_ids)
        
        st.subheader("📝 施工評価結果")
        st.markdown(f"### 評価ランク: **{result['rank']}** (スコア: {result['score']}/100)")
        st.write(result['comment'])

        if result['rank'] in ["S", "A", "B"]:
            st.success(f"報酬 {result['reward']:,} Cr を獲得しました！")
            st.session_state.funds += result['reward']
            st.session_state.reputation += result['score'] // 10
            
            if result['rank'] in ["S", "A"]:
                st.session_state.completed_clients[st.session_state.current_client] = True
                st.session_state.client_grids[st.session_state.current_client] = st.session_state.grid_furniture
                st.success("🎯 依頼達成！空間デザインが保存されました。")
        else:
            st.error("評価が不十分なため、報酬は支払われませんでした。")

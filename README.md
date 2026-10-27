# dimensional_renovation
# 🌌 異次元インテリア・リノベーション (Multi-verse Interior Renovation)

> マルチバースの風変わりな異世界顧客に向けた、理想の次元空間設計シミュレーションゲーム！

[![Python](https://img.shields.io/badge/Python-3.8%23-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎮 ゲーム概要

『異次元インテリア・リノベーション』は、物理法則や好みが全く異なるマルチバースの住民たちからの依頼を受け、**6×6のグリッド空間**に家具や環境装置を配置して理想のインテリアを作り上げるパズル＆シミュレーションゲームです。

溶岩の海で生きる竜族、サーバーの熱暴走に悩む電脳AI、完全無重力で暮らす精霊たちなど、クセの強い顧客の要望を満たし、最高評価（Sランク）を目指しましょう！

---

## ✨ 主な特徴

- 🏢 **個性豊かな異世界の顧客たち**
  - 灼熱の溶岩竜族、電脳空間のAI精神体、深海の結晶生命体、次元の風使いに加え、ハイブリッドな要求を持つ新種族など多数登場！
- 🧰 **4つのスタイル＆40種類以上の家具**
  - 「工業・マグマ風」「サイバー・ネオン風」「深海・クリスタル風」「次元・エーテル風」の4系統から自由に家具を選択。
- 🎯 **環境シミュレーション＆戦略的パズル**
  - 配置した家具によって**温度・湿度・重力・審美スコア**がリアルタイムに変動。
  - 顧客が「必ず入れてほしい指定家具（ランダム選出）」を配置するとボーナス点獲得！
- 🏆 **全クリア・実績保存システム**
  - 全ての依頼でAランク以上を獲得すると、各クライアントの設計ルームが記録された「結果発表画面」に移行します。

---

## 🚀 遊び方（ローカル実行手順）

1. **リポジトリのクローン**
   ```bash
   git clone [https://github.com/your-username/multiverse-interior-renovation.git](https://github.com/your-username/multiverse-interior-renovation.git)
   cd multiverse-interior-renovation
   ```
2. **依存ライブラリのインストール**
   ```bash
   pip install streamlit
   ```
3. **アプリケーションの起動**
   ```bash
   streamlit run app.py
   ```
## 🛠️ 技術スタック
- 言語: Python
- フレームワーク: Streamlit
- 状態管理: st.session_state によるリアルタイム・マルチクライアント管理
## 📜 ライセンス
このプロジェクトは MIT ライセンスのもとで公開されています。詳細については LICENSE をご覧ください。

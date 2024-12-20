import streamlit as st
import pandas as pd

#タイトル
st.title("調子判定アプリ(デモ版)")

#タブでページを切り替え
tab1, tab2 = st.tabs(["平常時データ入力", "今日のデータ入力"])

#平常時データ入力タブ
with tab1:
    st.subheader("平常時のデータを入力してください")
    平熱 = st.number_input("平熱を入力してください", min_value=35.0, max_value=42.0, value=36.5, step=0.1)
    平睡眠時間 = st.number_input("平常時の睡眠時間を入力してください", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
    平脈拍 = st.number_input("平常時の脈拍を入力してください", min_value=0, max_value=200, value=70, step=1)

    if st.button("平常時データを記録"):
        #データをセッションに保存
        st.session_state["平常時データ"] = pd.DataFrame({
            "項目": ["体温", "睡眠時間", "脈拍"],
            "数値": [平熱, 平睡眠時間, 平脈拍]
        })
        st.success("平常時のデータを記録しました")

    #記録済みデータの表示
    if "平常時データ" in st.session_state:
        st.write("記録済みの平常時データ:")
        st.write(st.session_state["平常時データ"])

#今日のデータ入力タブ
with tab2:
    st.subheader("今日のデータを入力してください")
    体温 = st.number_input("体温を入力してください", min_value=35.0, max_value=42.0, value=36.5, step=0.1)
    睡眠時間 = st.number_input("睡眠時間を入力してください", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
    脈拍 = st.number_input("脈拍を入力してください", min_value=0, max_value=200, value=70, step=1)
    体の不調 = st.checkbox("体調不良ですか？")

    if st.button("今日の調子を判定"):
        #平常時データが記録されていない場合の処理
        if "平常時データ" not in st.session_state:
            st.error("まずは平常時のデータを記録してください（左のタブで入力）")
        else:
            #平常時データと今日のデータを比較
            df1 = st.session_state["平常時データ"]
            df2 = pd.DataFrame({
                "項目": ["体温", "睡眠時間", "脈拍"],
                "数値": [体温, 睡眠時間, 脈拍]
            })

            #判定条件
            判定結果 = []
            if 体温 >= 37.5:
                判定結果.append("体温が平均以上")
            if 体の不調:
                判定結果.append("体の不調にチェックが入っている")
            if 脈拍 > 80:
                判定結果.append("脈拍が平均より速い")

            #体温、体の不調、脈拍に基づく判定
            if len([c for c in 判定結果 if c in ["体温が平均以上", "体の不調にチェックが入っている", "脈拍が平均より速い"]]) >= 2:
                st.error("体調が悪いようです。もし風邪症状がある場合は病院に行くことをおすすめします。")
            #睡眠時間の判定
            elif 睡眠時間 < 5:
                st.warning("睡眠時間が足りていません。ゆっくりと睡眠を取ることをおすすめします。")
            #脈拍の判定
            elif 脈拍 < 60 or 脈拍 > 81:
                if 脈拍 <= 50 or 脈拍 >= 120:
                    st.error("脈拍が正常範囲外です。病院で診察を受けることをおすすめします。")
                else:
                    st.warning("脈拍が正常範囲外です。安静にすることをおすすめします。")
            else:
                st.success("問題ありません！良い一日を過ごして下さい！")
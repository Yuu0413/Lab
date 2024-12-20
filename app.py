import streamlit as st
import pandas as pd

#タイトルと見出し
st.title("Demo App")
st.header("This is test App")

#数値の平均値を記録
st.subheader("平均値")
df1=pd.DataFrame({
    "項目":["体温","睡眠時間"],
    "数値" : [36.3,7.3]
})

#その日の数値を入力
st.subheader("今日の数値を入力して下さい")
temp=st.number_input("体温を入力して下さい", min_value=35.0, max_value=40.0, value=36.3, step=0.1)
sle_time=st.number_input("睡眠時間を入力して下さい", min_value=0.0, max_value=24.0, value=7.5, step=0.01)

#入力された数値を記録
df2=pd.DataFrame({
    "項目":["体温","睡眠時間"],
    "数値" : [temp,sle_time]
})

#df1とdf2を比較
if st.button("平均と比較"):
    df_merge=pd.merge(df1, df2, on="項目",suffixes=("_df1","_df2"))
    df_merge["数値差"]=df_merge["数値_df2"]-df_merge["数値_df1"]
    st.write(df_merge)

#数値差の値によってコメントを表示
    if df_merge["数値差"][0]>0.5:
        st.write("体温が高いです。")
    elif df_merge["数値差"][0]<-0.5:
        st.write("体温が低いです。")
    else:
        st.write("体温は平均値です。")

    if df_merge["数値差"][1]>1.0:
        st.write("睡眠時間が短いです。")
    elif df_merge["数値差"][1]<-1.0:
        st.write("睡眠時間が長いです。")
    else:
        st.write("睡眠時間は平均値です。")
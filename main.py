import streamlit as st

st.title("🧮 シンプル計算機")

# 入力フィールド
num1 = st.number_input("1つ目の数値", value=0.0, step=1.0)
num2 = st.number_input("2つ目の数値", value=0.0, step=1.0)

# 演算の選択
operation = st.selectbox("演算を選んでください", ["足し算", "引き算", "掛け算", "割り算"])

# 計算ボタン
if st.button("計算"):
    try:
        if operation == "足し算":
            result = num1 + num2
        elif operation == "引き算":
            result = num1 - num2
        elif operation == "掛け算":
            result = num1 * num2
        elif operation == "割り算":
            if num2 == 0:
                raise ZeroDivisionError("0で割ることはできません。")
            result = num1 / num2
        st.success(f"結果: {result}")
    except Exception as e:
        st.error(f"エラー: {e}")

import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')

# st.write('Display Image')
# st.write('Unteractive Windgets')

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition


# 〇サイドバーを作成する〇
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味は', text, 'です。'
# 'コンディション:', condition

# 〇2カラムレイアウトを作成する〇
# 左側→ボタンを追加　右側→テキストを追加
# left_columu, right_columu = st.beta_columns(2)
# button = left_columu.button('右カラムに文字を表示')
# if button:
#     right_columu.write('ここは右カラムです')

# 〇エキスパンダー使いする〇
# expander1 = st.beta_expander('問い合わせ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.beta_expander('問い合わせ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.beta_expander('問い合わせ3')
# expander3.write('問い合わせ3の回答')

# 〇プログレスバーの表示〇
st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'特に意味もなく読み込んでるフリをしています'

expander1 = st.beta_expander('会社概要')
expander1.write('わいわいわい')
expander2 = st.beta_expander('代表挨拶')
expander2.write('特になし')
expander3 = st.beta_expander('問い合わせはこちら')
expander3.write('電話番号:〇〇〇〇〇')


# インタラクティブとは
# 「双方向」とか「対話式」とか、そんな感じの用語。少しかみ砕くと
# 「一方通行ではなく、相互にやり取りできる感じ」のことを意味していますが
# 今回は動的な変化を起こしてくれる、と思ってもらえればOK

# option = st.selectbox(
#     'あなたの好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、', option, 'です。'



# if st.checkbox('Show Image'):
#     img = Image.open('LUCK.png')
#     st.image(img, caption='LUCK', use_column_width=True)


# df = pd.DataFrame({
#    '1列目': [1, 2, 3, 4],
#    '2列目': [10, 20, 30, 40],
# })

# write() = 表の細かい設定はできない
# st.write(df)

# dataframe() = 表の縦横の長さを指定できる
# dataframe() = 「動的」なテーブルを使いたい
# highlight_max() = 列または行の中で最大なものをハイライトする
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

# table() = static(静的)なテーブルを作りたい時に使用する
# table() = 「静的」なテーブルを使いたい
# st.table(df.style.highlight_max(axis=0))


# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.write(df)
# st.line_chart(df)


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)


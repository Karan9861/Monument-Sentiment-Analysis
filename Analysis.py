import streamlit as st
import pandas as pd

# st.markdown("### Top Five Monuments")

df1 = pd.read_csv('review_scores.csv')

st.write('### Top Five Monuments Based on User Ratings')
st.write('  ')

st.write(df1.groupby('Monument').agg({'Rating':'mean'}).sort_values(ascending=False, by='Rating')[:5])
# st.write(df.sort_values(by='Rating', ascending=False)['Monument'].unique()[:5])
# st.write(df1.groupby('Monument').agg({'TextBlob Analysis':'value_counts'}))
st.sidebar.markdown("# Top 5 Monuments 🏛")

st.write('### Top Five Monuments Based on Vader Sentiment Scores')
st.write('  ')

st.write(df1.groupby('Monument').agg({'Vader Sentiment':'mean'}).sort_values(ascending=False, by='Vader Sentiment')[:5])
# st.write(' ### Top Rated Monuments')
# st.write(df.sort_values(by='Rating', ascending=False)['Monument'].unique()[:5])

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Monument Sentiment Analysis')

df1 = pd.read_csv('review_scores.csv')

def piecahrt():
    
    idex = []
    
    for index,value in enumerate(gropuby['TextBlob Analysis'].index):
        if monument in value:
            # print(index, value)
            idex.append(index)
          
    s = []  
    
    for i in idex:
        s.append(int(gropuby.values[i]))
            
    sizes = s
    labels = ['Postitive', 'Neutral','Negative' ]
    explode = (0.1, 0, 0) 
    
    fig1, ax1 = plt.subplots()
    fig1.set_facecolor('#0E1117')
    ax1.pie(sizes,explode=explode, labels=labels,textprops={'color':"w"}, autopct='%1.1f%%', startangle=0, radius=1)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    return sizes,fig1
    # st.pyplot(fig1)  


monument = st.selectbox('Select the Monument', df1['Monument'].unique(), on_change=piecahrt)

gropuby = df1.groupby('Monument').agg({'TextBlob Analysis':'value_counts'})

sizes,pc = piecahrt()


st.pyplot(pc)  



# st.sidebar.markdown("# Select the Monument 🎈")


# st.dataframe(df)
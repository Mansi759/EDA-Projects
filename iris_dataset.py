import pandas as pd 
import streamlit as st 

data=pd.read_csv("iris.csv")

st.sidebar.header("Choose a specie :")
choose = st.sidebar.radio("",options=["Setosa","Versicolor","Virginica"])



### SETOSA 

if choose=="Setosa":
    st.image("setosa.png",width=400)
    setosa=data.loc[data["species"]=="setosa"]
    
    st.header("Inforation.....")
    choice = st.selectbox("", options=["sepal length","sepal width","petal length","petal width"])
    
    if choice =="sepal length":
        sepal_length = setosa["sepal_length"].mean()
        st.write("Average sepal length value is :", sepal_length)
    elif choice =="sepal width":
        sepal_width = setosa["sepal_width"].mean()
        st.write("Average sepal width value is :", sepal_width)
    elif choice =="petal length":
        petal_length = setosa["petal_length"].mean()
        st.write("Average petal length value is :", petal_length) 
    elif choice =="petal width":
        petal_width = setosa["petal_width"].mean()
        st.write("Average petal width value is :", petal_width)
    else:
        st.write("Select at least one option...")
        
        
## VERSICOLOR 

if choose=="Versicolor":
    st.image("versicolor.png",width=400)
    setosa=data.loc[data["species"]=="versicolor"]
    
    st.header("Inforation.....")
    choice = st.selectbox("", options=["sepal length","sepal width","petal length","petal width"])
    
    if choice =="sepal length":
        sepal_length = setosa["sepal_length"].mean()
        st.write("Average sepal length value is :", sepal_length)
    elif choice =="sepal width":
        sepal_width = setosa["sepal_width"].mean()
        st.write("Average sepal width value is :", sepal_width)
    elif choice =="petal length":
        petal_length = setosa["petal_length"].mean()
        st.write("Average petal length value is :", petal_length) 
    elif choice =="petal width":
        petal_width = setosa["petal_width"].mean()
        st.write("Average petal width value is :", petal_width)
    else:
        st.write("Select at least one option...")
        
        
### VIRGINICA 

if choose=="Virginica":
    st.image("virginica.png",width=400)
    setosa=data.loc[data["species"]=="virginica"]
    
    st.header("Inforation.....")
    choice = st.selectbox("", options=["sepal length","sepal width","petal length","petal width"])
    
    if choice =="sepal length":
        sepal_length = setosa["sepal_length"].mean()
        st.write("Average sepal length value is :", sepal_length)
    elif choice =="sepal width":
        sepal_width = setosa["sepal_width"].mean()
        st.write("Average sepal width value is :", sepal_width)
    elif choice =="petal length":
        petal_length = setosa["petal_length"].mean()
        st.write("Average petal length value is :", petal_length) 
    elif choice =="petal width":
        petal_width = setosa["petal_width"].mean()
        st.write("Average petal width value is :", petal_width)
    else:
        st.write("Select at least one option...")


    
    
    
    
    
    
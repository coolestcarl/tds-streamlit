import streamlit as st

st.title ("TDS")
st.header ("Streamlit Assignment")
st.subheader ("Week 8")

st.write ("""
    ##### Due date for this assignment: 
    2024-04-21, 23:59 IST.
    
    ##### Assignment Brief
    You may submit any number of times before the due date. The final submission will be considered for grading.
    Build a streamlit application for the following use case and host the application using streamlit cloud.


    #### UseCase:
    Find the largest among the 3 given numbers (value greater than the other two).
    """)

st.write ("Enter a the values of variables $x_1$, $x_2$, $x_3$")

x = list ()
for i in range (3):
    x_i = st.number_input (f"$x_{i + 1}$", value=0.0)
    x.append (x_i)

largest = x[0]
index = 0
for i in range (1, 3):
    if x[i] > largest:
        largest = x[i]
        index = i

st.write (f"The largest number is $x_{index + 1} = $ ", largest)

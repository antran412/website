# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:58:54 2024

@author: hantr
"""

import streamlit as st

from predict_page import show_predict_page
from graph_page import show_graph

page = st.sidebar.selectbox("Visualzation or Prediction", ("Prediction","Visualization"))

if page == "Visualization":
    show_graph()
else:
    show_predict_page()

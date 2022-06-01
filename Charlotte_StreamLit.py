# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:23:07 2022

@author: Eric
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import plotly.figure_factory as ff
sns.set()

import time
from datetime import datetime
from datetime import date

import streamlit as st

import warnings
warnings.filterwarnings('ignore')

px.set_mapbox_access_token(open("mapbox_access_token.txt").read())

cmpd_df = pd.read_csv("trunc_cmpd_incidents.csv")

crashes_df = pd.read_csv("updated_crash_incidents.csv")

clt_nc_df = pd.read_csv("clt_311_requests.csv")

#Setting the page to wide config
st.set_page_config(layout="wide", page_title="City of Charlotte Geospatial Dashboard")

st.markdown("<h1 style='text-align: center; color: forestgreen;'>City of Charlotte Geospatial Dashboard</h1>", unsafe_allow_html=True)
st.write("Below are maps for serious traffic accidents, Charlotte police incidents, and 311 call requests. Please enter in the parameters given to obtain your desired maps.")

st.title("Serious Traffic Incidents Map")

with st.container():
    
    row1_1, row1_2 = st.columns((2, 3))

    with row1_1:
        st.write("Enter the date ranges for which to plot serious traffic accidents")
        start_date = st.date_input(label = "Select a starting date from which to plot Traffic Incident data", 
                                   value = date(2019, 1, 1),
                                   min_value = pd.to_datetime(crashes_df['DATE'].min()),
                                   max_value = pd.to_datetime(crashes_df['DATE'].max()),
                                   key=1)
    
        end_date = st.date_input(label = "Select an ending date to plot Traffic Incident data up to", 
                                 value = date(2020, 1, 1),
                                 min_value = pd.to_datetime(crashes_df['DATE'].min()),
                                 max_value = pd.to_datetime(crashes_df['DATE'].max()),
                                 key=2)


    with row1_2:
        st.write("Enter the categories of crashes you wish to plot")
        crash_types = crashes_df['CRASH_TYPE'].unique().tolist()
    
        symbols = st.multiselect("Select Crash Types to plot",
                                 options = crash_types,
                                 default = ['Pedestrian', 'Ran off road right'],
                                 key=3)

crashes_display = crashes_df[crashes_df['DATE'].between(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))]
crashes_display = crashes_display[crashes_display['CRASH_TYPE'].isin(symbols)]

fig = px.scatter_mapbox(crashes_display, lat="LATITUDE", lon="LONGITUDE", color="CRASH_TYPE", 
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, title='Traffic Accidents', width=1000, height=1000)

st.plotly_chart(fig)

st.title("CMPD Incidents Map")
    
with st.container():
    
    row2_1, row2_2 = st.columns((2, 4))

    with row2_1:
        st.write("Enter the date ranges for which to plot CMPD incidents")
        start_date_2 = st.date_input(label = "Select a starting date from which to plot CMPD Incident data", 
                                   value = date(2019, 1, 1),
                                   min_value = pd.to_datetime(cmpd_df['DATE_INCIDENT_BEGAN'].min()),
                                   max_value = pd.to_datetime(cmpd_df['DATE_INCIDENT_BEGAN'].max()),
                                   key=4)
    
        end_date_2 = st.date_input(label = "Select an ending date to plot CMPD Incident data up to", 
                                 value = date(2020, 1, 1),
                                 min_value = pd.to_datetime(cmpd_df['DATE_INCIDENT_BEGAN'].min()),
                                 max_value = pd.to_datetime(cmpd_df['DATE_INCIDENT_BEGAN'].max()),
                                 key=5)
        
        st.write("Enter the CMPD Divisions you wish to include in the plot")
        divi = cmpd_df['CMPD_PATROL_DIVISION'].unique().tolist()
    
        symbols_divi = st.multiselect("Select CMPD Division to include",
                                 options = divi,
                                 default = ['Metro'],
                                 key=8)  


    with row2_2:
        st.write("Enter Category & Locations below")
        desc = cmpd_df['HIGHEST_NIBRS_DESCRIPTION'].unique().tolist()
    
        symbols_desc = st.multiselect("Enter the categories of CMPD incidents you wish to plot",
                                 options = desc,
                                 default = ['Shoplifting', 'Burglary/B&E'],
                                 key=6)    
        
        locations = cmpd_df['PLACE_TYPE_DESCRIPTION'].unique().tolist()
    
        symbols_loc = st.multiselect("Enter the categories of locations where CMPD incidents took place to plot",
                                 options = locations,
                                 default = ['Retail'],
                                 key=7)  

cmpd_display = cmpd_df[cmpd_df['DATE_INCIDENT_BEGAN'].between(start_date_2.strftime('%Y-%m-%d'), end_date_2.strftime('%Y-%m-%d'))]
cmpd_display = cmpd_display[cmpd_display['HIGHEST_NIBRS_DESCRIPTION'].isin(symbols_desc)]
cmpd_display = cmpd_display[cmpd_display['PLACE_TYPE_DESCRIPTION'].isin(symbols_loc)]
cmpd_display = cmpd_display[cmpd_display['CMPD_PATROL_DIVISION'].isin(symbols_divi)]

fig_2 = px.scatter_mapbox(cmpd_display, lat="LATITUDE_PUBLIC", lon="LONGITUDE_PUBLIC", color='HIGHEST_NIBRS_DESCRIPTION', 
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, title='CMPD Incidents', width=1000, height=1000)


st.plotly_chart(fig_2)

st.title("Charlotte 311 Reports Map")
    
with st.container():
    
    row3_1, row3_2 = st.columns((2, 4))

    with row3_1:
        st.write("Enter the date ranges for which to plot 311 call requests")
        start_date_3 = st.date_input(label = "Select a starting date from which to plot 311 Requests", 
                                   value = date(2019, 1, 1),
                                   min_value = pd.to_datetime(clt_nc_df['RECEIVED_DATE'].min()),
                                   max_value = pd.to_datetime(clt_nc_df['RECEIVED_DATE'].max()),
                                   key=9)
    
        end_date_3 = st.date_input(label = "Select an ending date to plot 311 Requests up to", 
                                 value = date(2020, 1, 1),
                                 min_value = pd.to_datetime(clt_nc_df['RECEIVED_DATE'].min()),
                                 max_value = pd.to_datetime(clt_nc_df['RECEIVED_DATE'].max()),
                                 key=10)


    with row3_2:
        st.write("Enter Department & Request Type below")
        dept = clt_nc_df['DEPARTMENT'].unique().tolist()
    
        symbols_dept = st.multiselect("Enter the Departments you wish to plot 311 Requests from",
                                 options = dept,
                                 default = ['Solid Waste Services'],
                                 key=11)    
        
        requests = clt_nc_df['REQUEST_TYPE'].unique().tolist()
    
        symbols_req = st.multiselect("Enter the Request Type(s) you wish to include in the map",
                                 options = requests,
                                 default = ['MISSED RECYCLING'],
                                 key=12)  


clt_311_display = clt_nc_df[clt_nc_df['RECEIVED_DATE'].between(start_date_3.strftime('%Y-%m-%d'), end_date_3.strftime('%Y-%m-%d'))]
clt_311_display = clt_311_display[clt_311_display['DEPARTMENT'].isin(symbols_dept)]
clt_311_display = clt_311_display[clt_311_display['REQUEST_TYPE'].isin(symbols_req)]

fig_3 = px.scatter_mapbox(clt_311_display, lat="LATITUDE", lon="LONGITUDE", color='REQUEST_TYPE', 
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, title='311 Requests', width=1000, height=1000)


st.plotly_chart(fig_3)


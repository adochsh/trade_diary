import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table
import datetime
#@st.cache(suppress_st_warning=True)
def app():
    st.header('Main !Page')
    df = create_table().copy()


#### BODY ####
    columns = st.multiselect( "", list(df.columns) )
    if not columns:
        st.dataframe(df, width=4000, height=700) #.style.highlight_max(axis=0)
    else:
        data = df[columns].drop_duplicates().reset_index() #data /= 1000000.0
        st.dataframe(data.drop(columns='index').sort_index() )
        st.write('You selected:', columns)



### Filters ###
    st.sidebar.header("Filters:")
    # Identifier
    with st.sidebar.expander("Identifier", expanded=False):
        # articles = {"LM code , ADEO code , EAN"}
        articles_join = df['LM code'].unique().tolist()+df['ADEO code'].unique().tolist()+df['GTIN (EAN)'].unique().tolist()
        articles = st.multiselect("LM code , ADEO code , EAN", articles_join)
        # orders = {"OC , RMS , ADEO order"}
        orders_join = df['RMS Order No.'].unique().tolist()+df['ADEO Order No.'].unique().tolist()+df['OC No.'].unique().tolist()
        orders = st.multiselect( "OC , RMS , ADEO order", orders_join)
        # suppliers
        supp_codes = st.multiselect( "Supplier code", df['Supplier Code'].unique())
        supp_names = st.multiselect( "Supplier name", df['Supplier name'].unique())
        # tm names
        tm_name = st.multiselect( "TM name", ['Dexter','and ..'])
        # deps and subdeps
        deps = st.multiselect( "Dep", df['Department'].unique())
        subdeps = st.multiselect( "SubDep", df['Subdepartment'].unique())
        # articles' eng names
        desc_eng = st.multiselect( "Article description", df['Description in English'].unique())

    # Shipment
    with st.sidebar.expander("Shipment", expanded=False):
        # invoices
        invoices = st.multiselect( "Invoice", df['Invoice No.'].unique())
        # containers
        containers = st.multiselect( "Container", df['Container No.'].unique())
        # custom declarations
        cds = st.multiselect( "Custom declaration", df['Customs Declaration No.'].unique())
        # swb
        swb = st.multiselect( "SWB", df['SWB'].unique())
        # port of discharge
        discharge_port = st.multiselect( "Port of discharge", df['Port of discharge'].unique())
        # wh
        wh = st.multiselect( "WH", df['WH'].unique())

    # Dates
    with st.sidebar.expander("Dates", expanded=False):
        # RDD from POL
        #df['RDD from POL']= pd.to_datetime(df['RDD from POL']).dt.date
        #dates = st.date_input('RDD from POL',df['RDD from POL'].unique())
        start_date, end_date = st.date_input('RDD from POL', (datetime.date(2021, 7, 6),datetime.date(2022, 7, 6)))
        # if start_date < end_date:
        #     pass
        # else:
        #     st.error('Error: Date')
            # greater than the start date and smaller than the end date
        # mask = (df['CREATEDDATE'] > start_date) & (df['CREATEDDATE'] <= end_date)
        # df = df.loc[mask]
        #     # And display the result!

    # Specialists
    with st.sidebar.expander("Specialists", expanded=False):
        # Approvision
        appro = st.multiselect( "Approvision", df['Approvision Specialist'].unique())
        # Import
        imports = st.multiselect( "Import", df['Import Specialist'].unique())



    st.header('Hellowworl!')
##### OTHERs

    # Column names
    # with st.sidebar.expander("Columns", expanded=True):
        # date_col, target_col = input_columns(config, readme, df, load_options)
        # df = format_date_and_target(df, date_col, target_col, config, load_options)

    # Filtering
    # with st.sidebar.expander("Filtering", expanded=False):
        # dimensions = input_dimensions(df, readme, config)
        # df, cols_to_drop = filter_and_aggregate_df(df, dimensions, config, date_col, target_col)
        # print_removed_cols(cols_to_drop)

    # if not columns:
    #     st.error("Please select at least one country.")
    # else:
    #     data = df[['Accumulated delay'
    #                 , 'ADEO code'
    #                 # , 'Date of 1st acceptance in WH',
    #                 # , 'Date of 2nd acceptance in WH'
    #                 ]] #data /= 1000000.0
    #     st.write(data.sort_index())
    #     data = data.T.reset_index()
    #     data = pd.melt(data, id_vars=["index"])
    #     #.rename( columns={"index": "year", "value": "Gross Agricultural Product ($B)"})
    #     chart = (
    #         alt.Chart(data)
    #         .mark_area(opacity=0.3)
    #         .encode(
    #             x="ADEO code:T",
    #             y=alt.Y("Accumulated delays", stack=None),
    #             color="Region:N",
    #         )
    #     )
    #     st.altair_chart(chart, use_container_width=True)

    color = st.color_picker('Pick A Color', '#51bb51')
    st.write('The current color is', color)





    # data = {'feature_1':  ['A','B','A','C','D','M','A','B','A','C'],
    #         'feature_2': ['Zack','Hassan','Ali','Hassan','Hassan','Ali','Zack','Hassan','Hassan','Hassan'],
    #         'feature_3': [0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    #         'feature_4': [10,10,10,10,10,20,20,20,20,20],
    #         'Result_count': [1000,2000,3330,100,250,20,990,160,10,200]}
    # df = pd.DataFrame(data)
    #
    #
    # #feature_1 filters
    # feature_1_val = df["feature_1"].unique()
    # feature_1ed = st.sidebar.selectbox('feature_1', feature_1_val)
    # #filter out data
    # df = df[(df["feature_1"] == feature_1ed)]
    #
    # #feature_2 filters
    # feature_2_val = df["feature_2"].unique()
    # feature_2 = st.sidebar.selectbox('feature_2', feature_2_val)
    # #filter out data
    # df = df[(df["feature_2"] == feature_2)]
    #
    # #feature_3 filters
    # feature_3_val = df["feature_3"].unique()
    # feature_3 = st.sidebar.selectbox('feature_3', feature_3_val)
    # #filter out data
    # df = df[(df["feature_3"] == feature_3)]
    #
    #
    # #feature_4 filter
    # feature_4_val = df["feature_4"].unique()
    # feature_4 = st.sidebar.selectbox('feature_4',feature_4_val)
    # #filter out data
    # df = df[(df["feature_4"] == feature_4)]
    #
    # df = df[(df["feature_1"] == feature_1ed) | (df["feature_2"] == feature_2)]
    # st.write(df)
    #

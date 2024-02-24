import streamlit as st
from data_fetch import get_realtime_stock_data, get_historical_stock_data
import plotly.graph_objs as go


# st.markdown(
#     """
#     <style>
#     .full-width {
#         width: 100%;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.write(
#     """
#     <style>
#     div[data-testid="stBlock"] {
#         padding: 10px !important;
#         margin: 10px 0px !important;
#         border-radius: 10px !important;
#         box-shadow: 0px 0px 5px 2px #ccc !important;
#     }
#     </style>
#     """
# )



# Title and description
st.title('Real-time Stock Market Dashboard')
st.write('This dashboard provides live real-time data and historical data of Indian stock market.')

# Stock selection
stock_symbol = st.text_input('Enter Stock Name:')

# Data range selection
date_range = st.selectbox('Select data range:', ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])

# Fetch and display stock data
if stock_symbol:
    # Real-time data
    st.subheader('Real-time Data:')
    real_time_data = get_realtime_stock_data(stock_symbol)
    st.write(real_time_data)
    
    # Historical data
    st.subheader('Historical Data:')
    historical_data = get_historical_stock_data(stock_symbol, date_range)
    st.write(historical_data)
    
    # Plot real-time data
    st.subheader('Real-time Data Chart:')
    fig = go.Figure(data=go.Scatter(x=real_time_data.index, y=real_time_data['Close']))
    fig.update_layout(title=f'Real-time Data for {stock_symbol}', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)

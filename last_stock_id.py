import streamlit as st

# Initialize the session state for the last stock ID if it doesn't exist
if 'last_stock_id' not in st.session_state:
    st.session_state.last_stock_id = None

# Function to set the stock ID in the session state
def set_stock_id(stock_id):
    st.session_state.last_stock_id = stock_id

# Function to get the last stock ID from the session state
def get_last_stock_id():
    return st.session_state.last_stock_id

# Streamlit app interface
st.title('Stock ID Tracker')

# Input for the stock ID
stock_id_input = st.text_input('Enter Stock ID:')

# Button to set the stock ID
if st.button('Set Stock ID'):
    set_stock_id(stock_id_input)
    st.success(f'Stock ID set to: {stock_id_input}')

# Display the last stock ID
if get_last_stock_id() is not None:
    st.write(f'Last Stock ID: {get_last_stock_id()}')
else:
    st.write('No Stock ID set yet.')

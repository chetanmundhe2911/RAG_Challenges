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
stock_id_input = st.text_input('Enter Stock ID (leave blank to keep last ID):')

# Button to update the stock ID
if st.button('Update Stock ID'):
    if stock_id_input:
        set_stock_id(stock_id_input)
        st.success(f'Stock ID updated to: {stock_id_input}')
    else:
        st.warning('No stock ID entered. Keeping the last stock ID.')

# Display the current stock ID
current_stock_id = get_last_stock_id()
if current_stock_id:
    st.write(f'Current Stock ID: {current_stock_id}')
else:
    st.write('No Stock ID set yet.')

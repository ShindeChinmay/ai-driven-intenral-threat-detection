import pandas as pd
import numpy as np
import streamlit as st

# Simulate or load data
data = pd.DataFrame({
    'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='T'),
    'user': np.random.choice(['user1', 'user2', 'user3'], size=100),
    'action': np.random.choice(['login', 'file_access', 'logout'], size=100)
})

# Add a dummy 'feature1' column
data['feature1'] = np.random.randint(1, 100, size=len(data))

# Ensure 'timestamp' is in datetime format
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Set 'timestamp' as the index
data.set_index('timestamp', inplace=True)

# Debugging: Print DataFrame structure in Streamlit
st.write("DataFrame after setting 'timestamp' as index:", data.head())

# Plot the line chart
st.line_chart(data['feature1'])

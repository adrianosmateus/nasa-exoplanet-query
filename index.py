import pandas as pd
import streamlit as st

filename = '20210125.csv'

# Load the data from file, ignoring failing lines and comment lines
df = pd.read_csv(filename, error_bad_lines=False, comment='#')

# Parse the content to JSON format
planets_json = df.to_json()

# Creating the data visualization using Streamlit
st.title("Planets listing by NASA")

# Show the amount of data loaded from the file
st.sidebar.info("The total of loaded content with no errors is {}".format(df.shape[0]))

# Show a select box using the data frame headers
search_column = st.sidebar.selectbox('Serch by column:', df.columns)

# Show a search input so the user can filter data
search_term = st.sidebar.text_input("Search by term:", '')

# Filter the data from the source frame to a new data frame
nf = df[df[search_column].str.contains(search_term)]
#nf = df.set_index(search_column).filter(like='ball', axis=0)


# Show the content from the data source
st.write(nf)

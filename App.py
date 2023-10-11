import streamlit as st

custom_css = f"""
    <style>
        .css-6qob1r.e1akgbir3 {{
            color: firebrick;
            background-color: black;
        }}
        .css-1629p8f.eqr7zpz1 >h2{{
            color: firebrick;
        }}
    </style>
"""


# Apply custom CSS to change sidebar width
st.markdown(custom_css, unsafe_allow_html=True)
# custom_css = f"""
#     <style>
#         h2 {{
#             color: firebrick;
#         }}
#     </style>
# """

# # Apply custom CSS to change header color
# st.markdown(custom_css, unsafe_allow_html=True)



# Input fields
st.sidebar.header("Packaging Estimation Sheet")
st.sidebar.header("Client Bio")
col1,col2=st.sidebar.columns(2)
client_name=col1._text_input("Client Name")
CSR=col2._text_input("CSR Name")
col1,col2=st.sidebar.columns(2)
client_email=col1._text_input("Client Email")
Phone=col2._text_input("Phone Number")



st.sidebar.header("Sheet Size")
col1, col2 = st.sidebar.columns(2)
W_S=col1.number_input("W_Sheet", min_value=0)

# st.write(W_S)

L_S=col2.number_input("L_Sheet", min_value=0)
# st.sidebar.header("Material")

Material = col1.selectbox(
    "Material",
    ["Bux Board", "Bleach Card", "Art Card", "Kraf",]
)
gsm = col2.number_input("GSM", min_value=0)
up = col1.number_input("Box Uping", min_value=0)
Req_Q = col2.number_input("Required Quantity", min_value=0)

st.sidebar.header("Print Size")
col1, col2 = st.sidebar.columns(2)
W_P=col1.number_input("W_Print", min_value=0)
L_P=col2.number_input("L_Print", min_value=0)
# st.sidebar.header("Material")

Material_p = col1.selectbox(
    "Material_Printing",
    ["Bux Board", "Bleach Card", "Art Card", "Kraf",]
)
gsm_p = col2.number_input("GSM_Print", min_value=0)
up_p = col1.number_input("Box Uping_Print", min_value=0)
Req_Q_p= col2.number_input("Required Quantity_P", min_value=0)

st.sidebar.header("Corrugation")
col1, col2 = st.sidebar.columns(2)
stock = col1.selectbox(
    "Corrugation Material",
    ["L1", "E Flute", "B Flute"]
)

pasting = col2.selectbox(
    "Corrugation Pasting",
    ["Single Side", "Double Side",]
)

st.sidebar.header("Printing Colors")
col1, col2, col3 = st.sidebar.columns(3)
process_color = col1.selectbox(
    "Process Color",
    [1, 2,3,4]
)
pantone_color=col2.number_input("Pantone Color", min_value=0)
matallic_color=col3.number_input("Matallic Color", min_value=0)


st.sidebar.header("Add-Ons")
col1, col2, col3,col4 = st.sidebar.columns(4)
Foil = col1.selectbox(
    "Foiling",
    ["Yes","No",]
)
Deboss = col2.selectbox(
    "Deboss",
     ["Yes","No",]
)
Emboss = col3.selectbox(
    "Emboss",
     ["Yes","No",]
)
UV = col4.selectbox(
    "UV",
     ["Yes","No",]
)

window_die_cut=st.sidebar.selectbox(
    "Window Diecut",
     ["None","With PVC","Without PVC",])
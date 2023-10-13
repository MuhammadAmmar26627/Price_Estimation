import streamlit as st
import pandas as pd
import math
st.set_page_config(layout="wide")
def Lamination_sheets_calculator(sheet):
    if sheet <= 100:
        return math.ceil(sheet * 0.5 + sheet)
    elif sheet <= 200:
        return math.ceil(sheet * 0.5 + sheet)
    elif sheet <= 300:
        return math.ceil(sheet * 0.4 + sheet)
    elif sheet <= 400:
        return math.ceil(sheet * 0.2 + sheet)
    elif sheet <= 500:
        return math.ceil(sheet * 0.2 + sheet)
    elif sheet <= 600:
        return math.ceil(sheet * 0.18 + sheet)
    elif sheet >= 650 and sheet <= 1000:
        return math.ceil(sheet * 0.15 + sheet)
    elif sheet >= 1000 and sheet <= 1500:
        return math.ceil(sheet * 0.1 + sheet)
    elif sheet >= 1500 and sheet <= 2000:
        return math.ceil(sheet * 0.12 + sheet)
    elif sheet >= 2000 and sheet <= 3000:
        return math.ceil(sheet * 0.08 + sheet)
    elif sheet >= 3000 and sheet <= 4000:
        return math.ceil(sheet * 0.04 + sheet)
    elif sheet >= 4000 and sheet <= 7000:
        return math.ceil(sheet * 0.04 + sheet)
    elif sheet > 7000:
        return math.ceil(sheet * 0.025 + sheet)
    else:
        return sheet

def Print_Sheet_calculator(sheet):
    if sheet <= 100:
        return math.ceil(sheet * 1.5 + sheet)
    elif sheet <= 200:
        return math.ceil(sheet * 1.0 + sheet)
    elif sheet <= 300:
        return math.ceil(sheet * 0.65 + sheet)
    elif sheet <= 400:
        return math.ceil(sheet * 0.45 + sheet)
    elif sheet <= 500:
        return math.ceil(sheet * 0.35 + sheet)
    elif sheet <= 600:
        return math.ceil(sheet * 0.3 + sheet)
    elif sheet >= 700 and sheet <= 1000:
        return math.ceil(sheet * 0.17 + sheet)
    elif sheet >= 1000 and sheet <= 1500:
        return math.ceil(sheet * 0.15 + sheet)
    elif sheet >= 1500 and sheet <= 2000:
        return math.ceil(sheet * 0.15 + sheet)
    elif sheet >= 2000 and sheet <= 3000:
        return math.ceil(sheet * 0.1 + sheet)
    elif sheet >= 3000 and sheet <= 4000:
        return math.ceil(sheet * 0.08 + sheet)
    elif sheet >= 4000 and sheet <= 5000:
        return math.ceil(sheet * 0.07 + sheet)
    elif sheet <= 6000:
        return math.ceil(sheet * 0.05 + sheet)
    elif sheet <= 7000:
        return math.ceil(sheet * 0.05 + sheet)
    elif sheet <= 8000:
        return math.ceil(sheet * 0.05 + sheet)
    elif sheet <= 9000:
        return math.ceil(sheet * 0.045 + sheet)
    elif sheet <= 10000:
        return math.ceil(sheet * 0.0475 + sheet)
    elif sheet > 10000:
        return math.ceil(sheet * 0.0425 + sheet)


def find_machine_size(w, l,rate_df):
    
    if (w <= 12 and l <= 17) or (l <= 12 and w <= 17):
        machine = rate_df[rate_df.Machine_size == "12x17"]
        # print("12x17")
    elif (w <= 23 and l <= 17) or (l <= 23 and w <= 17):
        machine = rate_df[rate_df.Machine_size == "23x17"]
        # print("23x17")
    elif (w <= 25 and l <= 36) or (l <= 25 and w <= 36):
        machine = rate_df[rate_df.Machine_size == "25x36"]
        # print("25x36")
    elif (w <= 28 and l <= 40) or (l <= 28 and w <= 40):
        machine = rate_df[rate_df.Machine_size == "28x40"]
        # print("28x40")
    elif (w <= 35 and l <= 45) or (l <= 35 and w <= 45):
        machine = rate_df[rate_df.Machine_size == "35x45"]
        # print("35x45")
    elif (w <= 40 and l <= 56) or (l <= 40 and w <= 56):
        machine = rate_df[rate_df.Machine_size == "40x56"]
        # print("40x56")
    else:
        # print("No matching machine size found.")
        machine = None
    return machine
    # st.dataframe(machine, hide_index=True)

def Printing_Calculator(Machine,cmyk,pms,met,print_sheet):
    try:
        # as printing rate is per 1170 and below list show us that if printing rate is 1400 and we have sheets 3350 it is below 4387 so we multply its index+1 to rate
        sheet_list =[1170, 2310, 3300, 4387, 5360, 6405, 7500, 8500, 9532, 10529, 11500, 12500, 13553, 14595, 15742, 16680, 17723, 18765, 19808, 20850, 21893, 22935, 23978, 25020, 26167, 27105, 28252, 29294, 30233, 31275, 32318, 33360, 34403, 35485, 36488, 37634, 38677, 39719]
        for i in sheet_list:
            if print_sheet<=i:
                factor=sheet_list.index(i)+1
                break
            # CMYK=Machine["CMYK"].iloc[0, 0]
        return Machine["CMYK"].iloc[0]*cmyk*factor,Machine["PMS"].iloc[0]*pms*factor,Machine["Met"].iloc[0]*met*factor
    except:
        return 0,0,0

@st.cache_data
def load_data(file,sheet_name):
    # Load your data into a DataFrame (replace 'your_data.csv' with your actual data source)
    data = pd.read_excel(file,sheet_name=sheet_name)
    data.fillna(0,inplace=True)
    return data
rate_df=load_data("rate_database.xlsx",sheet_name="Sheet1")
material_df=load_data("rate_database.xlsx",sheet_name="Sheet2")
lab_df=load_data("rate_database.xlsx",sheet_name="Sheet3")
# custom_css = f"""
#     <style>
#         .css-6qob1r.e1akgbir3 {{
#             color: firebrick;
#             background-color: black;
#         }}
#         .css-1629p8f.eqr7zpz1 >h2{{
#             color: firebrick;
#         }}
#     </style>
# """


# Apply custom CSS to change sidebar width
# st.markdown(custom_css, unsafe_allow_html=True)
# custom_css = f"""
#     <style>
#         h2 {{
#             color: firebrick;
#         }}
#     </style>
# """

# # Apply custom CSS to change header color
# st.markdown(custom_css, unsafe_allow_html=True)


######## Client Data ###########


# Input fields
st.sidebar.header("Packaging Estimation Sheet")
st.sidebar.header("Client Bio")
col1,col2=st.sidebar.columns(2)
client_name=col1._text_input("Client Name")
CSR=col2._text_input("CSR Name")
col1,col2=st.sidebar.columns(2)
client_email=col1._text_input("Client Email")
Phone=col2._text_input("Phone Number")


########### Sheet Data (Size) ########



st.sidebar.header("Sheet Size")
col1, col2 = st.sidebar.columns(2)
W_S=col1.number_input("W_Sheet", min_value=0.0)

# st.write(W_S)

L_S=col2.number_input("L_Sheet", min_value=0.0)
# st.sidebar.header("Material")

Material = col1.selectbox(
    "Material",
    ["Bux Board", "Bleach Card", "Art Card", "Kraf",]
)
gsm = col2.number_input("GSM", min_value=0,value=300)
up = col1.number_input("Box Uping", min_value=1)
Req_Q = col2.number_input("Required Quantity", min_value=0)

st.sidebar.header("Print Size")
col1, col2 = st.sidebar.columns(2)
W_P=col1.number_input("W_Print", min_value=0.0)
L_P=col2.number_input("L_Print", min_value=0.0)
# st.sidebar.header("Material")

# Material_p = col1.selectbox(
#     "Material_Printing",
#     ["Bux Board", "Bleach Card", "Art Card", "Kraf",]
# )
# gsm_p = col2.number_input("GSM_Print", min_value=0)
# up_p = col1.number_input("Box Uping_Print", min_value=0)
# Req_Q_p= col2.number_input("Required Quantity_P", min_value=0)

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
    [0,1,2,3,4,5,6,7,8,]
)
pantone_color=col2.number_input("Pantone Color", min_value=0)
matallic_color=col3.number_input("Matallic Color", min_value=0)


st.sidebar.header("Add-Ons")
col1, col2, col3,col4 = st.sidebar.columns(4)
Foil = col1.selectbox(
    "Foiling",
    ["No","Yes",],
     index=0
)
Deboss = col2.selectbox(
    "Deboss",
     ["No","Yes",],
     index=0
)
Emboss = col3.selectbox(
    "Emboss",
     ["No","Yes",],
     index=0
)
UV = col4.selectbox(
    "UV",
     ["No","Yes",],
     index=0
)

window_die_cut=st.sidebar.selectbox(
    "Window Diecut",
     ["None","With PVC","Without PVC",])
############ Lamination ##########
st.sidebar.header("Lamination")
col1,col2=st.sidebar.columns(2)
inside=col1.selectbox(
    "Inside Lamination",
     ["None","Matte","Gloss","Soft Touch","Varnish",])
inside=col2.selectbox(
    "Outside Lamination",
     ["None","Matte","Gloss","Soft Touch","Varnish",])
# Lamination_side=st.sidebar.selectbox(
#     "Window Lamination_Side",
#      ["Single","Double","Without PVC",])






############ Additional Expense ##########

st.sidebar.header("Additional Expense")
col1, col2, col3 = st.sidebar.columns(3)
Mics = col1.number_input("Micsellneus", min_value=0)
Profit_margin = col2.number_input("Profit Margin", min_value=0)
project_difficulty = col3.number_input("Project Difficulty", min_value=0)


### disply Machine size
machine_rate=find_machine_size(W_S,L_S,rate_df)
st.dataframe(machine_rate,hide_index=True)
Sheets=Req_Q/up
print_sheet=Print_Sheet_calculator(Sheets)
st.write(f'print_sheet: {print_sheet}')
laminate_sheet=Lamination_sheets_calculator(Sheets)
st.write(f'laminate_sheet: {laminate_sheet}')
process_color_rate,pantone_color_rate,matallic_color_rate=Printing_Calculator(machine_rate,process_color,pantone_color,matallic_color,print_sheet)
st.write(process_color_rate,pantone_color_rate,matallic_color_rate)






col1, col2, col3 = st.columns(3)
col1.metric("Total Amount", "10000", "Misc Profit Marig Difficulty")
# col2.metric("Wind", "9 mph", "-8%")
col3.metric("Cost Per Piece", "40", "")

col1, col2, col3 = st.columns(3)
col1.metric("Material Cost", "5000", "")
col2.metric("Labour Cost", "5000", "")
col3.metric("Material + Labour Cost", "10000 Rs", "")



col1,col2=st.columns(2)
n_rows=13
height = int(35.2*(n_rows+1))
col1.header("Material Cost")
col1.dataframe(material_df, width=700, height=410,hide_index=True)
col2.header("Labour Cost")
col2.dataframe(lab_df, width=700, height=height,hide_index=True)

# rate_df=pd.read_excel("rate_database.xlsx",sheet_name="Sheet1")
# rate_df

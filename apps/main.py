import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest


#
SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1OggIj5S9J9W6_caUe_1zzt2u5uezCY2H70o12TusEmw"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"

@st.experimental_singleton()
def connect_to_gsheet():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )

    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http = httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector


def get_data(gsheet_connector) -> pd.DataFrame:
    values = ( gsheet_connector.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{SHEET_NAME}!A:E",).execute())
    df = pd.DataFrame(values["values"])
    df.columns = df.iloc[0]
    df = df[1:]
    return df

def add_row_to_gsheet(gsheet_connector, row) -> None:
    gsheet_connector.values().append( spreadsheetId=SPREADSHEET_ID, range=f"{SHEET_NAME}!A:E", body=dict(values=row)
                                        , valueInputOption="USER_ENTERED", ).execute()

#################### START ############################################################################################
def app():
    st.title("📉 Trade diary!")

    gsheet_connector = connect_to_gsheet()

    st.sidebar.write( f"This app stores your data of deals into [Google Sheet]({GSHEET_URL}) to read or store data.")

    #### Insert forms
    form = st.form(key="annotation")
    with form:
        cols = st.columns((1, 1))
        author = cols[0].text_input("Your name:")
        currency = cols[1].selectbox("Сurrency:", ["USD", "BTS", "ETH", "USDT", "USDC", "BNB"], index=2)
        comment = st.text_area("Reason of buying:")
        cols = st.columns(3)
        date = cols[0].date_input("Deal date")
        price = cols[1].number_input("Price of a deal:", step=0.5)
        amount = cols[2].number_input("Amount of a deal:", step=0.5)
        submitted = st.form_submit_button(label="Submit")

    #### Submit the data into google sheet
    if submitted:
        add_row_to_gsheet(gsheet_connector, [[author, currency, comment, str(date), price, amount]],)
        st.success("Thanks! Your trade deal was recorded.")
        st.balloons()

    #### See all records from google sheet
    expander = st.expander("See all records")
    with expander:
        st.write(f"Open original [Google Sheet]({GSHEET_URL})")
        st.dataframe(get_data(gsheet_connector))

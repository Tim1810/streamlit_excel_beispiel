import streamlit as st
from berechnung import berechne_excel


st.set_page_config(
    page_title="Berechnung zu Excel",
    page_icon="📊"
)

st.title("Einfache Berechnung mit Excel-Ausgabe")

eingabe = st.number_input(
    "Bitte eine Zahl eingeben:",
    min_value=0,
    value=10
)


if st.button("Berechnung starten"):

    with st.spinner("Berechnung läuft..."):

        excel_datei = berechne_excel(eingabe)

    st.success("Berechnung abgeschlossen!")

    with open(excel_datei, "rb") as datei:

        st.download_button(
            label="Excel-Datei herunterladen",
            data=datei,
            file_name="Ergebnis.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

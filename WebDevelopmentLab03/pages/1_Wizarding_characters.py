import streamlit as st
import requests
import pandas as pd
import plotly.express as px


st.title("🧙 Wizard World: Explore Wizarding Characters")


BASE_URL = "https://wizard-world-api.herokuapp.com"


def get_wizards():
    try:
        response = requests.get(f"{BASE_URL}/Wizards")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        st.error(f"There was an error: {error}")
        return []


def filter_wizards(wizard_list, search_name, gender_choice):
    male_names = [
        "Harry", "Ron", "Draco", "Severus", "Albus", "Sirius", "Neville", "Fred", "George",
        "Dean", "Cedric", "Percy", "Remus", "Gilderoy", "Peter", "Kingsley", "Viktor", "Barty", "Igor"
    ]

    filtered = []
    for wizard in wizard_list:
        first = wizard.get("firstName") or ""
        last = wizard.get("lastName") or ""
        gender = wizard.get("gender")


        if not gender:
            if first in male_names:
                gender = "Male"
            else:
                gender = "Female"
        wizard["gender"] = gender


        if search_name.lower() in first.lower() or search_name.lower() in last.lower():
            if gender_choice == "All" or gender == gender_choice:
                filtered.append(wizard)
    return filtered


st.sidebar.header("Search Wizards")


name_input = st.sidebar.text_input("Enter part of a wizard's name")


gender_input = st.sidebar.selectbox("Choose Gender", ["All", "Male", "Female"])


all_wizards = get_wizards()


results = filter_wizards(all_wizards, name_input, gender_input)


if results:

    table = pd.DataFrame(results)


    for col in ["firstName", "lastName", "gender"]:
        if col not in table.columns:
            table[col] = "Unknown"

    st.write(f"### Found {len(table)} Wizard(s)")
    st.dataframe(table[["firstName", "lastName", "gender"]])

    gender_chart = table["gender"].value_counts().reset_index()
    gender_chart.columns = ["Gender", "Count"]
    fig = px.bar(gender_chart, x="Gender", y="Count", title="Wizard Gender Count")
    st.plotly_chart(fig)
else:
    st.warning("No wizards found with those search settings.")

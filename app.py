import streamlit as st
import pandas as pd


st.title("Unit Converter")


def distance_converter(value, from_unit, to_unit):
    units = {
        "metres": 1,
        "kilometres": 1000,
        "centimetres": 0.01,
        "millimetres": 0.001,
        "miles": 1609.34,
        "feet": 0.3048,
        "yards": 0.9144,
        "inches": 0.0254
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value
    
def weight_converter(value, from_unit, to_unit):
    units = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    return value * units[from_unit] / units[to_unit]


#UI
category = st.sidebar.radio("Choose the type of conversion", ["Length", "Temperature", "Weight"])


if category == "Length":
    from_unit = st.selectbox("Select the unit you want to convert from", ["kilometres", "metres", "centimetres", "millimetres", "miles", "feet", "yards", "inches"])

    to_unit = st.selectbox("Select the unit you want to convert to", ["kilometres", "metres", "centimetres", "millimetres", "miles", "feet", "yards", "inches"])

    value = st.number_input("Enter the value")

    if st.button("Convert"):
        result = distance_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("Select the unit you want to convert from", ["Celsius", "Fahrenheit", "Kelvin"])

    to_unit = st.selectbox("Select the unit you want to convert to", ["Celsius", "Fahrenheit", "Kelvin"])

    value = st.number_input("Enter the value")

    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("Select the unit you want to convert from", ["grams", "kilograms", "pounds", "ounces"])

    to_unit = st.selectbox("Select the unit you want to convert to", ["grams", "kilograms", "pounds", "ounces"])

    value = st.number_input("Enter the value")

    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")
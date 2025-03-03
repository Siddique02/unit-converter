import streamlit as st
import pandas as pd


st.title("Unit Converter")


def distance_converter(value, from_unit, to_unit):
    units = {
        "Metres": 1,
        "Kilometres": 1000,
        "Centimetres": 0.01,
        "millimetres": 0.001,
        "miles": 1609.34,
        "feet": 0.3048,
        "yards": 0.9144,
        "inches": 0.0254
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value
    
def weight_converter(value, from_unit, to_unit):
    units = {
        "Grams": 1,
        "Kilograms": 1000,
        "Pounds": 453.592,
        "Ounces": 28.3495
    }
    return value * units[from_unit] / units[to_unit]


#UI
category = st.sidebar.radio("Choose the type of conversion", ["Length", "Temperature", "Weight"])


if category == "Length":
    from_unit = st.selectbox("Select the unit you want to convert from", ["Kilometres", "Metres", "Centimetres", "millimetres", "miles", "feet", "yards", "inches"])

    to_unit = st.selectbox("Select the unit you want to convert to", ["Kilometer", "Metre", "Centimetre", "miles", "feet", "inches"])

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
    from_unit = st.selectbox("Select the unit you want to convert from", ["Grams", "Kilograms", "Pounds", "Ounces"])

    to_unit = st.selectbox("Select the unit you want to convert to", ["Grams", "Kilograms", "Pounds", "Ounces"])

    value = st.number_input("Enter the value")

    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")
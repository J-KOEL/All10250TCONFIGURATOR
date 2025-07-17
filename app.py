import streamlit as st
import pandas as pd

# Load all CSV files into dictionaries
def load_csv(file):
    return pd.read_csv(file)

# Mapping of product types to their required files and fields
product_configs = {
    "Non-Illuminated Pushbuttons": {
        "fields": ["Operator", "Button Color", "Circuit"],
        "files": {
            "Operator": "NonIlluminatedPushbuttonOperator 3.csv",
            "Button Color": "NonIlluminatedPushbuttonButtonColor 3.csv",
            "Circuit": "Circuit 8.csv"
        }
    },
    "Non-Illuminated Pushpulls": {
        "fields": ["Operator", "Button", "Circuit"],
        "files": {
            "Operator": "PushPullOperator 5.csv",
            "Button": "NonIlluminatedPushPullButton 2.csv",
            "Circuit": "Circuit 9.csv"
        }
    },
    "Illuminated Incandescent Pushpulls": {
        "fields": ["Operator", "Light Unit", "Lens", "Circuit"],
        "files": {
            "Operator": "PushPullOperator 5.csv",
            "Light Unit": "IlluminatedPushPullIncandescentLightUnit 2.csv",
            "Lens": "IlluminatedPushPullIncandescentLens 2.csv",
            "Circuit": "Circuit 10.csv"
        }
    },
    "Illuminated LED Pushpulls": {
        "fields": ["Operator", "Light Unit", "Lens", "Voltage", "Circuit"],
        "files": {
            "Operator": "PushPullOperator 5.csv",
            "Light Unit": "IlluminatedPushPullLEDLightUnit 2.csv",
            "Lens": "IlluminatedPushPullLEDlens 2.csv",
            "Voltage": "IlluminatedPushPullLLEDVoltage 2.csv",
            "Circuit": "Circuit 11.csv"
        }
    },
    "Illuminated Incandescent Pushbuttons": {
        "fields": ["Light Unit", "Lens", "Circuit"],
        "files": {
            "Light Unit": "IlluminatedPushbuttonIncandescentLightUnit 4.csv",
            "Lens": "illuminatedPushbuttonIncandescentLensColor 4.csv",
            "Circuit": "Circuit 12.csv"
        }
    },
    "Illuminated LED Pushbuttons": {
        "fields": ["Light Unit", "Lens", "Voltage", "Circuit"],
        "files": {
            "Light Unit": "IlluminatedPushbuttonLEDLightUnit 6.csv",
            "Lens": "IlluminatedPushbuttonLEDLensColor 6.csv",
            "Voltage": "IlluminatedPushbuttonLEDVoltage 7.csv",
            "Circuit": "Circuit 13.csv"
        }
    },
    "Standard Indicating Lights - LED": {
        "fields": ["Light Unit", "Lens", "Voltage"],
        "files": {
            "Light Unit": "StandardindicatingLightLEDlightUnit.csv",
            "Lens": "StandardIndicatingLightLEDLens.csv",
            "Voltage": "IndicatinglightLEDvoltage.csv"
        }
    },
    "Standard Indicating Lights - Incandescent": {
        "fields": ["Light Unit", "Lens"],
        "files": {
            "Light Unit": "StandardIndicatingLightIncandescentLightUnit.csv",
            "Lens": "StandardIndicatingIncandescentLens.csv"
        }
    },
    "PresTest Incandescent": {
        "fields": ["Light Unit", "Lens"],
        "files": {
            "Light Unit": "PrestTestIncandescentLightUnit.csv",
            "Lens": "PrestTestIncandescentLens.csv"
        }
    },
    "PresTest LED": {
        "fields": ["Light Unit", "Lens", "Voltage"],
        "files": {
            "Light Unit": "PrestTestLEDLightunit.csv",
            "Lens": "PrestTestLEDLens.csv",
            "Voltage": "IndicatinglightLEDvoltage 1.csv"
        }
    },
    "Master Test Incandescent": {
        "fields": ["Light Unit", "Lens"],
        "files": {
            "Light Unit": "MasterTestIncandescentLightUnit.csv",
            "Lens": "MasterTestIncandescentLens.csv"
        }
    }
}

# Catalog number generation logic
def build_catalog_number(product_type, selections):
    if product_type == "Non-Illuminated Pushbuttons":
        return f"10250T{selections['Operator']}{selections['Button Color']}-{selections['Circuit']}"
    elif product_type == "Non-Illuminated Pushpulls":
        return f"10250T{selections['Operator']}{selections['Button']}-{selections['Circuit']}"
    elif product_type == "Illuminated Incandescent Pushpulls":
        return f"10250T{selections['Operator']}{selections['Light Unit']}{selections['Lens']}-{selections['Circuit']}"
    elif product_type == "Illuminated LED Pushpulls":
        return f"10250T{selections['Operator']}{selections['Light Unit']}{selections['Lens']}={selections['Voltage']}-{selections['Circuit']}"
    elif product_type == "Illuminated Incandescent Pushbuttons":
        return f"10250T{selections['Light Unit']}{selections['Lens']}-{selections['Circuit']}"
    elif product_type == "Illuminated LED Pushbuttons":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}-{selections['Circuit']}"
    elif product_type == "Standard Indicating Lights - LED":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}"
    elif product_type == "Standard Indicating Lights - Incandescent":
        return f"10250T{selections['Light Unit']}{selections['Lens']}"
    elif product_type == "PresTest Incandescent":
        return f"10250T{selections['Light Unit']}{selections['Lens']}"
    elif product_type == "PresTest LED":
        return f"10250T{selections['Light Unit']}{selections['Lens']}{selections['Voltage']}"
    elif product_type == "Master Test Incandescent":
        return f"10250T{selections['Light Unit']}{selections['Lens']}"
    else:
        return "Invalid product type"

# Streamlit UI
st.title("10250T Catalog Number Configurator")

product_type = st.selectbox("Select Product Type", list(product_configs.keys()))

if product_type:
    config = product_configs[product_type]
    selections = {}

    for field in config["fields"]:
        df = load_csv(config["files"][field])
        label_col = [col for col in df.columns if "Label" in col][0]
        code_col = [col for col in df.columns if "Code" in col][0]
        options = dict(zip(df[label_col], df[code_col]))
        choice = st.selectbox(f"Select {field}", list(options.keys()))
        selections[field] = options[choice]

    if st.button("Generate Catalog Number"):
        catalog_number = build_catalog_number(product_type, selections)
        st.success(f"Catalog Number: {catalog_number}")

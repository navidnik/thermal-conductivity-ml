import pandas as pd

def load_and_clean_data(path: str):
    print("Loading and cleaning data...")
    df = pd.read_csv(path)

    target = "Thermal Conductivity (W/m·K)"
    features = [
        "Specific Heat (J/g·K)",
        "Entropy (J/mol·K)",
        "Band Gap (eV)",
        "Density (g/cm³)"
    ]

    df = df.dropna(subset=features + [target])

    X = df[features]
    y = df[target]

    return X, y, features
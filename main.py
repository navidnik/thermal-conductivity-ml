from src.preprocess import load_and_clean_data
from src.model import train_model, evaluate_model
from src.predict import predict_material

if __name__ == "__main__":
    print("Loading and cleaning data...")
    X, y, features = load_and_clean_data("data/crystal_thermal_properties.csv")

    print("Training model...")
    model = train_model(X, y)

    print("\nEvaluating model performance...")
    evaluate_model(model, X, y)

    print("\n=== Predict Thermal Conductivity for a New Material ===")
    try:
        user_features = {}
        for f in features:
            val = float(input(f"Enter {f}: "))
            user_features[f] = val

        predicted = predict_material(model, user_features)
        print(f"\nPredicted Thermal Conductivity: {predicted:.2f} W/m·K")

    except ValueError:
        print("⚠️ Invalid input! Please enter numeric values.")
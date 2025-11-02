# Crystal Thermal Conductivity Prediction

This is a simple Python project that predicts the **thermal conductivity** of crystalline materials using a **Random Forest Regressor**. The project uses a small dataset of crystal properties and demonstrates how machine learning can relate material features to thermal behavior.

---

## Dataset

The dataset (`crystal_thermal_properties.csv`) contains real material properties such as:

- `Elemental Composition`
- `Lattice Parameters (a, b, c)`
- `Symmetry`
- `Thermal Conductivity (W/m·K)` ✅ target variable
- `Specific Heat (J/g·K)`
- `Entropy (J/mol·K)`
- `Density (g/cm³)`
- `Band Gap (eV)`
- …and other physical properties

For this project, only **four numeric features** are used as input for the model:

1. `Specific Heat (J/g·K)`
2. `Entropy (J/mol·K)`
3. `Band Gap (eV)`
4. `Density (g/cm³)`

The target is:

- `Thermal Conductivity (W/m·K)`

---

## Project Structure

thermal-conductivity-ml/
│
├── data/
│ └── crystal_thermal_properties.csv
│
├── src/
│ ├── preprocess.py # Data loading and cleaning
│ ├── model.py # Training and evaluation
│ └── predict.py # Predicting new materials
│
└── main.py # Main script to run the project

yaml
Copy code

---

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd thermal-conductivity-ml
Install dependencies (Python 3.10+ recommended):

bash
Copy code
pip install -r requirements.txt
requirements.txt should contain:

nginx
Copy code
pandas
scikit-learn
Usage
Run the main script:

bash
Copy code
python main.py
The script will:

Load and clean the dataset.

Train a Random Forest model.

Evaluate the model on the training data.

Prompt the user to input features for a new material.

Output the predicted thermal conductivity.

Example Interaction
mathematica
Copy code
=== Predict Thermal Conductivity for a New Material ===
Enter Specific Heat (J/g·K): 900
Enter Entropy (J/mol·K): 45
Enter Band Gap (eV): 3.2
Enter Density (g/cm³): 4.0

Predicted Thermal Conductivity: 230.03 W/m·K
Notes
The model is simple and illustrative — it demonstrates the concept of using machine learning for material property prediction.

With a larger and more diverse dataset, the predictions would be more accurate.

This project is intended for educational purposes and to show interest in ML for material science.

License
MIT License


import pandas as pd

df = pd.DataFrame([["Pomacentrus", 1], ["Stethojulis", 2], ["Plectroglyphidodon", 3], ["Chrysiptera", 4], ["Halichoeres", 5], ["Acanthochromis", 6]])

df.columns = ["Date", "Scientific Name"]

df = df[df.Code.str.startswith("St")] 
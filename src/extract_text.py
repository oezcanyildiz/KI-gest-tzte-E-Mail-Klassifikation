import csv 
import pandas as pd 

def extract_text(
            input_path = "projekt/data/emails.csv",
            output_path="projekt/data/enron_5000.csv", 
            sample_size=5000
            ):
        
        
        print("Lade große Enron-Datei ...")
        df = pd.read_csv(input_path)

        df_small = df.sample(n=sample_size, random_state=42)

        df_small.to_csv(output_path, index=False)

if __name__ == "__main__":
    extract_text()


import pandas as pd

def main():
	dataset = pd.read_csv('survey_results_public_mega_inc.csv')
	dataset = dataset.dropna()
	dataset.to_csv('cleaned.csv')

main()
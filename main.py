import pandas as pd
import numpy as np


def main():
	dataset = pd.read_csv('survey_results_public_mega_inc.csv')
	dataset = dataset.dropna()
	dataset.drop(dataset.loc[ dataset['ConvertedSalary'] == 0.0 ].index , inplace=True)
	print(dataset)
	dataset['AgreeDisagree1'] = dataset['AgreeDisagree1'].map({'Strongly agree': 5, 'Agree': 4, 'Neither Agree nor Disagree': 3, 'Disagree': 2, 'Strongly disagree': 1})
	dataset['AgreeDisagree2'] = dataset['AgreeDisagree2'].map({'Strongly agree': 5, 'Agree': 4, 'Neither Agree nor Disagree': 3, 'Disagree': 2, 'Strongly disagree': 1})
	dataset['AgreeDisagree3'] = dataset['AgreeDisagree3'].map({'Strongly agree': 1, 'Agree': 2, 'Neither Agree nor Disagree': 3, 'Disagree': 4, 'Strongly disagree': 5})
	dataset['LnConvertedSalary'] = np.log(dataset['ConvertedSalary'])
	dataset.to_csv('cleaned.csv')

main()

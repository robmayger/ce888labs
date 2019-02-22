import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import seaborn as sns

def boostrap(sample, sample_size, iterations, percentile):
	# <---INSERT YOUR CODE HERE--->
    samples = []
    means = []
    for i in range(0, iterations):
        random_sample = np.random.choice(sample, sample_size)
        samples.append(random_sample)
        means.append(random_sample)
    data_mean = np.mean(samples)            
    lower = np.percentile(means, (100 - percentile)/2)
    upper = np.percentile(means, percentile + ((100-percentile)/2))
    return data_mean, lower, upper


if __name__ == "__main__":
	#df = pd.read_csv('./salaries.csv')
	df = pd.read_csv('./vehicles.csv').dropna()
	data = df.values.T[1]
	percentile = 95
	boots = []
	count = 1
	for i in range(100, 100000, 1000):
		print(count)
		count += 1
		boot = boostrap(data, data.shape[0], i, percentile)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("new_fleet_confidence.png", bbox_inches='tight')
	sns_plot.savefig("new_fleet_confidence.pdf", bbox_inches='tight')


	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))

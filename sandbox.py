import pandas as pd
import matplotlib.pyplot as plt

temp = pd.read_csv(data_file, sep='\t')
good_rows = np.where(temp['OverallValue'] > 0)[0]

plt.plot(temp['PctResEst'][good_rows], temp['PctAttEst'][good_rows], '.')
plt.title('Operation completion by resident')
plt.xlabel('Resident estimate')
plt.ylabel('Attending estimate')

plt.show()


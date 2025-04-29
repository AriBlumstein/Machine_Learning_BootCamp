
import numpy as np
from sklearn.impute import SimpleImputer
x = np.array([[1,2,float('nan')], [3,float('nan'),5], [8,float('nan'),9]])

for i in range(len(x[0])):
    print(len(list(filter(lambda row: np.isnan(row[i]), x))))

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, :])
x[:, :] = imputer.transform(x[:, :])
print(x)
## 3. Finding Correlations With the r Value ##

correlations = combined.corr()
correlations = correlations['sat_score']

## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt

plt.scatter(combined['total_enrollment'], combined['sat_score'])
plt.xlabel('total_enrollment')
plt.ylabel('sat_score')
plt.show()

## 6. Exploring Schools with Low SAT Scores and Enrollment ##

low_enrollment = combined[combined["total_enrollment"] < 1000]
low_enrollment = low_enrollment[low_enrollment["sat_score"] < 1000]
print(low_enrollment["School Name"])

## 7. Plotting Language Learning Percentage ##

plt.scatter(combined['ell_percent'], combined['sat_score'])
plt.xlabel('ell_percent')
plt.ylabel('sat_score')
plt.show()

## 8. Calculating District-Level Statistics ##

import numpy

districts = combined.groupby('school_dist').agg(numpy.mean)
districts.reset_index(inplace = True)
districts.head()
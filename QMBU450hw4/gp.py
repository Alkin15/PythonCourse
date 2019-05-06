import pandas as pd
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF
from sklearn.model_selection import train_test_split

url = 'https://raw.githubusercontent.com/carlson9/KocPython2019/master/Homework/immSurvey.csv'
tt = pd.read_csv(url,index_col=0,parse_dates=[0])
tt.head()

alphas = tt.stanMeansNewSysPooled
sample = tt.textToSend

from sklearn.feature_extraction.text import CountVectorizer


vec = CountVectorizer(ngram_range=(2, 2),
                                   token_pattern=r'\b\w+\b', min_df=1)
analyze = vec.build_analyzer()
X=vec.fit_transform(sample)



Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas,
random_state=1)


rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

# Compute posterior predictive mean and covariance
mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

#test correlation between test and mus
print np.corrcoef(ytest, mu_s)
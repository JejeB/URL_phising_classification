# URL phishing classication study
### Introduction 
This project try to apply machine learning classification to recognize phising URL.
The dataset used are the one describe here : https://data.mendeley.com/datasets/72ptz43s9v/1

### Launch the project
To launch the project first launch the preprocessing script

```
$ python3 src/preprocessing.py
```

This script clean a normalize the data, it will create 2 other `.csv` files : 
- `clean_data.csv` the data here are cleaned and normalized
- `clean_data_no_norm.csv` the same but not normalized

The 2 files will be used as input for the classifers 
> the goal is just to not do the preprocessing again if you want to test differents classifiers

Now just launch the test script 
```
$ src/testtest_classifier.py
```
The output is all the confussion matrix

### Result
| Algorithm | True positiv |False positiv |True negativ|False negative|Score|
|tree classifier|5233|430|7137|0.84|
|random forest|6477|505|7068|610|0.92|
|support vector machine|5118|1891|5629|0.73|
|lineare regression|4759|2249|5752|1900|0.72|

Tree classifier rules :


from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression

def PCA_test(df,label):
    pca = PCA(n_components=3)
    new_df = pca.fit_transform(df)
    variance = pca.explained_variance_ratio_
    return new_df

def testForest(df,lab):

    df_train, df_test,label_train,label_test = train_test_split(df,label)
    
    clf = RandomForestClassifier(n_estimators=10)
    
    clf = clf.fit(df_train,label_train)
   
    predict=clf.predict(df_test)
    print(confusion_matrix(label_test,predict) )
    print(accuracy_score(label_test,predict))

def testTree(df,label):
    df_train, df_test,label_train,label_test = train_test_split(df,label)

    clf = tree.DecisionTreeClassifier(max_depth=3)
    
    clf = clf.fit(df_train,label_train)
   
    predict=clf.predict(df_test)
    print(confusion_matrix(label_test,predict) )
    print(accuracy_score(label_test,predict))

def testSVM(df,label):
    df_train, df_test,label_train,label_test = train_test_split(df,label)

    clf = svm.SVC()
    
    clf = clf.fit(df_train,label_train)
   
    predict=clf.predict(df_test)
    print(confusion_matrix(label_test,predict) )
    print(accuracy_score(label_test,predict))

def testLG(df,label):
    df_train, df_test,label_train,label_test = train_test_split(df,label)

    clf = LogisticRegression()
    
    clf = clf.fit(df_train,label_train)
   
    predict=clf.predict(df_test)
    print(confusion_matrix(label_test,predict) )
    print(accuracy_score(label_test,predict))


if __name__ == "__main__":
    df  = pd.read_csv('dataset/clean_data.csv')
    df_no_norm = pd.read_csv('dataset/clean_data_no_norm.csv')

    label = df['phishing']
    df  = df.drop(columns=['phishing'])

    label_n = df_no_norm['phishing']
    df_no_norm  = df_no_norm.drop(columns=['phishing'])
    
    print('Tree...')
    testTree(df_no_norm,label_n)
    print('RandomForest...')
    testForest(df_no_norm,label_n)

    df  = PCA_test(df,label)
    print('SVM...')
    testSVM(df,label)
    print('Lineare regression...')
    testLG(df,label)
    

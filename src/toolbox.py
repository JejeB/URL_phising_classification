import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
import pydotplus

"""
Sets of functiions used to draw plot and images of the results. The project as first a shcol project so I needed some image to show in
a more preaty way the results
"""

def draw_boxplot(att,df):
    df.boxplot(att)
    plt.savefig('./img/boxplot_after.png')
    plt.clf()

def draw_histo(att,df):
    df.hist(att)
    plt.savefig('./img/hist_'+att+'.png')
    plt.clf()

def export_tree_img(clt,f):
    dot_data = tree.export_graphviz(clt, out_file=None,feature_names=f,  
                   class_names=['phishing','no phishing'])
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png("img/tree_no_norm.png")  

def PAC_projection(new_df,label):

    plt.scatter(new_df[:,0][label==1],new_df[:,1][label==1],c='r')
    plt.scatter(new_df[:,0][label==0],new_df[:,1][label==0],c='b')
    plt.savefig('./img/pca_projection.png')
    plt.clf()

def PAC_histo(variance):
    plt.bar(range(len(variance) ), variance, alpha=0.5, align='center',
            label='individual explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal components')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('./img/pac_histo.png')
    plt.clf()
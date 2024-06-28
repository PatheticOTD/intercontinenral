import numpy as np
import pandas as pd

class TwoPointers():
    def __init__(self, col, sep):
        self.col = col
        self.sep = sep
        self.right = None
        self.left = None
        self.left_prob = None
        self.right_prob = None
        self.is_right = None # 1 или 0


def entropy_shennon(y: np.array):
    ans = 0
    for i in np.unique(y):
        si = (y == i).sum() / y.shape[0]
        ans -= si * np.log2(si)
    return ans

def  IG (*y_arr):
    ans = entropy_shennon(y_arr[0])
    N = y_arr[0].shape[0]
    for yi in y_arr[1:]:
        Ni = yi.shape[0]
        ans -= Ni/N * entropy_shennon(yi) 
    return ans

def get_best_split(X:np.array, y:np.array):
    ig = 0
    split_value = 0
    col_name = ''
    for col in range(X.shape[1]):
        unique_sorted = np.sort(np.unique(X[:, col]))
        separators = np.zeros(unique_sorted.shape[0] - 1)
        for i in range(unique_sorted.shape[0] - 1):
            separators[i] = (unique_sorted[i] + unique_sorted[i+1]) / 2
        
        for sep in separators:
            right = y[X[:, col] > sep]
            left = y[X[:, col] <= sep]
            ig_local = IG(y, right, left)
            
            if ig_local > ig:
                ig = ig_local
                col_name = col
                split_value = sep 
    return (col_name, split_value, ig)

def tree_builder(x, y, curr_depth:int, Node, min_samples_split, max_depth:int = -1, is_right = 0):
        if (x.shape[0] < min_samples_split) or (np.unique(y).shape[0] <=1) or (curr_depth == max_depth):
            if is_right == 1:
                Node.right_prob = (y == 1).sum() / y.shape[0]
                Node.left_prob = 0.0
            else:
                Node.left_prob = (y == 1).sum() / y.shape[0]
                Node.right_prob = 0.0
            return Node

        else:
            best_split = get_best_split(x, y)
            
            right_x = x[x[:, best_split[0]] > best_split[1]]
            left_x  = x[x[:,  best_split[0]] <= best_split[1]]
            
            right_y = y[x[:, best_split[0]] > best_split[1]]
            left_y = y[x[:,  best_split[0]] <= best_split[1]]
            
            Node.col = best_split[0]
            Node.sep = best_split[1]
            Node.left =  tree_builder(left_x,  left_y,  curr_depth + 1, TwoPointers(None, None), min_samples_split, max_depth, 0)
            Node.right = tree_builder(right_x, right_y, curr_depth + 1, TwoPointers(None, None), min_samples_split, max_depth, 1)
        
        return Node


    
def tree_reader(node, indent = ''):
    if (node.left == None) and (node.right == None):
        if node.is_right == 1:
            print(indent, 'right_prob =', node.right_prob)
        else:print(indent, 'right_prob =', node.right_prob)

    else:
        print(indent, 'col:', node.col, 'sep:', node.sep)
        tree_reader(node.right, indent + '  ')
        tree_reader(node.left, indent + '  ')
        
class MyTreeClf():

    def __init__(self, max_depth = 5, min_samples_split = 10, max_leafs = None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_leafs = max_leafs
        self.leafs_cnt = 0
        self.tree = None
    
    def leaf_counter(self, node):
        if (node.left == None) and (node.right == None):
            self.leafs_cnt +=1

        else:
            self.leaf_counter(node.right)
            self.leaf_counter(node.left )

    def tree_pruner(self, node):
        if (node.left.left == None) and (node.left.right == None): # <-- если левая ветка имеет листья
            pass
    
    def fit (self, X, y):
        self.tree = TwoPointers(None, None)
        X = X.values
        y = y.values
        tree_builder(X, y, 0, self.tree, self.min_samples_split, max_depth=self.max_depth)
        self.leaf_counter(self.tree)
        
        if self.leafs_cnt > self.max_leafs:
            self.tree_pruner(self.tree)
    
    def display_tree(self):
        tree_reader(self.tree)
    
    def print_leafs_count(self):
        return self.leafs_cnt
    
            
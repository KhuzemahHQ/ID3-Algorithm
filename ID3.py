from importlib.metadata import entry_points
import numpy
import sys
import pprint

# Loasing the dataset:
dataset_file_name = sys.argv[1]

# Loading the encodings:
encodings_file_name = sys.argv[2]

dataset = numpy.loadtxt(dataset_file_name , dtype=int , delimiter=",") 

# Function to find the entropy of the entire system under consideration:
def find_entropy_of_system(dataset):
    entropy = 0

    rows = dataset.shape[0]
    if rows == 0:
        return 1
    outputs = dataset[:,-1]
    output1 = 0
    for row in outputs:
        if row == 1:
            output1 += 1
    output2 = rows - output1
    if output1 == 0:
        output1_entropy = 0
    else:
        output1_entropy = - (output1/rows)*numpy.log2(output1/rows)
    if output2 == 0:
        output2_entropy = 0
    else:
        output2_entropy = - (output2/rows)*numpy.log2(output2/rows)
    entropy = output1_entropy + output2_entropy

    return entropy

# Function to find the entropy of a system GIVEN an attribute (i.e., the conditional entropy):
def find_entropy_given_attribute(dataset , attrbute_index):
    entropy_to_return = 0
    total_rows = dataset.shape[0]
    attributes_list,possible_outputs,possible_attribute_values = helper_with_encodings(attrbute_index,encodings_file_name)
    for i in range(len(possible_attribute_values)):
        x = []
        for instance in range(total_rows):
            if dataset[instance,attrbute_index] == i:
                x.append(dataset[instance,:])
        x = numpy.array(x)
        entropy_to_return += find_entropy_of_system(x)*(x.shape[0]/total_rows)

    return entropy_to_return

# Function to find the information gain of a given attribute:
def find_information_gain_of_attribute(dataset , attrbute_index):
    information_gain = 0
    information_gain = find_entropy_of_system(dataset) - find_entropy_given_attribute(dataset,attrbute_index)
    return information_gain

# Helper function to give me the correct encodings for each attribute:
def helper_with_encodings(max_attribute_node_column_number , file_name_of_encodings):
    encodings_txt = open(file_name_of_encodings , "r") 
    encodings_list = []
    for line in encodings_txt:
        line_stripped = line.rstrip('\n')
        encodings_list.append(line_stripped)
        
    attributes = encodings_list[0].split(",")
    yes_or_nos = encodings_list[-1].split(",") 
    values_of_each_attribute = encodings_list[max_attribute_node_column_number+1].split(",")
    
    return attributes , yes_or_nos , values_of_each_attribute

def best_feature(dataset,feature_list):
    info_gain = -1
    result = None
    for feature in feature_list:
        gain = find_information_gain_of_attribute(dataset,feature) 
        if gain > info_gain:
            info_gain = gain
            result = feature
    return result


def subtree(dataset,feature):
    tree = {}
    total_rows = dataset.shape[0]
    attributes,possible_outputs,possible_attribute_values = helper_with_encodings(feature,encodings_file_name)
    pure = []
    for i in range(len(possible_attribute_values)):
        x = []
        for instance in range(total_rows):
            if dataset[instance,feature] == i:
                x.append(dataset[instance,:])
        x = numpy.array(x)
        if find_entropy_of_system(x) == 0:
            pure.append(i)
            total = x.shape[0]
            outputs = x[:,-1]
            output1 = 0
            for row in outputs:
                if row == 0:
                    output1 += 1
            if output1 == total:
                tree[possible_attribute_values[i]] = possible_outputs[0]
            else:
                tree[possible_attribute_values[i]] = possible_outputs[1]

    for i in range(len(possible_attribute_values)):
        if i in pure:
            x = []
            total_rows = dataset.shape[0]
            for instance in range(total_rows):
                if dataset[instance,feature] != i:
                    x.append(dataset[instance,:])
            x = numpy.array(x)
            dataset = x
        else:
            tree[possible_attribute_values[i]] = "expand"
        
    return tree, dataset


# Now, a recursive function that finds the root node, constructs subtables for each unique attribute value inside the root node
# and checks the purity of the subtable. If the subtable is not pure, this means another subtable can be made out of it and so this
# process carries on recursively until we get a pure subtable (i.e., a leaf node is obtained). Ultimately, this function builds the 
# entire tree. 

def recursive_tree(root,previous_feature_value,dataset,feature_list):
    if dataset.shape[0] > 0:
        best_node = best_feature(dataset,feature_list)
        attributes,possible_outputs,possible_attribute_values = helper_with_encodings(best_node,encodings_file_name)
        feature_name = attributes[best_node]

        new_feature_list = []
        for element in feature_list:
            if element != best_node:
                new_feature_list.append(element)
        feature_list = new_feature_list

        tree, dataset = subtree(dataset,best_node)
        next_root = None

        if previous_feature_value != None:
            root[previous_feature_value] = dict()
            root[previous_feature_value][feature_name] = tree
            next_root = root[previous_feature_value][feature_name]
        
        else:
            root[feature_name] = tree
            next_root = root[feature_name] 

        for node, branch in list(next_root.items()):
            if branch == "expand": 
                total_rows = dataset.shape[0]
                x = []
                i = possible_attribute_values.index(node)
                for instance in range(total_rows):
                    if dataset[instance,best_node] == i:
                        x.append(dataset[instance,:])
                x = numpy.array(x)
                new_dataset = x
                
                recursive_tree(next_root, node, new_dataset,feature_list)


def decision_tree_maker(dataset , tablee=None): 
    tree = {}
    feature_list = numpy.arange(dataset.shape[1]-1)
    recursive_tree(tree,None,dataset,feature_list)
    return tree

decision_tree = decision_tree_maker(dataset)   

pprint.pprint(decision_tree) 
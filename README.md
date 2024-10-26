# ID3-Algorithm
Implementing the ID3 Algorithm in python, to make Decision Trees.

The <name>_dataset.txt contains integer labels for the string attribute values, and the <name>_encodings.txt contains information about which integer maps to which string label (this will be useful for naming the keys of output tree).

![dataset](https://github.com/user-attachments/assets/7859f5c0-fe69-464a-bed7-86dc6b0cddc4)

The following is an example of tennis_encodings.txt

![image](https://github.com/user-attachments/assets/768107c0-16a5-438c-bac1-15adeb19ba82)

You should interpret this file as follows:
● The first row of tennis_encodings.txt gives you the name of columns in tennis_dataset.txt. The first column name is Outlook, 2nd one is Temperature, third is Humidity and so on.
● Then the second row gives you label mappings for attributes inside the first column
Outlook. The sunny maps to 0, Rainy maps to 1 and Overcast maps to 2 (as depicted in the above tables).
● The third row gives label mappings for attributes inside the 2nd column Temperature. Hot maps to 0, Mild maps to 1, Cool maps to 2.
● Onward rows follow the same pattern. In short each nth row except 1st one gives you labels for (n-1)th column. And each word inside that row maps to i where i is the index of that word in that row and i starts from 0.
(The same convention is followed for all the other <name>_encodings.txt files).


ID3 Decision Tree Implementation
Using the ID3 algorithm, this implementation builds a decision tree based on the dataset provided. The process includes:

Data Preprocessing: Each attribute and class label is encoded as an integer for computation, referencing encoding tables.
Tree Construction: The ID3 algorithm selects attributes based on information gain to form branches, creating a tree structure where each node represents a decision point.
Tree Output: Once the tree is constructed, it’s printed as a Python dictionary. Integer labels are then converted back to their original string labels as per the encoding table, providing clarity and readability.
The output dictionary is formatted to match the structure specified in the example output.

When run using tennis_dataset.txt and tennis_encodings.txt:

![image](https://github.com/user-attachments/assets/b4c62014-dee0-45d6-a458-549430f984b9)

When run using vampire_dataset.txt and vampire_encodings.txt:

![image](https://github.com/user-attachments/assets/57a7d8f5-02fc-44f6-9c8d-5aaa4e975be5)


When run using drug_dataset.txt and drug_encodings.txt:

![image](https://github.com/user-attachments/assets/ac1c5e45-6907-4c2e-a8b6-80447796c997)


When run using loan_dataset.txt and loan_encodings.txt:

![image](https://github.com/user-attachments/assets/769162f8-e1cb-4608-989e-1e788e0babae)


How to run your code:
Your dataset and encoding files should be present in the same directory as the python file, and your program should take as input the data set file from the command line. The command to run the program will be as follows: python3 <RollNumber>.py <datasetName>.txt <encodings>.txt
(look up sys.argv on the internet to see how you can get the file name from the command line into your program).

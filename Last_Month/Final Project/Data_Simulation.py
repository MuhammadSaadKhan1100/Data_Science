"""

@MuhammadSaadKhan1100 
PlayingNumbers
/
ML_Process_Course
Public
Code
Issues
1
Pull requests
Actions
Projects
Security
Insights
You’re making changes in a project you don’t have write access to. We’ve created a fork of this project for you to commit your proposed changes to. Submitting a change will write it to a new branch in your fork, so you can send a pull request.
ML_Process_Course
/
dataset_simulation.py
in
PlayingNumbers:main
 

Tabs

8

No wrap
1
import pandas as pd
2
import numpy as np
3
from sklearn import datasets
4
import random
5
​
6
## Customer Lifetime Value Dataset
7
​
8
def make_clv_dataset():
9
​
10
        features, output, coef = datasets.make_regression(n_samples = 5000, n_features = 7,
11
                                    n_informative = 7, n_targets = 1,
12
                                    noise = 0.0, coef = True)
13
​
14
        df = pd.DataFrame(features, columns=['id',
15
                'age',
16
                'gender',
17
                'income',
18
                'days_on_platform',
19
                'city',
20
                'purchases'])
21
​
22
        def make_id(df, column):
23
                df[column] = df.index
24
                return df
25
​
26
        def create_from_list(df, column, col_list):
27
​
28
                final_list = []
29
                for i in range(0,len(df)):
30
                        chosen = random.choice(col_list)
31
                        final_list.append(chosen)
32
​
33
                df[column] = final_list
34
                return df
35
​
36
        def scale_by_list(df, column, col_scale):
37
​
38
                df[column] = abs(df[column])
39
                df[column] = df[column] * col_scale
40
                df[column] = df[column].astype(int)
41
                return df
42
​
43
        age_range = np.arange(10,90)
44
        gender = ['Male','Female']
45
        city = ['New York City', 'San Francisco','Miami','Tokyo','London']
@MuhammadSaadKhan1100
Propose changes
Commit summary
Create dataset_simulation.py
Optional extended description
Add an optional extended description…
 
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About

```

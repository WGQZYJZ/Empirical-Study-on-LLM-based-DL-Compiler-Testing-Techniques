## The purpose of the project
This study is to test the feasibility and efficiency of the generation of PyTorch models with public APIs in an open-source way. Therefore, we used a pre-existing dataset of images and labels to generate models that contain the specified patterns.
The main reason why this study was carried out is because our team has tested our new models against the previously generated ones on the existing datasets, and found that the result of these comparisons could potentially be helpful for the development of the model architecture.

# Results of comparison
The results obtained from our testing are presented in Table 2. In the table, a line representing an image is provided with three columns. First column represents the generated model with public APIs meets the specified requirements, second column represents the generated model without public APIs, and third column represents the corresponding input for this model. The results show that we could generate models with public APIs and then convert them to a standard PyTorch model, resulting in a small difference of one to three orders of magnitude (see Table 3). 

![Table 2](https://user-images.githubusercontent.com/9071856/107606914-e85af700-6c8a-11eb-96d2-e3f8878fb67b.png)

As expected, we see that public APIs are capable of generating models containing the specified patterns. But because they do not have an equivalent to standard PyTorch model, the difference cannot be easily explained by our results; for example, the generated models do not contain any `nn.ReLU`, `torch.log()`, `nn.Linear()`, and `nn.ReLU6()`.


![Table 3](https://user-images.githubusercontent.com/9071856/107606927-ea14ba80-6c8a-11eb-9d2b-7be0e0bc3cd0.png)

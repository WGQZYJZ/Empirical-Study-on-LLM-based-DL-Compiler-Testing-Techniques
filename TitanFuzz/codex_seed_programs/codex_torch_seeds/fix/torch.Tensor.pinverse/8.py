'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pinverse\ntorch.Tensor.pinverse(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input tensor: \n', input_tensor)
pinv_tensor = input_tensor.pinverse()
print('Pseudoinverse of the input tensor is: \n', pinv_tensor)
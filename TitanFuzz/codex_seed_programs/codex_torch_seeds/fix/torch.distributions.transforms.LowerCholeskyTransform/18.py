'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.LowerCholeskyTransform\ntorch.distributions.transforms.LowerCholeskyTransform(cache_size=0)\n'
import torch
import numpy as np
print('Task1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task2: Generate input data')
input_data = torch.rand(10, 10)
print('input_data: ', input_data)
print('Task3: Call the API torch.distributions.transforms.LowerCholeskyTransform')
lower_cholesky_transform = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)
print('lower_cholesky_transform: ', lower_cholesky_transform)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
quantile_tensor = input_tensor.quantile(0.5, dim=1)
print('The input tensor is: \n{}'.format(input_tensor))
print('The quantile tensor is: \n{}'.format(quantile_tensor))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma\ntorch.Tensor.polygamma(_input_tensor, n)\n'
import torch
import numpy as np
input_tensor = torch.randn(4, 4)
n = 1
print('Input Tensor: ', input_tensor)
print('N: ', n)
print('Output: ', torch.Tensor.polygamma(input_tensor, n))
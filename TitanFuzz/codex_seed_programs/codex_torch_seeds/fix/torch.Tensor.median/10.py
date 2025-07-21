'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
import numpy as np
_input_tensor = torch.rand(3, 3)
print('Input data:')
print(_input_tensor)
print('Median of the input tensor:')
print(_input_tensor.median())
print('Median of the input tensor along the dimension 0:')
print(_input_tensor.median(dim=0))
print('Median of the input tensor along the dimension 1:')
print(_input_tensor.median(dim=1))
print('Median of the input tensor along the dimension 0 with keepdim:')
print(_input_tensor.median(dim=0, keepdim=True))
print('Median of the input tensor along the dimension 1 with keepdim:')
print(_input_tensor.median(dim=1, keepdim=True))
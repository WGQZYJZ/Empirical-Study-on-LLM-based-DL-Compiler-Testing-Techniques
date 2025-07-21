'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(3, 4)
print('input tensor: ', input_tensor)
index = torch.tensor([1, 0, 3, 2])
output_tensor = input_tensor.index_select(dim=1, index=index)
print('output tensor: ', output_tensor)
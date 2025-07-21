'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 3, 4)
print('input_tensor = ', input_tensor)
index = torch.tensor([0, 1])
output_tensor_1 = input_tensor.index_select(0, index)
print('output_tensor_1 = ', output_tensor_1)
index = torch.tensor([1, 2])
output_tensor_2 = input_tensor.index_select(1, index)
print('output_tensor_2 = ', output_tensor_2)
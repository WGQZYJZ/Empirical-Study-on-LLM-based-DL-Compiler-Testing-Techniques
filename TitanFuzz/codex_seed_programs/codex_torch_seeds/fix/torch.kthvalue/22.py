'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data: ', input_data)
k = 1
(values, indices) = torch.kthvalue(input_data, k)
print('Values: ', values)
print('Indices: ', indices)
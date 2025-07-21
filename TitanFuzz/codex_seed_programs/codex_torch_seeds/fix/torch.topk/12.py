'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input data: ', input)
k = 1
(values, indices) = torch.topk(input, k)
print('Values: ', values)
print('Indices: ', indices)
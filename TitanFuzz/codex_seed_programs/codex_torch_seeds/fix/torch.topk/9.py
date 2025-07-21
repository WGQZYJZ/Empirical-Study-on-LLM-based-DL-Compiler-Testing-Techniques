'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
import torch
input_data = torch.randn(2, 3)
print('Input data:')
print(input_data)
k = 2
(values, indices) = torch.topk(input_data, k)
print('\nValues:')
print(values)
print('\nIndices:')
print(indices)
(values, indices) = torch.topk(input_data, k, dim=1)
print('\nValues:')
print(values)
print('\nIndices:')
print(indices)
(values, indices) = torch.topk(input_data, k, dim=1, largest=False)
print('\nValues:')
print(values)
print('\nIndices:')
print(indices)
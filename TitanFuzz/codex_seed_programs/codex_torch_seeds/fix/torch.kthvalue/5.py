'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(3, 5)
k = 2
(values, indices) = torch.kthvalue(data, k, dim=1)
print('Input data:')
print(data)
print('Values:')
print(values)
print('Indices:')
print(indices)
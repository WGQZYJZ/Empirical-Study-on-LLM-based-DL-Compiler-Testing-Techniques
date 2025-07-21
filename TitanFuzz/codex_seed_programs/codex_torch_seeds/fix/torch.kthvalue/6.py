'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(5, 5)
print('Input data:\n', data)
k = 1
print('\n', torch.kthvalue(data, k))
k = 2
print('\n', torch.kthvalue(data, k))
k = 3
print('\n', torch.kthvalue(data, k))
k = 4
print('\n', torch.kthvalue(data, k))
k = 5
print('\n', torch.kthvalue(data, k))
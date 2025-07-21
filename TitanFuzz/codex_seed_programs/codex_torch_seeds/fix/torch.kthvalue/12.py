'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('Input:')
print(input)
k = 2
dim = 1
keepdim = True
(value, index) = torch.kthvalue(input, k, dim, keepdim)
print('\nValue:')
print(value)
print('\nIndex:')
print(index)
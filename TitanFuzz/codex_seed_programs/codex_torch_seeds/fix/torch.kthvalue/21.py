'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
print('Input: ')
print(input)
print('Output: ')
print(torch.kthvalue(input, 2))
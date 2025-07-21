'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
input = torch.randn(10, 5)
print('Input data:')
print(input)
print('\nTop 3 values:')
print(torch.topk(input, 3))
print('\nTop 3 values along dim=1:')
print(torch.topk(input, 3, dim=1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
input = torch.randn(2, 3)
print('Input:')
print(input)
print('\n')
print('Output:')
print(torch.argmin(input, dim=1))
print('\n')
print('Output:')
print(torch.argmin(input, dim=1, keepdim=True))
print('\n')
print('Output:')
print(torch.argmin(input, dim=0))
print('\n')
print('Output:')
print(torch.argmin(input, dim=0, keepdim=True))
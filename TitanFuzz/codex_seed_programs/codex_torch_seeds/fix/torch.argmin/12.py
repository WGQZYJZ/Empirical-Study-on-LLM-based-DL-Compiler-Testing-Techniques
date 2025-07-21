'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
a = torch.randn(4, 4)
print(a)
print('Task 1:')
print(torch.argmin(a))
print('Task 2:')
print(torch.argmin(a, dim=1))
print('Task 3:')
print(torch.argmin(a, dim=1, keepdim=True))
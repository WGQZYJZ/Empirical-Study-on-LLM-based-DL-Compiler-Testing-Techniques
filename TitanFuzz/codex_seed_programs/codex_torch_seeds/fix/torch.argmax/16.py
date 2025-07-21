'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmax\ntorch.argmax(input, dim, keepdim=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(3, 5)
print('Task 3: Call the API torch.argmax')
print('torch.argmax(input, dim, keepdim=False)')
print('input:')
print(input)
print('torch.argmax(input, 1):')
print(torch.argmax(input, 1))
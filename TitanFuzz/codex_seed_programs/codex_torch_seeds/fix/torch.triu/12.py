'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 3)
print('Input data:')
print(input)
output = torch.triu(input, diagonal=0)
print('Output data:')
print(output)
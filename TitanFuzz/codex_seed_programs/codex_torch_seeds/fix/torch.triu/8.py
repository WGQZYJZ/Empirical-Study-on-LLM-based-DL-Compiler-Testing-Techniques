'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('input: \n', input)
output = torch.triu(input)
print('output: \n', output)
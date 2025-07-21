'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input = torch.randn(2, 3, 4)
print('input: ', input)
dim = 0
output = torch.unsqueeze(input, dim)
print('output: ', output)
dim = 1
output = torch.unsqueeze(input, dim)
print('output: ', output)
dim = 2
output = torch.unsqueeze(input, dim)
print('output: ', output)
dim = 3
output = torch.unsqueeze(input, dim)
print('output: ', output)
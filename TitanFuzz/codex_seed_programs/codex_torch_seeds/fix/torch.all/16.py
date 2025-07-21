'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.tensor([[True, False], [False, False]])
print('Input: ', input)
output = torch.all(input)
print('Output: ', output)
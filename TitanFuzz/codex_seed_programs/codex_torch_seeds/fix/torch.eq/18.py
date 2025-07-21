'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
other = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output = torch.eq(input, other)
print('output = ', output)
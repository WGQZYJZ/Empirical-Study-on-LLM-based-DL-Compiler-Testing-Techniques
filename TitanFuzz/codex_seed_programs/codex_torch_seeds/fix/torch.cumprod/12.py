'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor:', input)
output = torch.cumprod(input, dim=1)
print('Output tensor:', output)
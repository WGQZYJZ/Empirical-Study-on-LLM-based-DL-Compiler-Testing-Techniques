'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
input = torch.randn(3, dtype=torch.float)
print('Input data: ', input)
result = torch.special.polygamma(1, input)
print('Result: ', result)
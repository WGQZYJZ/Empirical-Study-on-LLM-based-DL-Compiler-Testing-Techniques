'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print('Input data: \n', input)
polygamma = torch.special.polygamma(1, input)
print('Result: \n', polygamma)
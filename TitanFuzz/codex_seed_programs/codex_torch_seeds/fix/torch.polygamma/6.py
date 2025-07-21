'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('input: ', input)
print('torch.polygamma(0, input): ', torch.polygamma(0, input))
print('torch.polygamma(1, input): ', torch.polygamma(1, input))
print('torch.polygamma(2, input): ', torch.polygamma(2, input))
print('torch.polygamma(3, input): ', torch.polygamma(3, input))
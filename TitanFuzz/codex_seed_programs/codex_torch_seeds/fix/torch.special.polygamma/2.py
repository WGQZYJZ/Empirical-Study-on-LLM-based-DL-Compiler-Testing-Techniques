'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print('x = ', x)
print('polygamma(1, x) = ', torch.special.polygamma(1, x))
print('polygamma(2, x) = ', torch.special.polygamma(2, x))
print('polygamma(3, x) = ', torch.special.polygamma(3, x))
print('polygamma(4, x) = ', torch.special.polygamma(4, x))
print('polygamma(5, x) = ', torch.special.polygamma(5, x))
print('polygamma(6, x) = ', torch.special.polygamma(6, x))
print('polygamma(7, x) = ', torch.special.polygamma(7, x))
print('polygamma(8, x) = ', torch.special.polygamma(8, x))
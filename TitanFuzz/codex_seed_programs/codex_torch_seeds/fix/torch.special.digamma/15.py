'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print(x)
print(torch.special.digamma(x))
'\ntorch.special.polygamma(n, input, *, out=None)\n'
print(torch.special.polygamma(0, x))
print(torch.special.polygamma(1, x))
print(torch.special.polygamma(2, x))
print(torch.special.polygamma(3, x))
'\ntorch.special.erf(input, *, out=None)\n'
print(torch.special.erf(x))
'\ntorch.special.erfc(input, *, out=None)\n'
print(torch.special.erfc(x))
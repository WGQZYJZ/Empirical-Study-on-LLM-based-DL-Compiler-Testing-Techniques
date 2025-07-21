'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
import torch
n = 1
input = torch.randn(2, 3)
torch.special.polygamma(n, input)
n = 1
input = torch.randn(2, 3)
out = torch.zeros_like(input)
torch.special.polygamma(n, input, out=out)
print(out)
n = 1
input = torch.randn(2, 3)
out = torch.zeros_like(input)
torch.special.polygamma(n, input, out=out)
print(out)
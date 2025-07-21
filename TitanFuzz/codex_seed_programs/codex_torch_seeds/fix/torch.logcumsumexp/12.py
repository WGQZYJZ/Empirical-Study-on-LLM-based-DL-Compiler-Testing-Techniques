'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
import torch
input_data = torch.randn(1, 2, 3)
torch.logcumsumexp(input_data, dim=1)
torch.logcumsumexp(input_data, dim=1, out=None)
print(torch.logcumsumexp(input_data, dim=1))
print(torch.logcumsumexp(input_data, dim=1, out=None))
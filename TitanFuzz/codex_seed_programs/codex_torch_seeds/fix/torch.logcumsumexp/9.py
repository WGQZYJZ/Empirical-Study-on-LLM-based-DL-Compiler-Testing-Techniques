'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(torch.logcumsumexp(input_data, dim=1))
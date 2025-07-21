'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
a = torch.randn(2, 3)
print(a)
print(torch.count_nonzero(a))
print(torch.count_nonzero(a, dim=0))
print(torch.count_nonzero(a, dim=1))
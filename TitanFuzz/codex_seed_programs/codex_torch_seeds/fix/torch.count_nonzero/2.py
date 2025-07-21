'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input = torch.randn(1, 3)
print(input)
print(torch.count_nonzero(input))
print(torch.count_nonzero(input, dim=0))
print(torch.count_nonzero(input, dim=1))
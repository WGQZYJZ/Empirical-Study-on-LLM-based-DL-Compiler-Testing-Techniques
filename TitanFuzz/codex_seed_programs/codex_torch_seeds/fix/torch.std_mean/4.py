'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std_mean\ntorch.std_mean(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input = torch.rand(10, 10)
print(torch.std_mean(input, dim=1))
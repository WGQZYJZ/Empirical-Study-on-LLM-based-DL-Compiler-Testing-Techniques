'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(torch.var(input_data))
print(torch.var(input_data, dim=0))
print(torch.var(input_data, dim=1))
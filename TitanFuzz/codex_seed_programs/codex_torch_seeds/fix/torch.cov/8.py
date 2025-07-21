'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cov\ntorch.cov(input, *, correction=1, fweights=None, aweights=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
print(torch.cov(input_data))
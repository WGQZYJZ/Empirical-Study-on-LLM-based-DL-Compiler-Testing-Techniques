'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
import torch
input_data = torch.randn(1, 1)
output = torch.digamma(input_data)
print(output)
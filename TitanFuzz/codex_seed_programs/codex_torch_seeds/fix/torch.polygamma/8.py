'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
output = torch.polygamma(5, input_data)
print(output)
print(torch.polygamma(5, input_data).sum())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
input_data = torch.randn(1)
output = torch.polygamma(1, input_data)
print('The output tensor is:', output)
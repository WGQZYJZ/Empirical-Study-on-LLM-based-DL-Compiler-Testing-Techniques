'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.normal\ntorch.normal(mean, std, size, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output = torch.normal(input_data, torch.ones(2, 3))
print(output)
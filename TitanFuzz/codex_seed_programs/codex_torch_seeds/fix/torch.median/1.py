'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, 3)
print(input_data)
output = torch.median(input_data)
print(output)
output = torch.median(input_data, dim=1)
print(output)
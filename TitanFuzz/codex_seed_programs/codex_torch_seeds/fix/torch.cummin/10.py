'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummin\ntorch.cummin(input, dim, *, out=None)\n'
import torch
input_data = torch.rand(10)
print(input_data)
output_data = torch.cummin(input_data, dim=0)
print(output_data)
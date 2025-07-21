'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input_data = torch.rand(3, 4, 5)
print(input_data)
output_data = torch.median(input_data, dim=(- 1))
print(output_data)
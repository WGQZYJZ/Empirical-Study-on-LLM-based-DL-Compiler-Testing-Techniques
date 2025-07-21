'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
input_data = torch.arange((- 2), 3, dtype=torch.float)
print(input_data)
output_data = torch.clamp(input_data, min=(- 1), max=1)
print(output_data)
output_data = torch.clamp_min(input_data, min=(- 1))
print(output_data)
output_data = torch.clamp_max(input_data, max=1)
print(output_data)
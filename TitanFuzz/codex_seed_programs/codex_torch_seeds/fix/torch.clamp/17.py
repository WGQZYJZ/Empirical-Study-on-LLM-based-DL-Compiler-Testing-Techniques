'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input_data: ', input_data)
output_data = torch.clamp(input_data, min=(- 0.5), max=0.5)
print('output_data: ', output_data)
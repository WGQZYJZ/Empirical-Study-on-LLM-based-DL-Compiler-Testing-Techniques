'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
input_tensor = torch.rand(3, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.argsort(input_tensor, dim=(- 1), descending=False)
print('Output tensor: ', output_tensor)
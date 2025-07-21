'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
import torch
input_data = torch.randn(3, 4)
print('input_data: ', input_data)
output_data = torch.sort(input_data, dim=1)
print('output_data: ', output_data)
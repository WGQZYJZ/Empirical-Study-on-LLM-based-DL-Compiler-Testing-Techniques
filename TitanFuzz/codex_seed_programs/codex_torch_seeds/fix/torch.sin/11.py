'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sin\ntorch.sin(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('input_data: ', input_data)
output_data = torch.sin(input_data)
print('output_data: ', output_data)
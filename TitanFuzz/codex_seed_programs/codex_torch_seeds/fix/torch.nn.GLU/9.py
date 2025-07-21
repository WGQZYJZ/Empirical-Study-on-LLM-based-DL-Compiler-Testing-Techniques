'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
input_data = torch.randn(2, 3, 4)
glu_module = torch.nn.GLU(dim=(- 1))
output_data = glu_module(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)
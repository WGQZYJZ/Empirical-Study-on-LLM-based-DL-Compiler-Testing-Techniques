'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.full((5, 5), 3)
print('Input data: ', input_data)
output_data = torch.full((5, 5), 2)
print('Output data: ', output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = [1, 2, 3, 4, 5]
output_data = torch.zeros(input_data, dtype=torch.long)
print('input_data: ', input_data)
print('output_data: ', output_data)
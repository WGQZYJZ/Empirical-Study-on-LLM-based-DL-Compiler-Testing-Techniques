'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(3, 3)
output_data = torch.full(input_data.size(), 0)
print('Input data:')
print(input_data)
print('Output data:')
print(output_data)
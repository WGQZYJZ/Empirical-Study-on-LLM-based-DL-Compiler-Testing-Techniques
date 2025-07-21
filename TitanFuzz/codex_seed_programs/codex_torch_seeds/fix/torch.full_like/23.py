'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full_like\ntorch.full_like(input, fill_value, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.rand(2, 3)
print('Input data: ', input_data)
output_data = torch.full_like(input_data, fill_value=3)
print('Output data: ', output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full_like\ntorch.full_like(input, fill_value, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.arange(0, 10, dtype=torch.float)
output_data = torch.full_like(input_data, fill_value=3.14, dtype=torch.float)
print('Input data:', input_data)
print('Output data:', output_data)
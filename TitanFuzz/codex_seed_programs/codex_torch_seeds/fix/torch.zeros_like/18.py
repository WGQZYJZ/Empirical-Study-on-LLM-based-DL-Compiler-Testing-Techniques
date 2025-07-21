'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros_like\ntorch.zeros_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ', input_data)
output_data = torch.zeros_like(input_data)
print('Output data: ', output_data)
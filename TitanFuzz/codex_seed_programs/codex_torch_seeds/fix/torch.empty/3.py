'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty\ntorch.empty(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False, memory_format=torch.contiguous_format)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
output_data = torch.empty(2, 3)
print('Output data: ', output_data)
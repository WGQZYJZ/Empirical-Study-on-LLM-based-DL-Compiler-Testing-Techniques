'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logspace\ntorch.logspace(start, end, steps, base=10.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.linspace(start=0, end=10, steps=5)
print('Input data: ', input_data)
output_data = torch.logspace(start=0, end=10, steps=5)
print('Output data: ', output_data)
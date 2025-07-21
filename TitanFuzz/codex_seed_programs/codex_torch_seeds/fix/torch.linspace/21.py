'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.linspace(start=0, end=1, steps=10)
print('Input data: ', input_data)
output_data = torch.linspace(start=0, end=1, steps=10)
print('Output data: ', output_data)
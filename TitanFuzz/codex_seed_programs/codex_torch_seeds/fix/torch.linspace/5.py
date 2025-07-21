'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linspace\ntorch.linspace(start, end, steps, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.linspace((- 10), 10, 10, requires_grad=True)
print(input_data)
output_data = torch.sigmoid(input_data)
print(output_data)
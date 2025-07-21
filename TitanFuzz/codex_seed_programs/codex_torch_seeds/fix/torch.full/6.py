'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.full((2, 3), fill_value=3)
print(input_data)
print('\n')
input_data = torch.full((2, 3), fill_value=3, dtype=torch.float)
print(input_data)
print('\n')
input_data = torch.full((2, 3), fill_value=3, dtype=torch.float, layout=torch.strided, device=None, requires_grad=False)
print(input_data)
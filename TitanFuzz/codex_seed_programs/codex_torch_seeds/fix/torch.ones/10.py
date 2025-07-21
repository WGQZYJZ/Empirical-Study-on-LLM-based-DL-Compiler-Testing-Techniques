'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones\ntorch.ones(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.ones(2, 3)
print('Input data: \n', input_data)
ones_data = torch.ones(input_data.size())
print('Ones data: \n', ones_data)
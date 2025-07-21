'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
print('input_data: ', input_data)
print('torch.randn: ', torch.randn(1, 1, 3, 3))
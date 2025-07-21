'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kaiser_window\ntorch.kaiser_window(window_length, periodic=True, beta=12.0, *, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(10)
print(input_data)
output = torch.kaiser_window(10, periodic=True, beta=12.0)
print(output)
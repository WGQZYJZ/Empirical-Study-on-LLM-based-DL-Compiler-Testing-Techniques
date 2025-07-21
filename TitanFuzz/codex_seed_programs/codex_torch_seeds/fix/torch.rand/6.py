'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(10, 10)
print(input_data)
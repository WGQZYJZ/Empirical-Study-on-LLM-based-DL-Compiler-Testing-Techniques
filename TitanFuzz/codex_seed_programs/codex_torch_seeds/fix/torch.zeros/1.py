'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(1, 1, 32, 32)
output_data = torch.zeros(1, 1, 32, 32)
print(input_data)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eye\ntorch.eye(n, m=None, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.arange(0, 10)
print(input_data)
output_data = torch.eye(10)
print(output_data)
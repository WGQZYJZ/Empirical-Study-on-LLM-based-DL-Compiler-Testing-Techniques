'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logspace\ntorch.logspace(start, end, steps, base=10.0, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import torch
input_data = torch.arange(1, 101, 1)
output_data = torch.logspace(start=(- 10), end=10, steps=5)
print(input_data)
print(output_data)
print(input_data.dtype)
print(output_data.dtype)
print(input_data.size())
print(output_data.size())
print(input_data.device)
print(output_data.device)
print(input_data.requires_grad)
print(output_data.requires_grad)
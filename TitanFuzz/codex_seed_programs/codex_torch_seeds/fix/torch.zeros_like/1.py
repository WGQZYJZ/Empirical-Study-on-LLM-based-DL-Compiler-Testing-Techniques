'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros_like\ntorch.zeros_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
import torch
input_data = torch.rand(10, 5, dtype=torch.float32)
output = torch.zeros_like(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones_like\ntorch.ones_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
import torch
input_data = torch.rand(10, 5, dtype=torch.float32)
output = torch.ones_like(input_data)
print(output)
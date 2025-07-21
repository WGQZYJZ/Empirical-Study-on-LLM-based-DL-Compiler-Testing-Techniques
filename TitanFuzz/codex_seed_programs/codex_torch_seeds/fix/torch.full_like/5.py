'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full_like\ntorch.full_like(input, fill_value, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
import torch
input = torch.randn(2, 3)
output = torch.full_like(input, fill_value=3.14)
print(input)
print(output)
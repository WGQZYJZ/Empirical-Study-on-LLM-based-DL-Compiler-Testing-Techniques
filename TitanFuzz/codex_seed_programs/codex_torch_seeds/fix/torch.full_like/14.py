'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full_like\ntorch.full_like(input, fill_value, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input = torch.randn(2, 3, dtype=torch.float)
print(torch.full_like(input, fill_value=1.0))
'\nTask 1: Call the API torch.full\ntorch.full(size, fill_value, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
print(torch.full((2, 3), fill_value=2.0))
'\nTask 1: Call the API torch.full_like with non-default dtype\n'
print(torch.full_like(input, fill_value=3.0, dtype=torch.int))
'\nTask 1: Call the API torch.full with non-default dtype\n'
print(torch.full((2, 3), fill_value=4.0, dtype=torch.int))
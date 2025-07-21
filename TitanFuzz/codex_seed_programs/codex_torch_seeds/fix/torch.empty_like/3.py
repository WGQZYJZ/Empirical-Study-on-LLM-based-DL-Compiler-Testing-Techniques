'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_like\ntorch.empty_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input = torch.randn(2, 3)
print(input)
output = torch.empty_like(input)
print(output)
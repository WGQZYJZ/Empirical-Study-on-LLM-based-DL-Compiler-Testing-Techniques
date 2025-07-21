'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_like\ntorch.empty_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
x = torch.rand(3, 3)
print(x)
y = torch.empty_like(x)
print(y)